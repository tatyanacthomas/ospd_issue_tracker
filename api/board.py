#will contain the attributes and getters for board object

from abc import ABC, abstractmethod
from .exceptions import BoardError

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
        """Return the unique identifier of the board.

        Concrete implementations should normally return a stored identifier
        without error. If the board object is in an invalid or unusable state,
        implementations may raise BoardError or a more specific board-related
        subtype.
        """
        raise BoardError("Subclasses must implement Board.id")

    @property
    @abstractmethod
    def board_name(self) -> str:
        """Return the name of the board.

        Concrete implementations should normally return a stored name without
        error. If the board object is in an invalid or unusable state,
        implementations may raise BoardError or a more specific board-related
        subtype.
        """
        raise BoardError("Subclasses must implement Board.board_name")