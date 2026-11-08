from src.exceptions.repository_exceptions import ConflictError, NotFoundError


class TestCaseNotFoundError(NotFoundError): ...


class TestCaseConflictError(ConflictError): ...
