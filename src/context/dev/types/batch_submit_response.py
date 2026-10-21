# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .intake import Intake
from .._models import BaseModel
from .crawl_controls import CrawlControls

__all__ = ["BatchSubmitResponse", "CacheMetadata", "Credits", "Formats", "InvalidURL", "KeyMetadata"]


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


class Formats(BaseModel):
    """Outputs requested for each page. Matches input.data.formats on submission."""

    bytes: Optional[bool] = None
    """The original HTTP response body."""

    highlights: Optional[bool] = None
    """Markdown excerpts relevant to `highlightsParams.query`."""

    html: Optional[bool] = None
    """Rendered HTML."""

    images: Optional[bool] = None
    """Images found on the page."""

    json_: Optional[bool] = FieldInfo(alias="json", default=None)
    """An object matching `jsonParams.schema`, extracted from the page."""

    markdown: Optional[bool] = None
    """Page content as Markdown."""

    parse: Optional[bool] = None
    """Fields extracted with custom rules or a prebuilt parser, returned as `parsed`."""

    product: Optional[bool] = None
    """Product details such as name, price, and availability."""

    screenshot: Optional[bool] = None
    """A screenshot of the page."""


class InvalidURL(BaseModel):
    reason: str
    """Why it was rejected."""

    url: str
    """Rejected URL."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

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

    formats: Formats
    """Outputs requested for each page. Matches input.data.formats on submission."""

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
    """Credits this request used and your remaining balance."""

    webhook_secret: Optional[str] = None
    """Secret for verifying `X-Context-Signature`.

    Only submit returns it, so store it.
    """
