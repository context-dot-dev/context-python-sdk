# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebSearchResponse", "CacheMetadata", "Result", "ResultMarkdown", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing to the output was a hit; age_ms is the oldest contributing hit.
    """

    age_ms: int
    """Age of the cached data in milliseconds. Zero for miss and zdr responses."""

    status: Literal["hit", "miss", "zdr"]
    """
    Whether the response was served from cache, required fresh work, or honored
    zero-data-retention cache bypass.
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
    """How complete the returned content is.

    `loaded` means the page finished the waits the request asked for.
    `still-loading` only occurs with timeoutOpts.behavior=return-partial: the
    timeoutOpts.milliseconds deadline was reached first, so the content reflects the
    DOM at that moment and late-rendering parts may be missing. Partial results are
    billed at the base request cost.
    """


class Result(BaseModel):
    description: str
    """Snippet excerpt from the page."""

    markdown: ResultMarkdown
    """Markdown scrape status and content for this result."""

    relevance: Literal["high", "medium", "low"]
    """Relevance to the original query."""

    title: str
    """Page title."""

    url: str
    """Canonical result URL."""


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebSearchResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    query: str
    """Echo of the original query (useful when fanout was enabled)."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    results: List[Result]

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
    """
    True when timeoutOpts.behavior=return-partial returned the usable results
    collected before the deadline. Partial collections are not cached as complete
    results.
    """
