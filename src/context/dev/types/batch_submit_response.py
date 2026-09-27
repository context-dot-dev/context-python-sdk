# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .intake import Intake
from .._models import BaseModel
from .crawl_controls import CrawlControls

__all__ = ["BatchSubmitResponse", "CacheMetadata", "Credits", "InvalidURL", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Whether this response came from cache."""

    age_ms: int
    """Age of the cached data in milliseconds. Zero for miss and zdr responses."""

    status: Literal["hit", "miss", "zdr"]
    """
    Whether the response was served from cache, required fresh work, or honored
    zero-data-retention cache bypass.
    """


class Credits(BaseModel):
    """What accepting this batch cost."""

    reserved: int
    """Credits held at submission."""


class InvalidURL(BaseModel):
    reason: str
    """Why it was rejected."""

    url: str
    """Rejected URL."""


class KeyMetadata(BaseModel):
    """API key usage for this request."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class BatchSubmitResponse(BaseModel):
    id: str
    """Batch ID. Poll GET /batch/{batch_id} with it."""

    cache_metadata: CacheMetadata
    """Whether this response came from cache."""

    crawl: Optional[CrawlControls] = None
    """Crawl settings as submitted."""

    created_at: str
    """When the batch was created."""

    credits: Credits
    """What accepting this batch cost."""

    format: Literal["markdown", "html"]
    """What each page will be returned as."""

    input: Intake
    """What the submission accepted."""

    invalid_urls: List[InvalidURL]
    """Rejected URLs (first 100)."""

    mode: Literal["scrape", "crawl"]
    """How pages will be selected."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: Literal["queued"]
    """Always `queued`. An accepted batch has not started yet."""

    tags: List[str]
    """Tags stored on the batch."""

    key_metadata: Optional[KeyMetadata] = None
    """API key usage for this request."""

    webhook_secret: Optional[str] = None
    """Secret for verifying `X-Context-Signature`.

    Only submit returns it, so store it.
    """
