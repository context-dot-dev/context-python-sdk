# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .intake import Intake
from .failure import Failure
from .._models import BaseModel
from .crawl_controls import CrawlControls
from .page_error_count import PageErrorCount

__all__ = [
    "BatchRetrieveResponse",
    "Credits",
    "Formats",
    "InvalidURL",
    "Progress",
    "Results",
    "ResultsFile",
    "Timing",
    "KeyMetadata",
]


class Credits(BaseModel):
    """Credits reserved, refunded, and charged for the batch."""

    net: int
    """`reserved` minus `refunded` plus `ocr_charged`."""

    ocr_charged: int
    """Credits charged for OCR when the batch finishes."""

    refunded: int
    """
    Credits returned when the batch finishes, such as for failed or unattempted
    pages.
    """

    reserved: int
    """Credits reserved before scraping starts. `0` while `pending`."""


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


class Progress(BaseModel):
    """Page counts so far. Check `status` to know when the batch is done."""

    failed: int
    """Pages that could not be scraped."""

    pending: int
    """Accepted pages not yet attempted.

    A link-following crawl reports `0` once it finishes, since its unused page
    budget is not counted.
    """

    succeeded: int
    """Pages scraped successfully."""


class ResultsFile(BaseModel):
    bytes: int
    """Compressed file size in bytes."""

    items: int
    """Number of result records in this file."""

    url: str
    """Temporary download URL for a gzipped NDJSON file of result records."""


class Results(BaseModel):
    """Links to download the results.

    `null` until the batch finishes; the files are deleted 180 days after that.
    """

    expires_at: str
    """When these links expire, 24 hours after this response.

    Retrieve the batch again for fresh links.
    """

    files: List[ResultsFile]
    """Result files, in no particular order."""


class Timing(BaseModel):
    """When the batch was created, started, and finished."""

    completed_at: Optional[str] = None
    """When the batch reached a final status. `null` until then."""

    created_at: str
    """When the batch was created."""

    started_at: Optional[str] = None
    """When scraping started. `null` until the batch is `running`."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class BatchRetrieveResponse(BaseModel):
    id: str
    """Unique ID of the batch."""

    crawl: Optional[CrawlControls] = None
    """Crawl settings as submitted."""

    credits: Credits
    """Credits reserved, refunded, and charged for the batch."""

    failure: Optional[Failure] = None
    """Why the batch as a whole failed.

    Individual page failures are counted in `page_errors`.
    """

    formats: Formats
    """Formats requested for each page, as submitted in `input.data.formats`."""

    input: Intake
    """Page counts from your submission."""

    invalid_urls: List[InvalidURL]
    """URLs rejected from your list, up to the first 100."""

    mode: Literal["scrape", "crawl"]
    """`scrape` for a URL list, `crawl` for a site crawl."""

    page_errors: List[PageErrorCount]
    """Page failures grouped by error code, most common first.

    For the batch itself failing, see `failure`.
    """

    progress: Progress
    """Page counts so far. Check `status` to know when the batch is done."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    results: Optional[Results] = None
    """Links to download the results.

    `null` until the batch finishes; the files are deleted 180 days after that.
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

    timing: Timing
    """When the batch was created, started, and finished."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    policies: Optional[List[str]] = None
    """Access policy IDs applied to every page."""

    webhook_delivery_id: Optional[str] = None
    """
    ID of the batch's final-status webhook delivery, for
    `GET /webhooks/deliveries/{delivery_id}`. Omitted until a delivery exists.
    """
