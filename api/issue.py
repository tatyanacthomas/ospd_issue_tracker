#will contain the attributes and getters for issue object

from abc import ABC, abstractmethod
from enum import Enum
from .exceptions import IssueError

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
        """Return the unique identifier of the issue.

        Concrete implementations should normally return a stored identifier
        without error. If the issue object is in an invalid or unusable state,
        implementations may raise IssueError or a more specific issue-related
        subtype.
        """
        raise IssueError("Subclasses must implement Issue.id")

    @property
    @abstractmethod
    def title(self) -> str:
        """Return the title of the issue.

        Concrete implementations should normally return a stored title without
        error. If the issue object is in an invalid or unusable state,
        implementations may raise IssueError or a more specific issue-related
        subtype.
        """
        raise IssueError("Subclasses must implement Issue.title")

    @property
    @abstractmethod
    def desc(self) -> str:
        """Return the description of the issue.

        Concrete implementations should normally return a stored description
        without error. If the issue object is in an invalid or unusable state,
        implementations may raise IssueError or a more specific issue-related
        subtype.
        """
        raise IssueError("Subclasses must implement Issue.desc")

    @property
    @abstractmethod
    def members(self) -> list[str] | None:
        """Return the issue emails and/or names of assignees, or None if the issue is unassigned.

        Concrete implementations should normally return stored assignee data
        without error. If the issue object is in an invalid or unusable state,
        implementations may raise IssueError or a more specific issue-related
        subtype.
        """
        raise IssueError("Subclasses must implement Issue.members")

    @property
    @abstractmethod
    def due_date(self) -> str | None:
        """Return the due date, or None if not set.

        Concrete implementations should normally return stored due-date data
        without error. If the issue object is in an invalid or unusable state,
        implementations may raise IssueError or a more specific issue-related
        subtype.
        """
        raise IssueError("Subclasses must implement Issue.due_date")

    @property
    @abstractmethod
    def status(self) -> "Status":
        """Return the status of the issue.

        Concrete implementations should normally return a stored status without
        error. If the issue object is in an invalid or unusable state,
        implementations may raise IssueError or a more specific issue-related
        subtype.
        """
        raise IssueError("Subclasses must implement Issue.status")

    @property
    @abstractmethod 
    def board_id(self) -> str:
        """Return the id of the board associated with the issue.

        Concrete implementations should normally return a stored board id
        without error. If the issue object is in an invalid or unusable state,
        implementations may raise IssueError or a more specific issue-related
        subtype.
        """
        raise IssueError("Subclasses must implement Issue.board_id")
        
class Status(Enum):
    """Status values for an issue."""

    TO_DO = "to_do"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"