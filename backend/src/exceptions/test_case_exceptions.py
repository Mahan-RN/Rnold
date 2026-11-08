from src.exceptions.repository_exceptions import NotFoundError, ConflictError


class TestCaseNotFoundError(NotFoundError): ...


class TestCaseConflictError(ConflictError): ...
