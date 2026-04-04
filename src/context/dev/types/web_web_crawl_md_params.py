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

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in the Markdown output"""

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth from the starting URL (0 = only the starting page)"""

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum number of pages to crawl. Hard cap: 500."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate base64-encoded image data in the Markdown output"""

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Regex pattern. Only URLs matching this pattern will be followed and scraped."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """
    Extract only the main content, stripping headers, footers, sidebars, and
    navigation
    """
