# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page."""

    limit: int
    """Batches per page. Defaults to 25."""

    q: str
    """
    Free-text search term, matched against the batch id, crawl source (start URL or
    sitemap domain), and tags.
    """

    search_type: Literal["exact", "prefix"]
    """
    `prefix` for as-you-type prefix matching (default), `exact` for full-token
    matching.
    """

    status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Filter by status."""

    tags: str
    """Comma-separated list of tags to filter by (matches batches having any of them)."""
