"""Exception hierarchy for the common issue-tracker API.

Hierarchy:
    IssueTrackerError
    |- ValidationError
    |- RequestError
    |  |- NotFoundError
    |  |- ConflictError
    |- AuthenticationError
    |- AuthorizationError
    |- IssueError
    |  |- IssueNotFoundError (IssueError, NotFoundError)
    |  |- IssueValidationError (IssueError, ValidationError)
    |- BoardError
       |- BoardNotFoundError (BoardError, NotFoundError)
       |- BoardValidationError (BoardError, ValidationError)
       |- BoardDeleteBlockedError (BoardError, ConflictError)
"""

class IssueTrackerError(Exception):
    """Base exception for all issue tracker API errors."""

    def __init__(
        self,
        message: str,
        *,
        provider: str | None = None,
        cause: Exception | None = None,
    ):
        super().__init__(message)
        self.provider = provider
        self.cause = cause

class ValidationError(IssueTrackerError):
    """Input payload/parameters are invalid before sending to provider."""

class RequestError(IssueTrackerError):
    """Generic remote request failure."""

class NotFoundError(RequestError):
    """Requested resource was not found in the provider."""

class ConflictError(RequestError):
    """Requested operation conflicts with current provider state."""

#Authentication-specific exceptions -------------------------------------------------------
class AuthenticationError(IssueTrackerError):
    """Authentication failed (invalid token, expired credentials)."""

class AuthorizationError(IssueTrackerError):
    """Authenticated but not allowed to perform action."""

#Issue-specific exceptions ----------------------------------------------------------------

class IssueError(IssueTrackerError):
    """Base class for issue-specific errors."""

class IssueNotFoundError(IssueError, NotFoundError):
    """Raised when an issue ID cannot be found."""

class IssueValidationError(IssueError, ValidationError):
    """Raised when issue input fails validation."""

# Board-specific exceptions -------------------------------------------------------------

class BoardError(IssueTrackerError):
    """Base class for board-specific errors."""

class BoardNotFoundError(BoardError, NotFoundError):
    """Raised when a board ID cannot be found."""

class BoardValidationError(BoardError, ValidationError):
    """Raised when board input fails validation."""

class BoardDeleteBlockedError(BoardError, ConflictError):
    """Raised when a board cannot be deleted due to provider constraints."""
