# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "BatchGetResultsResponse",
    "Data",
    "DataOk",
    "DataOkCacheMetadata",
    "DataOkMetadata",
    "DataOkMetadataAlternate",
    "DataOkMetadataHeading",
    "DataError",
    "KeyMetadata",
]


class DataOkCacheMetadata(BaseModel):
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


class DataOkMetadataAlternate(BaseModel):
    href: str
    """Resolved alternate URL."""

    hreflang: Optional[str] = None
    """Language or locale for the alternate URL, when present."""

    title: Optional[str] = None
    """Alternate resource title, when present."""

    type: Optional[str] = None
    """Alternate resource MIME type, when present."""


class DataOkMetadataHeading(BaseModel):
    level: int
    """Heading level, 1–6 (from h1–h6)."""

    text: str
    """Heading text with whitespace collapsed, truncated to 1000 characters."""


class DataOkMetadata(BaseModel):
    """Metadata extracted from the scraped page HTML."""

    final_url: str = FieldInfo(alias="finalUrl")
    """Final URL scraped after redirects or scraper fallback, when known.

    Falls back to sourceUrl when unavailable.
    """

    source_url: str = FieldInfo(alias="sourceUrl")
    """Original URL requested by the caller."""

    additional_meta: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="additionalMeta", default=None)
    """Additional non-social meta tags not promoted to top-level metadata fields."""

    alternates: Optional[List[DataOkMetadataAlternate]] = None
    """Resolved alternate links from link rel=alternate tags."""

    author: Optional[str] = None
    """Author metadata, when present."""

    canonical_url: Optional[str] = FieldInfo(alias="canonicalUrl", default=None)
    """Resolved canonical URL, when present."""

    description: Optional[str] = None
    """Best description extracted from standard, Open Graph, or Twitter metadata."""

    favicon: Optional[str] = None
    """Resolved favicon URL, when present."""

    headings: Optional[List[DataOkMetadataHeading]] = None
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


class DataOk(BaseModel):
    """A page the batch fetched successfully."""

    cache_metadata: DataOkCacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    final_url: str
    """URL the content was read from, after redirects."""

    http_status: Optional[int] = None
    """HTTP status of the final response, when known."""

    metadata: DataOkMetadata
    """Metadata extracted from the scraped page HTML."""

    status: Literal["ok"]
    """The page was scraped."""

    url: str
    """URL as submitted, or as discovered by the crawl."""

    html: Optional[str] = None
    """Page HTML.

    Present on html batches, and on markdown batches submitted with
    `options.includeHTML`.
    """

    item_id: Optional[str] = FieldInfo(alias="itemId", default=None)
    """Caller-supplied identifier echoed from submission."""

    markdown: Optional[str] = None
    """Page content as Markdown. Present on markdown batches."""

    meta: Optional[Dict[str, object]] = None
    """Caller-supplied metadata echoed from submission."""

    ocr_pages: Optional[int] = None
    """PDF pages of this document recovered by OCR (pdf.ocr=true).

    Each recovered page bills 1 credit on top of the page base credit; absent when
    no OCR ran.
    """


class DataError(BaseModel):
    """A page the batch could not fetch."""

    error_code: str
    """Why the page failed."""

    message: str
    """Human-readable failure detail."""

    status: Literal["error"]
    """The page could not be scraped."""

    url: str
    """URL as submitted, or as discovered by the crawl."""

    item_id: Optional[str] = FieldInfo(alias="itemId", default=None)
    """Caller-supplied identifier echoed from submission."""

    meta: Optional[Dict[str, object]] = None
    """Caller-supplied metadata echoed from submission."""


Data: TypeAlias = Annotated[Union[DataOk, DataError], PropertyInfo(discriminator="status")]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class BatchGetResultsResponse(BaseModel):
    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    data: Optional[List[Data]] = None
    """Result records on this page."""

    has_more: Optional[bool] = None
    """Whether another page is available."""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    next_cursor: Optional[str] = None
    """Cursor for the next page."""
