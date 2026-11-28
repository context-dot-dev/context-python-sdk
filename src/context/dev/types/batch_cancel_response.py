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
    """Credits reserved for the batch."""

    reserved: int
    """Credits reserved for the batch.

    Unused credits are refunded once it reaches `cancelled`.
    """


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


class Progress(BaseModel):
    """How far the batch got before cancellation."""

    failed: int
    """Pages that could not be scraped before cancellation."""

    pending: int
    """Pages not yet attempted, which will be skipped."""

    succeeded: int
    """Pages scraped successfully before cancellation."""


class Timing(BaseModel):
    """When the batch was created and started."""

    created_at: str
    """When the batch was created."""

    started_at: Optional[str] = None
    """When scraping started. `null` if the batch was cancelled before it started."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class BatchCancelResponse(BaseModel):
    id: str
    """Unique ID of the batch."""

    crawl: Optional[CrawlControls] = None
    """Crawl settings as submitted."""

    credits: Credits
    """Credits reserved for the batch."""

    formats: Formats
    """Formats requested for each page, as submitted in `input.data.formats`."""

    input: Intake
    """Page counts from your submission."""

    mode: Literal["scrape", "crawl"]
    """`scrape` for a URL list, `crawl` for a site crawl."""

    page_errors: List[PageErrorCount]
    """Page failures so far, grouped by error code, most common first."""

    progress: Progress
    """How far the batch got before cancellation."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: Literal["cancelling"]
    """Always `cancelling`.

    Pages in progress finish, then the batch becomes `cancelled`.
    """

    tags: List[str]
    """Tags set when the batch was submitted."""

    timing: Timing
    """When the batch was created and started."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
