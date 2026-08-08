# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WebWebCrawlMdResponse",
    "Metadata",
    "Result",
    "ResultMetadata",
    "ResultMetadataAlternate",
    "ResultMetadataHeading",
    "KeyMetadata",
]


class Metadata(BaseModel):
    max_crawl_depth: int = FieldInfo(alias="maxCrawlDepth")
    """Maximum crawl depth reached during the crawl"""

    num_failed: int = FieldInfo(alias="numFailed")
    """Number of pages that failed to crawl"""

    num_skipped: int = FieldInfo(alias="numSkipped")
    """
    Number of URLs skipped (PDFs when pdf.shouldParse=false, or URLs not matching
    urlRegex)
    """

    num_succeeded: int = FieldInfo(alias="numSucceeded")
    """Number of pages successfully crawled"""

    num_urls: int = FieldInfo(alias="numUrls")
    """Total number of URLs crawled"""


class ResultMetadataAlternate(BaseModel):
    href: str
    """Resolved alternate URL."""

    hreflang: Optional[str] = None
    """Language or locale for the alternate URL, when present."""

    title: Optional[str] = None
    """Alternate resource title, when present."""

    type: Optional[str] = None
    """Alternate resource MIME type, when present."""


class ResultMetadataHeading(BaseModel):
    level: int
    """Heading level, 1–6 (from h1–h6)."""

    text: str
    """Heading text with whitespace collapsed, truncated to 1000 characters."""


class ResultMetadata(BaseModel):
    crawl_depth: int = FieldInfo(alias="crawlDepth")
    """Depth relative to the start URL. 0 = start URL, 1 = one link away."""

    final_url: str = FieldInfo(alias="finalUrl")
    """Final URL scraped after redirects or scraper fallback, when known.

    Falls back to sourceUrl when unavailable.
    """

    source_url: str = FieldInfo(alias="sourceUrl")
    """Original URL requested by the caller."""

    status_code: int = FieldInfo(alias="statusCode")
    """HTTP status code of the response"""

    success: bool
    """true if the page was fetched and parsed successfully"""

    title: str
    """Best page title extracted from the page (empty string if unavailable)."""

    url: str
    """The crawl URL fetched for this page."""

    additional_meta: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="additionalMeta", default=None)
    """Additional non-social meta tags not promoted to top-level metadata fields."""

    alternates: Optional[List[ResultMetadataAlternate]] = None
    """Resolved alternate links from link rel=alternate tags."""

    author: Optional[str] = None
    """Author metadata, when present."""

    canonical_url: Optional[str] = FieldInfo(alias="canonicalUrl", default=None)
    """Resolved canonical URL, when present."""

    description: Optional[str] = None
    """Best description extracted from standard, Open Graph, or Twitter metadata."""

    favicon: Optional[str] = None
    """Resolved favicon URL, when present."""

    headings: Optional[List[ResultMetadataHeading]] = None
    """Page headings (h1–h6) in document order, extracted from the unfiltered document.

    Capped at the first 500 headings. Omitted when the page has none.
    """

    image: Optional[str] = None
    """Primary resolved preview image from Open Graph, Twitter, or image metadata."""

    json_ld: Optional[List[Dict[str, object]]] = FieldInfo(alias="jsonLd", default=None)
    """JSON-LD structured data blocks parsed from the page."""

    keywords: Optional[List[str]] = None
    """Keywords extracted from the page's keywords meta tag."""

    language: Optional[str] = None
    """Language extracted from html lang or language meta tags."""

    modified_time: Optional[str] = FieldInfo(alias="modifiedTime", default=None)
    """Modified timestamp/date from page metadata, when present."""

    open_graph: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="openGraph", default=None)
    """Open Graph metadata with the og: prefix removed and keys camel-cased."""

    published_time: Optional[str] = FieldInfo(alias="publishedTime", default=None)
    """Published timestamp/date from page metadata, when present."""

    robots: Optional[str] = None
    """Robots meta directive, when present."""

    site_name: Optional[str] = FieldInfo(alias="siteName", default=None)
    """Site or application name from page metadata."""

    twitter: Optional[Dict[str, Union[str, List[str]]]] = None
    """Twitter card metadata with the twitter: prefix removed and keys camel-cased."""


class Result(BaseModel):
    markdown: str
    """Extracted page content as Markdown (empty string on failure)"""

    metadata: ResultMetadata


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class WebWebCrawlMdResponse(BaseModel):
    metadata: Metadata

    results: List[Result]

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
