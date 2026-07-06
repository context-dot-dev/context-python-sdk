# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["MonitorListParams"]


class MonitorListParams(TypedDict, total=False):
    change_detection_type: Literal["exact", "semantic"]

    cursor: str

    limit: int

    q: str
    """Free-text search term, matched against the fields named in `search_by`."""

    search_by: List[Literal["name", "url", "query", "tags"]]
    """Comma-separated fields to search with `q`.

    Defaults to all of them. Note `query` only exists on semantic monitors.
    """

    search_type: Literal["exact", "prefix"]
    """
    `prefix` for as-you-type prefix matching (default), `exact` for full-token
    matching.
    """

    status: Literal["active", "paused", "failed"]
    """Monitor lifecycle status.

    `failed` means the most recent run failed (see the monitor's `last_error`);
    failed monitors keep running on schedule and flip back to `active` on the next
    successful run. Monitors are auto-`paused` after repeated consecutive failures
    or insufficient-credit skips; resume by PATCHing status to `active`.
    """

    tag: str
    """Filter to items that have this tag."""

    tags: SequenceNotStr[str]
    """
    Comma-separated list of tags to filter by (matches monitors having any of them).
    """

    target_type: Literal["page", "sitemap", "extract"]
