#will contain the attributes and getters for board object

from abc import ABC, abstractmethod

'''
attributes:
id
name: str
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