# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BatchGetResultsParams"]


class BatchGetResultsParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of results to return per page.

    A page can hold fewer to stay under about 8 MB, so page with `next_cursor`
    instead of counting records.
    """
