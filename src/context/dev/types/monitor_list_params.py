# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["MonitorListParams"]


class MonitorListParams(TypedDict, total=False):
    change_detection_type: Literal["exact", "semantic"]
    """Filter by change detection type."""

    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of monitors to return per page. Defaults to 25."""

    q: str
    """Text to search for in the fields listed in `search_by`."""

    search_by: Optional[List[Literal["name", "url", "instructions", "tags"]]]
    """Comma-separated fields to search with `q`.

    Defaults to all fields. For search targets, `url` matches the target's `query`.
    """

    search_type: Literal["exact", "prefix"]
    """How `q` matches.

    `prefix` matches the start of words and tolerates one typo, for search as you
    type; `exact` matches whole words only. Defaults to `prefix`.
    """

    status: Literal["active", "paused", "failed"]
    """Filter by monitor status."""

    tags: Optional[SequenceNotStr[str]]
    """Comma-separated tags. Returns monitors that have any of them."""

    target_type: Literal["page", "sitemap", "extract", "search"]
    """Filter by target type."""
