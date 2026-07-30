# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["BatchGetResultsParams"]


class BatchGetResultsParams(TypedDict, total=False):
    cursor: str
    """next_cursor from the previous page."""

    limit: int
    """Records per page.

    Defaults to 25. A page can close early so its payload stays under ~8 MB; rely on
    next_cursor rather than counting records.
    """

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """
