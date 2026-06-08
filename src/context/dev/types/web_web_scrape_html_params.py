# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebScrapeHTMLParams", "Pdf"]


class WebWebScrapeHTMLParams(TypedDict, total=False):
    url: Required[str]
    """Full URL to scrape (must include http:// or https:// protocol)"""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """CSS selectors to remove from the result.

    Applied after includeSelectors. Exclusion takes precedence: an element matching
    both is removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".
    """

    headers: Dict[str, str]
    """
    Optional outbound HTTP headers forwarded only to the target URL, sent as
    deep-object query params such as headers[X-Custom]=value. When provided, caching
    is bypassed: the result is neither read from nor written to cache.
    """

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """When true, iframes are rendered inline into the returned HTML."""

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """CSS selectors.

    When provided, only matching subtrees (and their descendants) are kept and
    everything else is dropped. When omitted, the entire document is kept. Examples:
    "article.main", "#content", "[role=main]".
    """

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    pdf: Pdf
    """PDF parsing controls.

    Use start/end to limit text extraction and OCR to an inclusive 1-based page
    range.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """
    When true, return only the page's main content in the HTML response, excluding
    headers, footers, sidebars, and navigation when detectable.
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """Optional browser wait time in milliseconds after initial page load.

    Min: 0. Max: 30000 (30 seconds).
    """


class Pdf(TypedDict, total=False):
    """PDF parsing controls.

    Use start/end to limit text extraction and OCR to an inclusive 1-based page range.
    """

    end: int
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    start when both are provided.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF URLs are fetched and parsed.

    When false, PDF URLs are skipped and a 400 WEBSITE_ACCESS_ERROR is returned.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """
