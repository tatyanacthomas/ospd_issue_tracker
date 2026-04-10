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

### `api/tests/`
Unit tests that provide concrete test implementations of the abstract interfaces and verify expected behavior.

| File | Purpose |
| --- | --- |
| `api/tests/test_issue.py` | Creates a concrete `Issue` test class, verifies issue property accessors, and checks the `Status` enum values. |
| `api/tests/test_board.py` | Creates a concrete `Board` test class and verifies that board properties return the expected values. |
| `api/tests/test_client.py` | Creates a concrete `Client` test class, confirms it can be instantiated, and checks that unimplemented abstract operations raise `NotImplementedError`. |


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
```