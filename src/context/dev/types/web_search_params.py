# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebSearchParams", "MarkdownOptions", "MarkdownOptionsPdf"]


class WebSearchParams(TypedDict, total=False):
    query: Required[str]
    """Natural-language search query."""

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]
    """Blocklist — drop results from these domains.

    Example: ["pinterest.com", "reddit.com"].
    """

    freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"]
    """Restrict results to content published within this window."""

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Allowlist — only return results from these domains.

    Example: ["arxiv.org", "github.com"].
    """

    markdown_options: Annotated[MarkdownOptions, PropertyInfo(alias="markdownOptions")]
    """Inline Markdown scraping for each result. Set `enabled: true` to activate."""

    query_fanout: Annotated[bool, PropertyInfo(alias="queryFanout")]
    """Expand the query into multiple parallel variants for broader recall."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class MarkdownOptionsPdf(TypedDict, total=False):
    """PDF handling. Use start/end to bound text extraction and OCR to a page range."""

    end: int
    """Last PDF page to parse (1-based, inclusive).

    Defaults to the final page. Must be >= start.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF URLs. When false, PDF results are skipped with WEBSITE_ACCESS_ERROR."""

    start: int
    """First PDF page to parse (1-based, inclusive). Defaults to page 1."""


class MarkdownOptions(TypedDict, total=False):
    """Inline Markdown scraping for each result. Set `enabled: true` to activate."""

    enabled: bool
    """Scrape each result to Markdown. Off by default to keep search cheap and fast."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Render iframe contents into the Markdown."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Emit image references in the Markdown."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep hyperlinks in the Markdown."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Cache TTL in ms for scraped Markdown keyed by URL + options.

    Default 1 day, max 30 days. Set to 0 to force a fresh scrape.
    """

    pdf: MarkdownOptionsPdf
    """PDF handling. Use start/end to bound text extraction and OCR to a page range."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate inline base64 image payloads to keep responses small."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Strip nav, header, footer, and sidebar — keep only the primary article content."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """Extra wait after page load before rendering, in ms (0–30000).

    Useful for JS-heavy pages.
    """
