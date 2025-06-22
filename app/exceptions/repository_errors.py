class RepositoryError(Exception):
    """Base class for repository-related errors."""
    pass

class NotFoundError(RepositoryError):
    """Raised when an object is not found in the database."""
    def __init__(self, message: str = "Item not found"):
        super().__init__(message)

class CreationError(RepositoryError):
    """Raised when an object creation fails."""
    def __init__(self, message: str = "Failed to create item"):
        super().__init__(message)

class DeletionError(RepositoryError):
    """Raised when an object deletion fails."""
    def __init__(self, message: str = "Failed to delete item"):
        super().__init__(message)