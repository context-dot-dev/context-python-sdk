# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of batches to return per page."""

    q: str
    """
    Search term matched against batch IDs, crawl sources (start URL or sitemap
    domain), and tags.
    """

    search_type: Literal["exact", "prefix"]
    """
    How `q` matches: `prefix` matches the start of a term, for search-as-you-type,
    and `exact` matches whole terms. Defaults to `prefix`.
    """

    status: Literal["pending", "queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Filter by batch status."""

    tags: Union[str, SequenceNotStr[str]]
    """Comma-separated tags.

    Returns batches that have any of them. You can also repeat the `tags` parameter.
    """
