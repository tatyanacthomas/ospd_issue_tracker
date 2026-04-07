from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from board import Board

class ConcreteBoard(Board):
	def __init__(
		self,
		board_id: str,
		board_name: str,
		list_ids: list[str] | None,
	):
		self._id = board_id
		self._board_name = board_name
		self._list_ids = list_ids

	@property
	def id(self) -> str:
		return self._id

	@property
	def board_name(self) -> str:
		return self._board_name

	@property
	def list_ids(self) -> list[str] | None:
		return self._list_ids


@pytest.fixture
def sample_board() -> ConcreteBoard:
	return ConcreteBoard(
		board_id="board-1",
		board_name="Engineering Board",
		list_ids=["list-1", "list-2"],
	)


def test_board_getters_return_expected_values(sample_board):
	assert sample_board.id == "board-1"
	assert sample_board.board_name == "Engineering Board"
	assert sample_board.list_ids == ["list-1", "list-2"]
