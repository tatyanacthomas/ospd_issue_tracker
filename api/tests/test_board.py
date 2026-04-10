from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[2]))

from api.board import Board

class ConcreteBoard(Board):
	def __init__(
		self,
		board_id: str,
		board_name: str,
	):
		self._id = board_id
		self._board_name = board_name

	@property
	def id(self) -> str:
		return self._id

	@property
	def board_name(self) -> str:
		return self._board_name

@pytest.fixture
def sample_board() -> ConcreteBoard:
	return ConcreteBoard(
		board_id="board-1",
		board_name="Engineering Board",
	)


def test_board_getters_return_expected_values(sample_board):
	assert sample_board.id == "board-1"
	assert sample_board.board_name == "Engineering Board"