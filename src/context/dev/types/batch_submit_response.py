# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .intake import Intake
from .._models import BaseModel
from .crawl_controls import CrawlControls

__all__ = ["BatchSubmitResponse", "CacheMetadata", "Credits", "Formats", "InvalidURL", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Cache status of this response."""

    age_ms: int
    """Age of the cached data, in milliseconds. `0` for `miss` and `zdr`."""

    status: Literal["hit", "miss", "zdr"]
    """
    `hit` when served from cache, `miss` when fetched fresh, `zdr` when zero data
    retention bypassed the cache.
    """


class Credits(BaseModel):
    """Credits reserved for the batch."""

    reserved: int
    """Credits reserved after validation, before scraping starts. `0` while `pending`."""


class Formats(BaseModel):
    """Formats requested for each page, as submitted in `input.data.formats`."""

    bytes: Optional[bool] = None
    """Return the original HTTP response body."""

    highlights: Optional[bool] = None
    """Return Markdown excerpts relevant to `highlightsParams.query`."""

    html: Optional[bool] = None
    """Return the rendered HTML."""

    images: Optional[bool] = None
    """Return the images found on the page."""

    json_: Optional[bool] = FieldInfo(alias="json", default=None)
    """
    Return an object matching `jsonParams.schema`, extracted from the page text and
    embedded data such as JSON-LD, meta tags, and framework state.
    """

    markdown: Optional[bool] = None
    """Return the page content, or a video transcript, as Markdown."""

    parse: Optional[bool] = None
    """Return fields extracted with custom rules or a prebuilt parser, as `parsed`."""

    product: Optional[bool] = None
    """Return product details such as name, price, and availability."""

    screenshot: Optional[bool] = None
    """Return a screenshot of the page."""


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
    """Credits your organization has left after this request."""


class BatchSubmitResponse(BaseModel):
    id: str
    """Unique ID of the batch. Pass it to `GET /batch/{batch_id}` to track progress."""

    cache_metadata: CacheMetadata
    """Cache status of this response."""

    crawl: Optional[CrawlControls] = None
    """Crawl settings as submitted."""

    created_at: str
    """When the batch was created."""

    credits: Credits
    """Credits reserved for the batch."""

    formats: Formats
    """Formats requested for each page, as submitted in `input.data.formats`."""

    input: Intake
    """Page counts from your submission."""

    invalid_urls: List[InvalidURL]
    """URLs rejected from your list, up to the first 100."""

    mode: Literal["scrape", "crawl"]
    """`scrape` for a URL list, `crawl` for a site crawl."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: Literal["pending", "queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Current state.

    `pending` batches are being validated or are waiting for a slot under your
    plan's concurrent batch limit, `queued` batches are ready to start, and
    `running` batches are scraping. `completed`, `cancelled`, and `failed` are
    final.
    """

    tags: List[str]
    """Tags set when the batch was submitted."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    webhook_secret: Optional[str] = None
    """Secret for verifying `X-Context-Signature` on this batch's webhooks.

    Returned only here and only when you set a webhook, so store it.
    """
