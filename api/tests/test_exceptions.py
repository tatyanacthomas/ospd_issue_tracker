from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))

from api.exceptions import (
	AuthenticationError,
	AuthorizationError,
	BoardDeleteBlockedError,
	BoardError,
	BoardNotFoundError,
	BoardValidationError,
	ConflictError,
	IssueError,
	IssueNotFoundError,
	IssueTrackerError,
	IssueValidationError,
	NotFoundError,
	RequestError,
	ValidationError,
)


def test_base_exception_stores_metadata():
	cause = ValueError("bad token")
	err = IssueTrackerError("boom", provider="jira", cause=cause)

	assert str(err) == "boom"
	assert err.provider == "jira"
	assert err.cause is cause


def test_core_exceptions_inherit_from_base():
	assert issubclass(ValidationError, IssueTrackerError)
	assert issubclass(AuthenticationError, IssueTrackerError)
	assert issubclass(AuthorizationError, IssueTrackerError)
	assert issubclass(RequestError, IssueTrackerError)


def test_request_subclasses():
	assert issubclass(NotFoundError, RequestError)
	assert issubclass(ConflictError, RequestError)


def test_issue_specific_exceptions():
	assert issubclass(IssueError, IssueTrackerError)
	assert issubclass(IssueNotFoundError, IssueError)
	assert issubclass(IssueNotFoundError, NotFoundError)
	assert issubclass(IssueValidationError, IssueError)
	assert issubclass(IssueValidationError, ValidationError)


def test_board_specific_exceptions():
	assert issubclass(BoardError, IssueTrackerError)
	assert issubclass(BoardNotFoundError, BoardError)
	assert issubclass(BoardNotFoundError, NotFoundError)
	assert issubclass(BoardValidationError, BoardError)
	assert issubclass(BoardValidationError, ValidationError)
	assert issubclass(BoardDeleteBlockedError, BoardError)
	assert issubclass(BoardDeleteBlockedError, ConflictError)

