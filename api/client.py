#will contain the client injection as well as methods for all client objects (i.e update_issue, delete_board, etc)
from abc import ABC, abstractmethod

'''
-get_issue(issue_id) - returns a single issue object by issue_id
-get_issues(board_id) - returns all issue objects in a board
-get_board(board_id) - returns a single board object by board_id
-get_boards() - retrieves boards from the session 
update_status() - REMOVED - this will be handled by update_issue() method instead, which will allow for updating any field on the issue object, including status
-update_issue(issue_id) - update any field on issue
-update_board(board_id) - update board fields on board
-delete_issue(issue_id) - delete any issue by id
-delete_board(board_id) - delete any board by id
-create_issue(issue attr) - create an issue object instance
-create_board(board attr) - create an board object instance
'''

from typing import Iterator

from .board import Board
from .issue import Issue, Status


class Client(ABC):
    """Abstract base class for an issue-tracker client."""

    # individual get methods -------------------------------------------------------------
    @abstractmethod
    def get_issue(self, issue_id: str) -> Issue:
        """Return a single issue by its ID."""
        raise NotImplementedError("Subclasses must implement get_issue")

    @abstractmethod
    def get_board(self, board_id: str) -> Board:
        """Return a single board by its ID."""
        raise NotImplementedError("Subclasses must implement get_board")

    # bulk get methods -------------------------------------------------------------------
    @abstractmethod
    def get_issues(self, board_id: str) -> Iterator[Issue]:
        """Return an iterator of issues on the board."""
        raise NotImplementedError("Subclasses must implement get_issues")

    @abstractmethod
    def get_boards(self) -> Iterator[Board]:
        """Return an iterator of boards."""
        raise NotImplementedError("Subclasses must implement get_boards")

    #update methods ------------------------------------------------------------------------
    @abstractmethod
    def update_issue(
        self,
        issue_id: str,
        title: str | None = None,
        desc: str | None = None,
        members: list[str] | None = None,
        due_date: str | None = None,
        status: Status | None = None,
        board_id: str | None = None,
    ) -> Issue:
        """Update an issue's fields."""
        raise NotImplementedError("Subclasses must implement update_issue")

    @abstractmethod
    def update_board(
        self,
        board_id: str,
        name: str | None = None,
    ) -> Board:
        """Update a board's fields."""
        raise NotImplementedError("Subclasses must implement update_board")

    # delete methods ---------------------------------------------------------------------
    @abstractmethod
    def delete_issue(self, issue_id: str) -> bool:
        """Delete an issue by its ID."""
        raise NotImplementedError("Subclasses must implement delete_issue")

    @abstractmethod
    def delete_board(self, board_id: str) -> bool:
        """Delete a board by its ID."""
        raise NotImplementedError("Subclasses must implement delete_board")

    #create methods ------------------------------------------------------------------------
    @abstractmethod
    def create_issue(
        self,
        title: str,
        board_id: str,
        desc: str | None = None,
        members: list[str] | None = None,
        due_date: str | None = None,
        status: Status = Status.TO_DO,
    ) -> Issue:
        """Create a new issue in the given board."""
        raise NotImplementedError("Subclasses must implement create_issue")

    @abstractmethod
    def create_board(self, name: str) -> Board:
        """Create a new board and return it."""
        raise NotImplementedError("Subclasses must implement create_board")

def get_client(*, interactive: bool = False) -> Client:
    """
    Create instance of Client.
    Args:
        interactive: 
            When True, the implementation can pause, prompt the user for input (login credentials),and wait for input
            When False, the implementation should rely solely on environment variables or pre-configured credentials which is good for a development environment.

    Returns:
        A concrete Client instance.

    Raises:
        NotImplementedError: Until replaced by a concrete factory.

    """
    raise NotImplementedError