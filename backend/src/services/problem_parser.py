import logging
from pathlib import Path
from typing import TypedDict

from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.exceptions.evaluation_case_exceptions import EvaluationCaseNotFoundError
from src.exceptions.problem_exceptions import ProblemNotFoundError
from src.exceptions.problem_parser_exceptions import (
    InvalidDataDirectoryError,
    InvalidPathError,
    InvalidProblemTemplateFormatError,
)
from src.schemas.problem_parser import ParsedProblem, ParsedTestCase
from src.services import evaluation_case_services, problem_services, topic_services


class ParserOutput(TypedDict):
    problem: ParsedProblem
    test_cases: list[ParsedTestCase]


logging.basicConfig(
    filename="problem_parser.log", encoding="utf-8", level=logging.DEBUG, filemode="w"
)
logger = logging.getLogger(__name__)


def load_problem_data(db_session: Session, path: Path) -> None:
    """Loads problems data from a given direcotry and commits them to DB

    @Note: suitable as a Lifespan function

    Args:
        db_session (Session): database session
        path (Path): path to the directory containing problem files
    """
    parser_outputs: list[ParserOutput] = _parse_problem_directory(path)

    for parser_output in parser_outputs:
        write_parser_output_to_db(parser_output, db_session)

    db_session.commit()


def write_parser_output_to_db(parser_output: ParserOutput, db_session: Session) -> None:
    """Takes a ParserOutput object and flushes it to DB

    @Note: the caller is responsible for commiting the data to the database!

    Args:
        parser_output (ParserOutput): ParserOutput object to be flushed to DB
        db_session (Session): DB session
    """
    parsed_problem = parser_output["problem"]
    topic_name = parsed_problem.topic_name
    topic_id = topic_services.get_by_name(topic_name, db_session).id
    try:
        problem = problem_services.get_by_title(parsed_problem.title, db_session)
        problem = problem_services.update_one(
            id=problem.id,
            topic_id=topic_id,
            sort_order=parsed_problem.sort_order,
            title=parsed_problem.title,
            description=parsed_problem.description,
            difficulty=parsed_problem.difficulty,
            starter_code=parsed_problem.starter_code,
            session=db_session,
        )
    except ProblemNotFoundError:
        problem = problem_services.insert_one(
            topic_id=topic_id,
            sort_order=parsed_problem.sort_order,
            title=parsed_problem.title,
            description=parsed_problem.description,
            difficulty=parsed_problem.difficulty,
            starter_code=parsed_problem.starter_code,
            session=db_session,
        )
    problem_id = problem.id

    for parsed_test_case in parser_output["test_cases"]:
        try:
            test_case = evaluation_case_services.get_by_unique_constraint(
                problem_id, parsed_test_case.sort_order, db_session
            )
            evaluation_case_services.update_one(
                id=test_case.id,
                problem_id=problem_id,
                sort_order=parsed_test_case.sort_order,
                code=parsed_test_case.code,
                session=db_session,
            )
        except EvaluationCaseNotFoundError:
            evaluation_case_services.insert_one(
                problem_id=problem_id,
                sort_order=parsed_test_case.sort_order,
                code=parsed_test_case.code,
                session=db_session,
            )


def parse_problem(text: str) -> ParserOutput:
    """Parses the string content of a single problem template file into a ParserOutput object

    Args:
        text (str): string content of a problem template file

    Returns:
        ParserOutput: parsed object containing problem and test data
    """
    sections: list[str] = text.split("#@")
    _validate_sections(sections)
    parsed_problem = _problem_parser(sections[2])
    test_cases: list[ParsedTestCase] = []
    for i in range(3, len(sections)):
        test_cases.append(_test_case_parser(sections[i]))

    return {"problem": parsed_problem, "test_cases": test_cases}


# -- Private Helpers --


def _parse_problem_directory(directory: Path) -> list[ParserOutput]:
    """Parses files in a given directory as ParserOutput objects

    Args:
        directory (Path): directory containing problem files

    Raises:
        InvalidPathError: raised when directory path is invalid
        InvalidDataDirectoryError: raised when the path doesn't point to a directory

    Returns:
        list[ParserOutput]: list of ParserOutput objects
    """
    results: list[ParserOutput] = []
    if not directory.exists():
        raise InvalidPathError(f"Path {directory!s} does not exist")
    elif not directory.is_dir():
        raise InvalidDataDirectoryError(
            f"Path {directory!s} does not point to a directory"
        )
    else:
        for file in directory.iterdir():
            if file.is_file() and file.suffix.upper() == ".R":
                text = file.read_text()
                try:
                    results.append(parse_problem(text))
                except InvalidProblemTemplateFormatError:
                    logger.warning(f"File {file!s} has invalid problem template")
                    raise
                except ValidationError:
                    logger.warning(f"File {file!s} has type error in problem template")
                    raise
        return results


def _validate_sections(sections: list[str]) -> None:
    """Checks to ensure extracted sections from problem template file are all included and in the correct order

    Args:
        sections (list[str]): list of sections extracted from problem template file

    Raises:
        InvalidProblemTemplateFormatError: missing at least 1 of the required sections
        InvalidProblemTemplateFormatError: preamble section absent
        InvalidProblemTemplateFormatError: problem section absent
        InvalidProblemTemplateFormatError: test case section absent
    """
    PREAMBLE_HEADER = "Preamble"
    PROBLEM_HEADER = "Problem"
    TEST_CASE_HEADER = "Test Case"

    if len(sections) < 3:
        raise InvalidProblemTemplateFormatError(
            "A Problem template file must at least have 3 sections: Preamble, Problem, Test Case"
        )
    if PREAMBLE_HEADER not in sections[1]:
        raise InvalidProblemTemplateFormatError(
            "Preamble tag missing from the first section of the template"
        )
    if PROBLEM_HEADER not in sections[2]:
        raise InvalidProblemTemplateFormatError(
            "Problem tag missing from the second section of the template"
        )
    for i in range(3, len(sections)):
        curr_section = sections[i]
        if TEST_CASE_HEADER not in curr_section:
            raise InvalidProblemTemplateFormatError(
                "Test Case tag missing from the third section of the template"
            )


def _problem_parser(text: str) -> ParsedProblem:
    """Parses problem metadata from the problems section of the template problem file

    Args:
        text (str): problem section

    Returns:
        ParsedProblem: parsed problem metadata
    """
    TOPIC_NAME_KEY = "topic_name:"
    SORT_ORDER_KEY = "sort_order:"
    TITLE_KEY = "title:"
    DIFFICULTY_KEY = "difficulty:"
    BEGIN_DESCRIPTION = "--begin_description"
    END_DESCRIPTION = "--end_description"
    BEGIN_CODE = "begin_starter_code"
    END_CODE = "end_starter_code"

    is_description = False
    is_code = False

    lines = text.split("\n")
    data = {
        "topic_name": "",
        "sort_order": "",
        "title": "",
        "difficulty": "",
        "description": "",
        "starter_code": "",
    }

    for i in range(1, len(lines)):
        curr_line = lines[i]

        if TOPIC_NAME_KEY in curr_line:
            data["topic_name"] = _extract_metadata_from_line(curr_line, TOPIC_NAME_KEY)
        elif SORT_ORDER_KEY in curr_line:
            data["sort_order"] = _extract_metadata_from_line(curr_line, SORT_ORDER_KEY)
        elif TITLE_KEY in curr_line:
            data["title"] = _extract_metadata_from_line(curr_line, TITLE_KEY)
        elif DIFFICULTY_KEY in curr_line:
            data["difficulty"] = _extract_metadata_from_line(curr_line, DIFFICULTY_KEY)
        elif BEGIN_DESCRIPTION in curr_line:
            is_description = True
        elif is_description and END_DESCRIPTION not in curr_line:
            data["description"] += curr_line.strip() + "\n"
        elif END_DESCRIPTION in curr_line:
            is_description = False
        elif BEGIN_CODE in curr_line:
            is_code = True
        elif is_code and END_CODE not in curr_line:
            data["starter_code"] += curr_line.rstrip(" \t") + "\n"
        elif END_CODE in curr_line:
            break

    return ParsedProblem.model_validate(data)


def _test_case_parser(text: str) -> ParsedTestCase:
    """Parses test case metadata from the test case section of the template problem file

    Args:
        text (str): test case section

    Returns:
        ParsedTestCase: parsed test case metadata
    """
    SORT_ORDER_KEY = "sort_order:"
    BEGIN_CODE = "begin_test_case"
    END_CODE = "end_test_case"
    is_code = False

    lines = text.split("\n")

    data = {"sort_order": "", "code": ""}

    for i in range(1, len(lines)):
        curr_line = lines[i]

        if SORT_ORDER_KEY in curr_line:
            data["sort_order"] = _extract_metadata_from_line(curr_line, SORT_ORDER_KEY)
        elif BEGIN_CODE in curr_line:
            is_code = True
        elif is_code and END_CODE not in curr_line:
            data["code"] += curr_line.rstrip(" \t") + "\n"
        elif END_CODE in curr_line:
            break

    return ParsedTestCase.model_validate(data)


def _extract_metadata_from_line(line: str, key: str) -> str:
    """String clean up helper to remove extra space, comment marker (#), and keyword

    Args:
        line (str): line of a document to be processed
        key (str): keyword to be removed from this line

    Returns:
        str: cleaned up string
    """
    line = line.lstrip()
    line = line.replace("#", "", 1)
    line = line.replace(key, "", 1)
    result = line.strip()
    return result
