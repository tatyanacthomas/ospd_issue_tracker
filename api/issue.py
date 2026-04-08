#will contain the attributes and getters for issue object

from abc import ABC, abstractmethod
from enum import Enum

'''
attributes:
id
title
desc
member(s) - a list of assignees associated with issue
due_date
status -  enum(to_do, in_progress, completed)
board_id - lookup to related board object

'''

class Issue(ABC):
    """Abstract base class representing a issue."""

    @property
    @abstractmethod
    def id(self) -> str:
        """Return the unique identifier of the issue."""
        raise NotImplementedError

    @property
    @abstractmethod
    def title(self) -> str:
        """Return the title of the issue."""
        raise NotImplementedError

    @property
    @abstractmethod
    def desc(self) -> str:
        """Return the description of the issue."""
        raise NotImplementedError

    @property
    @abstractmethod
    def members(self) -> list[str] | None:
        """Return the usernames or emails of the members associated with the issue, or None if unassigned."""
        raise NotImplementedError

    @property
    @abstractmethod
    def due_date(self) -> str | None:
        """Return the due date, or None if not set."""
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self) -> "Status":
        """Return the status of the issue."""
        raise NotImplementedError

    @property
    @abstractmethod 
    def board_id(self) -> str:
        """Return the id of the board associated with the issue."""
        raise NotImplementedError
        
class Status(Enum):
    """Status values for an issue."""

    TO_DO = "to_do"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"