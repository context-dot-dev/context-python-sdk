# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebWebCrawlMdResponse", "Metadata", "Result", "ResultMetadata", "KeyMetadata"]


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


class ResultMetadata(BaseModel):
    crawl_depth: int = FieldInfo(alias="crawlDepth")
    """Depth relative to the start URL. 0 = start URL, 1 = one link away."""

    status_code: int = FieldInfo(alias="statusCode")
    """HTTP status code of the response"""

    success: bool
    """true if the page was fetched and parsed successfully"""

    title: str
    """The page's <title> content (empty string if unavailable)"""

    url: str
    """The URL that was fetched"""


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
