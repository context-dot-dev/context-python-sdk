# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebWebScrapeSitemapResponse", "Meta", "KeyMetadata"]


class Meta(BaseModel):
    """Metadata about the sitemap crawl operation"""

    errors: int
    """Number of errors encountered during crawling"""

    sitemaps_discovered: int = FieldInfo(alias="sitemapsDiscovered")
    """Total number of sitemap files discovered"""

    sitemaps_fetched: int = FieldInfo(alias="sitemapsFetched")
    """Number of sitemap files successfully fetched and parsed"""

    sitemaps_skipped: int = FieldInfo(alias="sitemapsSkipped")
    """Number of sitemap files skipped (due to errors, timeouts, or limits)"""


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class WebWebScrapeSitemapResponse(BaseModel):
    domain: str
    """The normalized domain that was crawled"""

    meta: Meta
    """Metadata about the sitemap crawl operation"""

    success: Literal[True]
    """Indicates success"""

    urls: List[str]
    """Discovered page URLs from the sitemap, up to `maxLinks`.

    When `search` is set these are only the matching pages, most relevant first.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
