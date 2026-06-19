# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebWebScrapeHTMLResponse", "Metadata", "MetadataAlternate", "KeyMetadata"]


class MetadataAlternate(BaseModel):
    href: str
    """Resolved alternate URL."""

    hreflang: Optional[str] = None
    """Language or locale for the alternate URL, when present."""

    title: Optional[str] = None
    """Alternate resource title, when present."""

    type: Optional[str] = None
    """Alternate resource MIME type, when present."""


class Metadata(BaseModel):
    """Metadata extracted from the scraped page HTML."""

    final_url: str = FieldInfo(alias="finalUrl")
    """Final URL scraped after redirects or scraper fallback, when known.

    Falls back to sourceUrl when unavailable.
    """

    source_url: str = FieldInfo(alias="sourceUrl")
    """Original URL requested by the caller."""

    additional_meta: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="additionalMeta", default=None)
    """Additional non-social meta tags not promoted to top-level metadata fields."""

    alternates: Optional[List[MetadataAlternate]] = None
    """Resolved alternate links from link rel=alternate tags."""

    author: Optional[str] = None
    """Author metadata, when present."""

    canonical_url: Optional[str] = FieldInfo(alias="canonicalUrl", default=None)
    """Resolved canonical URL, when present."""

    description: Optional[str] = None
    """Best description extracted from standard, Open Graph, or Twitter metadata."""

    favicon: Optional[str] = None
    """Resolved favicon URL, when present."""

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

    title: Optional[str] = None
    """Best title extracted from the page."""

    twitter: Optional[Dict[str, Union[str, List[str]]]] = None
    """Twitter card metadata with the twitter: prefix removed and keys camel-cased."""


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class WebWebScrapeHTMLResponse(BaseModel):
    html: str
    """The scraped content of the page.

    For normal pages this is the raw HTML. When the page is a sitemap or feed served
    behind an XSL stylesheet (which browsers render into HTML), this is the
    underlying XML instead — see the `type` field.
    """

    metadata: Metadata
    """Metadata extracted from the scraped page HTML."""

    success: Literal[True]
    """Indicates success"""

    type: Literal["html", "xml", "json", "text", "csv", "markdown", "svg", "pdf", "docx", "doc"]
    """Detected content type of the returned `html` field.

    Sitemaps and feeds are surfaced as `xml`; ordinary pages are `html`.
    """

    url: str
    """The URL that was scraped"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
