from src.exceptions.repository_exceptions import ConflictError, NotFoundError


class ProblemNotFoundError(NotFoundError): ...


class ProblemConflictError(ConflictError): ...
