from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from issue import Issue, Status


class ConcreteIssue(Issue):
	def __init__(
		self,
		issue_id: str,
		board_id: str,
		title: str,
		desc: str,
		members: list[str] | None,
		due_date: str | None,
		status: Status
	):
		self._id = issue_id
		self._board_id = board_id
		self._title = title
		self._desc = desc
		self._members = members
		self._due_date = due_date
		self._status = status

	@property
	def id(self) -> str:
		return self._id

	@property
	def board_id(self) -> str:
		return self._board_id

	@property
	def title(self) -> str:
		return self._title

	@property
	def desc(self) -> str:
		return self._desc

	@property
	def members(self) -> list[str] | None:
		return self._members

	@property
	def due_date(self) -> str | None:
		return self._due_date

	@property
	def status(self) -> Status:
		return self._status


@pytest.fixture
def sample_issue() -> ConcreteIssue:
	return ConcreteIssue(
		issue_id="issue-1",
		board_id="board-1",
		title="Fix login bug",
		desc="Users cannot log in with SSO.",
		members=["dev1", "dev2"],
		due_date="2026-04-30",
		status=Status.IN_PROGRESS
	)


def test_issue_getters_return_expected_values(sample_issue):
	assert sample_issue.id == "issue-1"
	assert sample_issue.board_id == "board-1"
	assert sample_issue.title == "Fix login bug"
	assert sample_issue.desc == "Users cannot log in with SSO."
	assert sample_issue.members == ["dev1", "dev2"]
	assert sample_issue.due_date == "2026-04-30"
	assert sample_issue.status == Status.IN_PROGRESS




@pytest.mark.parametrize(
	"status, expected",
	[
		(Status.TO_DO, "to_do"),
		(Status.IN_PROGRESS, "in_progress"),
		(Status.COMPLETED, "completed"),
	],
)
def test_status_enum_values(status, expected):
	assert status.value == expected
