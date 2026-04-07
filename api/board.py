#will contain the attributes and getters for board object

from abc import ABC, abstractmethod

'''
attributes:
id
name: str
list_ids - list of related lists (tbd on if this will be implemented)

'''

class Board(ABC):
    """Abstract base class representing a board."""

    @property
    @abstractmethod
    def id(self) -> str:
        """Return the unique identifier of the board."""
        raise NotImplementedError

    @property
    @abstractmethod
    def board_name(self) -> str:
        """Return the name of the board."""
        raise NotImplementedError

    @property
    @abstractmethod
    def list_ids(self) -> list[str] | None:
        """Return the list ids of the lists associated with the board, or None if none exist."""
        raise NotImplementedError
