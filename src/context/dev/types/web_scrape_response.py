# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WebScrapeResponse",
    "Bytes",
    "BytesData",
    "CacheMetadata",
    "HTML",
    "Images",
    "ImagesData",
    "Markdown",
    "Metadata",
    "MetadataAlternate",
    "MetadataHeading",
    "Parsed",
    "Screenshot",
    "KeyMetadata",
]


class BytesData(BaseModel):
    base64: str
    """Original response body as base64, after HTTP decompression.

    Maximum decoded size: 20 MiB.
    """

    content_type: str = FieldInfo(alias="contentType")


class Bytes(BaseModel):
    """Original HTTP response body.

    Waiting, actions, and content filters never change it.
    """

    data: Optional[BytesData] = None

    requested: bool


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


class HTML(BaseModel):
    """Rendered HTML after content filters."""

    data: Optional[str] = None

    requested: bool


class ImagesData(BaseModel):
    alt: Optional[str] = None
    """Alt text, if present."""

    url: str
    """Image URL, or a data URI for inline images."""

    classification: Optional[
        Literal["photography", "illustration", "logo", "wordmark", "icon", "pattern", "graphic", "other"]
    ] = None

    file_url: Optional[str] = FieldInfo(alias="fileUrl", default=None)
    """Hosted copy when file enrichment is requested and zdr is disabled.

    Valid for 24 hours from the original capture.
    """

    height: Optional[int] = None

    width: Optional[int] = None


class Images(BaseModel):
    """Images after content filters. Empty when none are found."""

    data: Optional[List[ImagesData]] = None

    requested: bool


class Markdown(BaseModel):
    """Markdown after content filters."""

    data: Optional[str] = None

    requested: bool


class MetadataAlternate(BaseModel):
    href: str
    """Resolved alternate URL."""

    hreflang: Optional[str] = None
    """Language or locale for the alternate URL, when present."""

    title: Optional[str] = None
    """Alternate resource title, when present."""

    type: Optional[str] = None
    """Alternate resource MIME type, when present."""


class MetadataHeading(BaseModel):
    level: int
    """Heading level, 1–6 (from h1–h6)."""

    text: str
    """Heading text with whitespace collapsed, truncated to 1000 characters."""


class Metadata(BaseModel):
    """Page details, when available."""

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

    headings: Optional[List[MetadataHeading]] = None
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

    title: Optional[str] = None
    """Best title extracted from the page."""

    twitter: Optional[Dict[str, Union[str, List[str]]]] = None
    """Twitter card metadata with the twitter: prefix removed and keys camel-cased."""


class Parsed(BaseModel):
    """Fields produced by parseParams.rules, after shared content filters."""

    data: Optional[Dict[str, object]] = None

    requested: bool


class Screenshot(BaseModel):
    """An image data URL. Use directly as an image src."""

    data: Optional[str] = None

    requested: bool


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebScrapeResponse(BaseModel):
    bytes: Bytes
    """Original HTTP response body.

    Waiting, actions, and content filters never change it.
    """

    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    html: HTML
    """Rendered HTML after content filters."""

    images: Images
    """Images after content filters. Empty when none are found."""

    markdown: Markdown
    """Markdown after content filters."""

    metadata: Metadata
    """Page details, when available."""

    parsed: Parsed
    """Fields produced by parseParams.rules, after shared content filters."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    screenshot: Screenshot
    """An image data URL. Use directly as an image src."""

    url: str
    """Final URL after redirects and browser actions."""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
