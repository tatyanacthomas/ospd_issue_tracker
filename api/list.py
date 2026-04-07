#will contain the attributes and getters for list object

from abc import ABC, abstractmethod

'''
attributes:
id  
board_id - lookup to related board object
name: str  

'''

class List(ABC):
    """Abstract base class representing a list."""

    @property
    @abstractmethod
    def id(self) -> str:
        """Return the unique identifier of the list."""
        raise NotImplementedError

    @property
    @abstractmethod
    def list_name(self) -> str:
        """Return the name of the list."""
        raise NotImplementedError