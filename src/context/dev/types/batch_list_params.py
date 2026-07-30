# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page."""

    limit: int
    """Batches per page. Defaults to 25."""

    status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Filter by status."""

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """
