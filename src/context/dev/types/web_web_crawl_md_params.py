# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebWebCrawlMdParams", "Pdf"]


class WebWebCrawlMdParams(TypedDict, total=False):
    url: Required[str]
    """The starting URL for the crawl (must include http:// or https:// protocol)"""

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """When true, follow links on subdomains of the starting URL's domain (e.g.

    docs.example.com when starting from example.com). www and apex are always
    treated as equivalent.
    """

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """
    When true, the contents of iframes are rendered to Markdown for each crawled
    page.
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in the Markdown output"""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth from the starting URL (0 = only the starting page)"""

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum number of pages to crawl. Hard cap: 500."""

    pdf: Pdf
    """PDF parsing controls.

    Use start/end to limit text extraction and OCR to an inclusive 1-based page
    range.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate base64-encoded image data in the Markdown output"""

    stop_after_ms: Annotated[int, PropertyInfo(alias="stopAfterMs")]
    """Soft time budget for the crawl in milliseconds.

    After each scrape, the crawler checks the elapsed time and, if exceeded, returns
    the pages collected so far instead of continuing. Min: 10000 (10s). Max: 240000
    (4 min). Default: 120000 (2 min).
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Regex pattern. Only URLs matching this pattern will be followed and scraped."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """
    Extract only the main content, stripping headers, footers, sidebars, and
    navigation
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load for each
    crawled page. Min: 0. Max: 30000 (30 seconds).
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
    """When true, PDF pages are fetched and parsed.

    When false, PDF pages are skipped entirely (not included in results and not
    counted as failures).
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """
