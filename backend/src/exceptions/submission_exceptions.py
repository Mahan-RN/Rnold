from src.exceptions.repository_exceptions import ConflictError, NotFoundError


class SubmissionNotFoundError(NotFoundError): ...


class SubmissionConflictError(ConflictError): ...
