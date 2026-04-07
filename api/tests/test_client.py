from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from issue import Issue, Status
from list import List
from board import Board
from client import Client


class ConcreteClient(Client):
	def get_issue(self, issue_id: str) -> Issue:
		return super().get_issue(issue_id)

	def get_list(self, list_id: str) -> List:
		return super().get_list(list_id)

	def get_board(self, board_id: str) -> Board:
		return super().get_board(board_id)

	def get_issues(self, list_id: str):
		return super().get_issues(list_id)

	def get_lists(self, board_id: str):
		return super().get_lists(board_id)

	def get_boards(self):
		return super().get_boards()

	def update_issue(
		self,
		issue_id: str,
		title: str | None = None,
		desc: str | None = None,
		members: list[str] | None = None,
		due_date: str | None = None,
		status: Status | None = None,
		list_id: str | None = None,
		board_id: str | None = None,
	) -> Issue:
		return super().update_issue(issue_id, title, desc, members, due_date, status, list_id, board_id)

	def update_list(self, list_id: str, name: str) -> List:
		return super().update_list(list_id, name)

	def update_board(
		self,
		board_id: str,
		name: str | None = None,
		list_ids: list[str] | None = None,
	) -> Board:
		return super().update_board(board_id, name, list_ids)

	def delete_issue(self, issue_id: str) -> bool:
		return super().delete_issue(issue_id)

	def delete_list(self, list_id: str) -> bool:
		return super().delete_list(list_id)

	def delete_board(self, board_id: str) -> bool:
		return super().delete_board(board_id)

	def create_issue(
		self,
		title: str,
		list_id: str,
		board_id: str,
		desc: str | None = None,
		members: list[str] | None = None,
		due_date: str | None = None,
		status: Status = Status.TO_DO, 
	) -> Issue:
		return super().create_issue(
			title,
			list_id=list_id,
			board_id=board_id,
			desc=desc,
			members=members,
			due_date=due_date,
			status=status,
		)

	def create_list(self, name: str) -> List:
		return super().create_list(name)

	def create_board(self, name: str, list_ids: list[str] | None = None) -> Board:
		return super().create_board(name, list_ids)


@pytest.fixture
def sample_client() -> ConcreteClient:
	return ConcreteClient()


def test_concrete_client_can_be_instantiated():
	client = ConcreteClient()
	assert isinstance(client, ConcreteClient)
	assert isinstance(client, Client)


def test_get_issue_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement get_issue"):
		sample_client.get_issue("issue-1")


def test_get_list_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement get_list"):
		sample_client.get_list("list-1")


def test_get_board_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement get_board"):
		sample_client.get_board("board-1")


def test_get_issues_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement get_issues"):
		list(sample_client.get_issues("list-1"))


def test_get_lists_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement get_lists"):
		list(sample_client.get_lists("board-1"))


def test_get_boards_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement get_boards"):
		list(sample_client.get_boards())


def test_update_issue_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement update_issue"):
		sample_client.update_issue("issue-1", title="Updated title")


def test_update_list_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement update_list"):
		sample_client.update_list("list-1", "In Progress")


def test_update_board_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement update_board"):
		sample_client.update_board("board-1", name="Platform")


def test_delete_issue_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement delete_issue"):
		sample_client.delete_issue("issue-1")


def test_delete_list_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement delete_list"):
		sample_client.delete_list("list-1")


def test_delete_board_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement delete_board"):
		sample_client.delete_board("board-1")


def test_create_issue_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement create_issue"):
		sample_client.create_issue("New issue", list_id="list-1", board_id="board-1")


def test_create_list_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement create_list"):
		sample_client.create_list("Done")


def test_create_board_raises_not_implemented(sample_client):
	with pytest.raises(NotImplementedError, match="Subclasses must implement create_board"):
		sample_client.create_board("Engineering Board", ["list-1", "list-2"])