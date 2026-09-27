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
    """Opaque pagination cursor from a previous response."""

    limit: int
    """Maximum number of items to return per page (1-100). Defaults to 25."""

    q: str
    """Free-text search term, matched against the fields named in `search_by`."""

    search_by: Optional[List[Literal["name", "url", "instructions", "tags"]]]
    """Fields to search with `q`.

    Defaults to all fields; page and extract targets can have instructions.
    """

    search_type: Literal["exact", "prefix"]
    """
    `prefix` for as-you-type prefix matching (default), `exact` for full-token
    matching.
    """

    status: Literal["active", "paused", "failed"]
    """Filter monitors by lifecycle status."""

    tag: str
    """Filter to items that have this tag."""

    tags: Optional[SequenceNotStr[str]]
    """
    Comma-separated list of tags to filter by (matches monitors having any of them).
    """

    target_type: Literal["page", "sitemap", "extract"]
    """Filter by target type."""
