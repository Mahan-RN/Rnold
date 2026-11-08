from src.exceptions.repository_exceptions import NotFoundError, ConflictError


class UserNotFoundError(NotFoundError): ...


class UserConflictError(ConflictError): ...


class LastAdminDeletionError(Exception): ...
