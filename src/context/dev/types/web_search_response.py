# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebSearchResponse", "CacheMetadata", "Result", "ResultHighlights", "ResultMarkdown", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Whether this response came from cache."""

    age_ms: int
    """Age of the cached data in milliseconds. Zero for miss and zdr responses."""

    status: Literal["hit", "miss", "zdr"]
    """
    Whether the response was served from cache, required fresh work, or honored
    zero-data-retention cache bypass.
    """


class ResultHighlights(BaseModel):
    """Highlights status and passages for this result."""

    code: Literal["SUCCESS", "NOT_REQUESTED", "TIMEOUT", "CONTENT_TOO_LARGE", "WEBSITE_ACCESS_ERROR", "ERROR"]
    """Per-result highlights outcome. Inspect this before reading `highlights`."""

    highlights: Optional[List[str]] = None
    """Passages relevant to the query, in page order.

    Null unless highlightsOptions.enabled is true and the page was read.
    """


class ResultMarkdown(BaseModel):
    """Markdown scrape status and content for this result."""

    code: Literal["SUCCESS", "NOT_REQUESTED", "TIMEOUT", "CONTENT_TOO_LARGE", "WEBSITE_ACCESS_ERROR", "ERROR"]
    """Per-result scrape outcome. Inspect this before reading `markdown`."""

    markdown: Optional[str] = None
    """GFM Markdown of the page.

    Null unless markdownOptions.enabled is true and scraping succeeded.
    """

    final_dom_state: Optional[Literal["loaded", "still-loading"]] = FieldInfo(alias="finalDOMState", default=None)
    """
    `loaded`, or `still-loading` when capture ended before the page finished
    loading.
    """


class Result(BaseModel):
    description: str
    """Snippet excerpt from the page.

    Empty string when the search provider does not supply a snippet.
    """

    highlights: ResultHighlights
    """Highlights status and passages for this result."""

    markdown: ResultMarkdown
    """Markdown scrape status and content for this result."""

    relevance: Literal["high", "medium", "low"]
    """Relevance to the original query."""

    title: str
    """Page title."""

    url: str
    """Canonical result URL."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebSearchResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Whether this response came from cache."""

    query: str
    """Echo of the original query (useful when fanout was enabled)."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    results: List[Result]

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """
    True when timeoutOpts.behavior=return-partial returned the usable results
    collected before the deadline. Partial collections are not cached as complete
    results.
    """
