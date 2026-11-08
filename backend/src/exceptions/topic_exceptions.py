from src.exceptions.repository_exceptions import ConflictError, NotFoundError


class TopicNotFoundError(NotFoundError): ...


class TopicConflictError(ConflictError): ...
