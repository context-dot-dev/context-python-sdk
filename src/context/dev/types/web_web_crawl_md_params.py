# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebWebCrawlMdParams"]


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

    parse_pdf: Annotated[bool, PropertyInfo(alias="parsePDF")]
    """
    When true (default), PDF pages are fetched and their text layer is extracted and
    converted to Markdown alongside HTML pages. When false, PDF pages are skipped
    entirely (not included in results and not counted as failures).
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate base64-encoded image data in the Markdown output"""

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
