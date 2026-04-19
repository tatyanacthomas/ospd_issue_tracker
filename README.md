# ospd_issue_tracker

This repository defines an abstract common API along with unit tests.

## Repository overview

### `api/`
Core interface definitions for boards, issues, lists, and clients.

| File | Purpose |
| --- | --- |
| `api/issue.py` | Defines the abstract `Issue` model and the `Status` enum (`TO_DO`, `IN_PROGRESS`, `COMPLETED`). |
| `api/board.py` | Defines the abstract `Board` model, including required properties such as `id` and `board_name` |
| `api/client.py` | Defines the abstract `Client` contract for retrieving, creating, updating, and deleting boards and issues. It also includes a placeholder `get_client()` factory function. |
| `api/exceptions.py` | Defines the shared exception hierarchy that concrete client implementations can raise to communicate validation, request, authentication, authorization, issue, and board errors. |

### `api/tests/`
Unit tests that provide concrete test implementations of the abstract interfaces and verify expected behavior.

| File | Purpose |
| --- | --- |
| `api/tests/test_issue.py` | Creates a concrete `Issue` test class, verifies issue property accessors, and checks the `Status` enum values. |
| `api/tests/test_board.py` | Creates a concrete `Board` test class and verifies that board properties return the expected values. |
| `api/tests/test_client.py` | Creates a concrete `Client` test class, confirms it can be instantiated, and checks that unimplemented abstract operations raise `IssueError` or `BoardError`, depending on the method. |
| `api/tests/test_exceptions.py` | Verifies the shared exception hierarchy, including inheritance relationships and exception metadata such as `provider` and `cause`. |


## Project setup with uv

### 1. Install uv

`pip install uv`

### 2. Create and sync the environment

From the repository root:

```bash
source .venv/bin/activate && uv sync --extra dev
```

This reads [pyproject.toml](pyproject.toml), creates a virtual environment, and installs dependencies.

### 3. Run tests

```bash
uv run pytest
```

## How other repos can depend on this package

### From GitHub

In another project:

```bash
uv add "ospd-issue-tracker-api @ git+https://github.com/tatyanacthomas/ospd_issue_tracker.git@main"
```

### Example import

```python
from api.client import Client
from api.issue import Issue, Status
from api.board import Board
from api.exceptions import IssueNotFoundError, BoardValidationError
```

## Exception types

Concrete implementations can use the shared exception types from `api.exceptions`. The heirarchy and use cases can be found below. 

### Outline of Exception Hierarchy

```text
IssueTrackerError
|- ValidationError
|- RequestError
|  |- NotFoundError
|  |- ConflictError
|- AuthenticationError
|- AuthorizationError
|- IssueError
|  |- IssueNotFoundError (IssueError, NotFoundError)
|  |- IssueValidationError (IssueError, ValidationError)
|- BoardError
   |- BoardNotFoundError (BoardError, NotFoundError)
   |- BoardValidationError (BoardError, ValidationError)
   |- BoardDeleteBlockedError (BoardError, ConflictError)
```

### Available exceptions

| Exception | Use when |
| --- | --- |
| `IssueTrackerError` | A general issue-tracker error does not fit a more specific type. |
| `ValidationError` | Input payload or parameters are invalid before sending to a provider. |
| `RequestError` | A remote request fails in a generic way. |
| `NotFoundError` | A requested resource does not exist in the provider. |
| `ConflictError` | An operation conflicts with current provider state. |
| `AuthenticationError` | Authentication fails because credentials are invalid, missing, or expired. |
| `AuthorizationError` | Authentication succeeded but the caller is not allowed to perform the action. |
| `IssueError` | A general issue-related error does not fit a more specific issue exception. |
| `IssueNotFoundError` | A requested issue ID does not exist. |
| `IssueValidationError` | Issue creation or update input is invalid. |
| `BoardError` | A general board-related error does not fit a more specific board exception. |
| `BoardNotFoundError` | A requested board ID does not exist. |
| `BoardValidationError` | Board creation or update input is invalid. |
| `BoardDeleteBlockedError` | A board cannot be deleted because provider constraints block the operation. |


Because some exceptions use multiple inheritance, callers can catch either a
specific type such as `IssueNotFoundError` or a broader category such as
`IssueError` or `NotFoundError`.