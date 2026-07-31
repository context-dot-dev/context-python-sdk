# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BatchGetResultsParams"]


class BatchGetResultsParams(TypedDict, total=False):
    cursor: str
    """next_cursor from the previous page."""

    limit: int
    """Records per page.

    Defaults to 25. A page can close early so its payload stays under ~8 MB; rely on
    next_cursor rather than counting records.
    """
