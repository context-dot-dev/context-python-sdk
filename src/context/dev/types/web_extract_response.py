# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebExtractResponse", "CacheMetadata", "Metadata", "MetadataActionsApplied", "KeyMetadata"]


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


class MetadataActionsApplied(BaseModel):
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


class Metadata(BaseModel):
    max_crawl_depth: int = FieldInfo(alias="maxCrawlDepth")

    num_blocked: int = FieldInfo(alias="numBlocked")
    """
    Number of crawled pages excluded because they were anti-bot challenges, error
    pages, or parked-domain placeholders.
    """

    num_failed: int = FieldInfo(alias="numFailed")

    num_skipped: int = FieldInfo(alias="numSkipped")

    num_succeeded: int = FieldInfo(alias="numSucceeded")

    num_urls: int = FieldInfo(alias="numUrls")

    actions_applied: Optional[List[MetadataActionsApplied]] = FieldInfo(alias="actionsApplied", default=None)
    """One verified outcome per requested browser action, in request order."""


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebExtractResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    data: Dict[str, object]
    """Extracted data matching the request schema"""

    metadata: Metadata

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    status: str
    """Status of the response, e.g., 'ok'"""

    url: str
    """The starting URL that was analyzed"""

    urls_analyzed: List[str]
    """List of URLs whose Markdown was used for extraction"""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
    """
    True when the timeout ended processing and this response contains only usable
    results completed so far. Unfinished results are omitted.
    """
