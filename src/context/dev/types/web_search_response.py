# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebSearchResponse", "CacheMetadata", "Result", "ResultHighlights", "ResultMarkdown", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Cache status of this response."""

    age_ms: int
    """Age of the cached data, in milliseconds. `0` for `miss` and `zdr`."""

    status: Literal["hit", "miss", "zdr"]
    """
    `hit` when served from cache, `miss` when fetched fresh, `zdr` when zero data
    retention bypassed the cache.
    """


class ResultHighlights(BaseModel):
    """Highlights status and passages for this result."""

    code: Literal[
        "SUCCESS",
        "NOT_REQUESTED",
        "TIMEOUT",
        "CONTENT_TOO_LARGE",
        "WEBSITE_ACCESS_ERROR",
        "WEBSITE_BLOCKED",
        "WEBSITE_NOT_FOUND",
        "ERROR",
    ]
    """Highlights outcome for this result. Check it before reading `highlights`."""

    highlights: Optional[List[str]] = None
    """Passages relevant to the query, in page order.

    `null` unless `highlightsOptions.enabled` is `true` and the page was read.
    """

    message: Optional[str] = None
    """Why this output is missing. Present only when `code` is a failure."""


class ResultMarkdown(BaseModel):
    """Markdown scrape status and content for this result."""

    code: Literal[
        "SUCCESS",
        "NOT_REQUESTED",
        "TIMEOUT",
        "CONTENT_TOO_LARGE",
        "WEBSITE_ACCESS_ERROR",
        "WEBSITE_BLOCKED",
        "WEBSITE_NOT_FOUND",
        "ERROR",
    ]
    """Scrape outcome for this result. Check it before reading `markdown`."""

    markdown: Optional[str] = None
    """Page content as GitHub-flavored Markdown.

    `null` unless `markdownOptions.enabled` is `true` and the scrape succeeded.
    """

    final_dom_state: Optional[Literal["loaded", "still-loading"]] = FieldInfo(alias="finalDOMState", default=None)
    """
    `loaded`, or `still-loading` when capture ended before the page finished
    loading.
    """

    message: Optional[str] = None
    """Why this output is missing. Present only when `code` is a failure."""


class Result(BaseModel):
    description: str
    """Snippet from the page. Empty string when no snippet is available."""

    highlights: ResultHighlights
    """Highlights status and passages for this result."""

    markdown: ResultMarkdown
    """Markdown scrape status and content for this result."""

    relevance: Literal["high", "medium", "low"]
    """How relevant the result is to the query."""

    title: str
    """Page title."""

    url: str
    """Canonical result URL."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class WebSearchResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache status of this response."""

    query: str
    """The query you sent."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    results: List[Result]

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """
    `true` when the deadline passed with `timeoutOpts.behavior` set to
    `return-partial`. Only results finished in time are included. Partial results
    are not cached.
    """
