# ospd_issue_tracker

This repository defines an abstract common API along with unit tests.

## Repository overview

### `api/`
Core interface definitions for boards, issues, lists, and clients.

| File | Purpose |
| --- | --- |
| `api/issue.py` | Defines the abstract `Issue` model and the `Status` enum (`TO_DO`, `IN_PROGRESS`, `COMPLETED`). |
| `api/list.py` | Defines the abstract `List` model and its required list metadata. |
| `api/board.py` | Defines the abstract `Board` model, including required properties such as `id`, `board_name`, and `list_ids`. |
| `api/client.py` | Defines the abstract `Client` contract for retrieving, creating, updating, and deleting boards, lists, and issues. It also includes a placeholder `get_client()` factory function. |

### `api/tests/`
Unit tests that provide concrete test implementations of the abstract interfaces and verify expected behavior.

| File | Purpose |
| --- | --- |
| `api/tests/test_issue.py` | Creates a concrete `Issue` test class, verifies issue property accessors, and checks the `Status` enum values. |
| `api/tests/test_list.py` | Creates a concrete `List` test class and verifies that list properties return the expected values. |
| `api/tests/test_board.py` | Creates a concrete `Board` test class and verifies that board properties return the expected values. |
| `api/tests/test_client.py` | Creates a concrete `Client` test class, confirms it can be instantiated, and checks that unimplemented abstract operations raise `NotImplementedError`. |


## Running the tests

From the repository root:

```bash
pytest api/tests/
```
