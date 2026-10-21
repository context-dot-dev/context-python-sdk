# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .intake import Intake
from .._models import BaseModel
from .crawl_controls import CrawlControls
from .page_error_count import PageErrorCount

__all__ = ["BatchCancelResponse", "Credits", "Formats", "Progress", "Timing", "KeyMetadata"]


class Credits(BaseModel):
    """What this batch cost so far."""

    reserved: int
    """Credits held at submission; unused credits are refunded when the batch settles."""


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


class Progress(BaseModel):
    """How far the batch got before cancellation."""

    failed: int
    """Pages that could not be scraped before the request landed."""

    pending: int
    """Pages that will be skipped."""

    succeeded: int
    """Pages scraped successfully before the request landed."""


class Timing(BaseModel):
    """Batch timestamps."""

    created_at: str
    """When the batch was created."""

    started_at: Optional[str] = None
    """When processing started. Null if it was cancelled while still queued."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class BatchCancelResponse(BaseModel):
    id: str
    """Batch ID."""

    crawl: Optional[CrawlControls] = None
    """Crawl settings as submitted."""

    credits: Credits
    """What this batch cost so far."""

    formats: Formats
    """Outputs requested for each page. Matches input.data.formats on submission."""

    input: Intake
    """What the submission accepted."""

    mode: Literal["scrape", "crawl"]
    """How pages were selected."""

    page_errors: List[PageErrorCount]
    """Page failures so far, grouped by error code and sorted by count."""

    progress: Progress
    """How far the batch got before cancellation."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: Literal["cancelling"]
    """Always `cancelling`.

    Work already in flight finishes; the batch reaches `cancelled` shortly after.
    """

    tags: List[str]
    """Tags stored on the batch at submission."""

    timing: Timing
    """Batch timestamps."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
