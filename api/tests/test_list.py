from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from list import List

class ConcreteList(List):
	def __init__(
		self,
		list_id: str,
		list_name: str,
		card_ids: list[str] | None,
	):
		self._id = list_id
		self._list_name = list_name
		self._card_ids = card_ids

	@property
	def id(self) -> str:
		return self._id

	@property
	def list_name(self) -> str:
		return self._list_name

	@property
	def card_ids(self) -> list[str] | None:
		return self._card_ids


@pytest.fixture
def sample_list() -> ConcreteList:
	return ConcreteList(
		list_id="list-1",
		list_name="To Do",
		card_ids=["card-1", "card-2"],
	)


def test_list_getters_return_expected_values(sample_list):
	assert sample_list.id == "list-1"
	assert sample_list.list_name == "To Do"
	assert sample_list.card_ids == ["card-1", "card-2"]