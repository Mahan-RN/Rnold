from src.exceptions.repository_exceptions import NotFoundError, ConflictError


class TopicNotFoundError(NotFoundError): ...


class TopicConflictError(ConflictError): ...
