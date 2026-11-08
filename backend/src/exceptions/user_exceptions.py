from src.exceptions.repository_exceptions import ConflictError, NotFoundError


class UserNotFoundError(NotFoundError): ...


class UserConflictError(ConflictError): ...


class LastAdminDeletionError(Exception): ...
