from src.exceptions.repository_exceptions import NotFoundError, ConflictError


class SubmissionNotFoundError(NotFoundError): ...


class SubmissionConflictError(ConflictError): ...
