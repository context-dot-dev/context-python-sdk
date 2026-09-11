# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WebWebScrapeMdResponse",
    "CacheMetadata",
    "Metadata",
    "MetadataAlternate",
    "MetadataHeading",
    "ActionsApplied",
    "KeyMetadata",
]


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


class ActionsApplied(BaseModel):
    instruction: str

    status: Literal["applied", "failed", "skipped"]
    """Applied means the requested page state was visibly verified.

    Failed means it was not verified. Skipped means it was not attempted.
    """

    completion_evidence: Optional[str] = FieldInfo(alias="completionEvidence", default=None)
    """Visible page evidence used to verify an applied action."""

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    error: Optional[str] = None

    method: Optional[str] = None

    target_description: Optional[str] = FieldInfo(alias="targetDescription", default=None)


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebWebScrapeMdResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    content_length: int = FieldInfo(alias="contentLength")
    """UTF-8 byte length of the returned Markdown.

    Use 0 to identify an empty result and compare small values against your
    workload's minimum useful-content threshold.
    """

    markdown: str
    """Page content converted to GitHub Flavored Markdown"""

    metadata: Metadata
    """Metadata extracted from the scraped page HTML."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    success: Literal[True]
    """Indicates success"""

    url: str
    """The URL that was scraped"""

    actions_applied: Optional[List[ActionsApplied]] = FieldInfo(alias="actionsApplied", default=None)
    """One verified outcome per requested browser action, in request order."""

    actions_html_stale: Optional[bool] = FieldInfo(alias="actionsHtmlStale", default=None)
    """
    True when an action was applied but the returned content could not be refreshed
    afterward.
    """

    html: Optional[str] = None
    """
    Only present when includeHTML=true: the page HTML the Markdown was converted
    from — the same body the Scrape HTML endpoint returns for the equivalent
    request.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
