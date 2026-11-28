# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WebWebCrawlMdResponse",
    "CacheMetadata",
    "Metadata",
    "Result",
    "ResultMetadata",
    "ResultMetadataAlternate",
    "ResultMetadataHeading",
    "KeyMetadata",
]


class CacheMetadata(BaseModel):
    """Cache status of this response."""

    age_ms: int
    """Age of the cached data, in milliseconds. `0` for `miss` and `zdr`."""

    status: Literal["hit", "miss", "zdr"]
    """
    `hit` when served from cache, `miss` when fetched fresh, `zdr` when zero data
    retention bypassed the cache.
    """


class Metadata(BaseModel):
    max_crawl_depth: int = FieldInfo(alias="maxCrawlDepth")
    """Deepest link depth reached."""

    num_failed: int = FieldInfo(alias="numFailed")
    """Number of pages that failed."""

    num_skipped: int = FieldInfo(alias="numSkipped")
    """
    Number of URLs skipped: PDFs when `pdf.shouldParse` is `false`, URLs that do not
    match `urlRegex`, and URLs that match `excludeUrlRegex`.
    """

    num_succeeded: int = FieldInfo(alias="numSucceeded")
    """Number of pages crawled successfully."""

    num_urls: int = FieldInfo(alias="numUrls")
    """Number of URLs crawled."""


class ResultMetadataAlternate(BaseModel):
    href: str
    """Absolute URL of the alternate version."""

    hreflang: Optional[str] = None
    """Language or locale of the alternate version, when present."""

    title: Optional[str] = None
    """Title of the alternate version, when present."""

    type: Optional[str] = None
    """MIME type of the alternate version, when present."""


class ResultMetadataHeading(BaseModel):
    level: int
    """Heading level, from 1 (`h1`) to 6 (`h6`)."""

    text: str
    """Heading text with whitespace collapsed, truncated to 1000 characters."""


class ResultMetadata(BaseModel):
    crawl_depth: int = FieldInfo(alias="crawlDepth")
    """Link depth from the start URL. `0` is the start URL, `1` is one link away."""

    final_url: str = FieldInfo(alias="finalUrl")
    """URL that was scraped, after redirects. Same as `sourceUrl` when unknown."""

    source_url: str = FieldInfo(alias="sourceUrl")
    """URL that was requested, before redirects."""

    status_code: int = FieldInfo(alias="statusCode")
    """HTTP status code of the page. `0` when the page could not be retrieved."""

    success: bool
    """Whether the page was fetched and parsed."""

    title: str
    """Page title. Empty string when unavailable."""

    url: str
    """URL fetched for this page."""

    additional_meta: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="additionalMeta", default=None)
    """Other non-social meta tags that don't have their own field."""

    alternates: Optional[List[ResultMetadataAlternate]] = None
    """Alternate links from `link rel="alternate"` tags, as absolute URLs."""

    author: Optional[str] = None
    """Author, when present."""

    canonical_url: Optional[str] = FieldInfo(alias="canonicalUrl", default=None)
    """Absolute canonical URL, when present."""

    description: Optional[str] = None
    """Best available description, from standard, Open Graph, or Twitter meta tags."""

    error_code: Optional[str] = None
    """Why the page failed.

    Present only when `success` is `false`: `WEBSITE_BLOCKED` (the site served an
    anti-bot challenge or access wall), `WEBSITE_ACCESS_ERROR` (the page could not
    be retrieved or had no usable content), `NOT_FOUND`, `UNSUPPORTED_CONTENT`,
    `NO_PUBLISHED_MARKDOWN`, or `INTERNAL_ERROR`.
    """

    favicon: Optional[str] = None
    """Absolute favicon URL, when present."""

    headings: Optional[List[ResultMetadataHeading]] = None
    """
    Headings (`h1` to `h6`) in document order, from the full page before any
    filtering. Up to 500. Omitted when the page has none.
    """

    image: Optional[str] = None
    """Main preview image URL, from Open Graph, Twitter, or image meta tags."""

    json_ld: Optional[List[Dict[str, object]]] = FieldInfo(alias="jsonLd", default=None)
    """JSON-LD structured data blocks parsed from the page."""

    keywords: Optional[List[str]] = None
    """Keywords from the page's `keywords` meta tag."""

    language: Optional[str] = None
    """Page language, from the `html` `lang` attribute or language meta tags."""

    modified_time: Optional[str] = FieldInfo(alias="modifiedTime", default=None)
    """Last-modified date or timestamp from page metadata, when present."""

    open_graph: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="openGraph", default=None)
    """Open Graph tags, with the `og:` prefix removed and keys in camelCase."""

    published_time: Optional[str] = FieldInfo(alias="publishedTime", default=None)
    """Publish date or timestamp from page metadata, when present."""

    robots: Optional[str] = None
    """`robots` meta directive, when present."""

    site_name: Optional[str] = FieldInfo(alias="siteName", default=None)
    """Site or app name from page metadata."""

    twitter: Optional[Dict[str, Union[str, List[str]]]] = None
    """Twitter card tags, with the `twitter:` prefix removed and keys in camelCase."""


class Result(BaseModel):
    markdown: str
    """Page content as Markdown. Empty string when the page failed."""

    metadata: ResultMetadata


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class WebWebCrawlMdResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache status of this response."""

    metadata: Metadata

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
