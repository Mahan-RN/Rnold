from src.exceptions.repository_exceptions import ConflictError, NotFoundError


class EvaluationCaseNotFoundError(NotFoundError): ...


class EvaluationCaseConflictError(ConflictError): ...
