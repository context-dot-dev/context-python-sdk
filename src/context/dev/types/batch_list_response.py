# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .intake import Intake
from .failure import Failure
from .._models import BaseModel
from .crawl_controls import CrawlControls
from .page_error_count import PageErrorCount

__all__ = [
    "BatchListResponse",
    "Data",
    "DataCredits",
    "DataProgress",
    "DataResults",
    "DataResultsFile",
    "DataTiming",
    "KeyMetadata",
]


class DataCredits(BaseModel):
    """What this batch has done to your credit balance."""

    net: int
    """`reserved` minus `refunded` plus `ocr_charged` — what the batch has cost so far.

    Equal to `reserved` until the batch settles.
    """

    ocr_charged: int
    """
    Credits charged for PDF pages recovered by OCR (pdf.ocr=true), 1 per recovered
    page, on top of `reserved`. Stays 0 until the batch settles.
    """

    refunded: int
    """Credits returned for pages that did not succeed.

    Stays 0 until the batch reaches a final status, then settles in one movement.
    """

    reserved: int
    """Credits debited from your balance the moment the batch was accepted.

    This is a charge, not a forecast — the whole amount leaves the balance up front.
    """


class DataProgress(BaseModel):
    """Pages attempted so far. Use `status` to check completion."""

    failed: int
    """Pages that could not be scraped."""

    pending: int
    """Reserved pages not yet attempted.

    A cancelled batch keeps reporting the URLs it never reached; a crawl whose
    `input.reserved_is_ceiling` is true reports 0 once final, because its unspent
    budget was never real pages.
    """

    succeeded: int
    """Pages scraped successfully."""


class DataResultsFile(BaseModel):
    bytes: int
    """Compressed file size in bytes."""

    items: int
    """Results in this file."""

    url: str
    """Temporary URL for a gzipped NDJSON file."""


class DataResults(BaseModel):
    """
    Download links, available once the batch reaches a final status and null before then. GET /batch/{batch_id}/results serves the same records as paginated JSON.
    """

    expires_at: str
    """When the download URLs expire."""

    files: List[DataResultsFile]
    """Result files. Order is not guaranteed."""


class DataTiming(BaseModel):
    completed_at: Optional[str] = None
    """When processing finished. Null while active."""

    created_at: str
    """When the batch was created."""

    started_at: Optional[str] = None
    """When processing started. Null while queued."""


class Data(BaseModel):
    """An asynchronous web scraping job."""

    id: str
    """Batch ID used to retrieve or cancel the job."""

    crawl: Optional[CrawlControls] = None
    """
    The crawl controls as submitted, so the limits requested can be compared against
    what the crawl reached.
    """

    credits: DataCredits
    """What this batch has done to your credit balance."""

    failure: Optional[Failure] = None
    """
    A failure of the batch as a whole, distinct from the per-page failures in
    `page_errors`.
    """

    format: Literal["markdown", "html"]
    """What each page is returned as.

    Matches `input.data.format` on the submit request.
    """

    input: Intake
    """What submission took in, and what it charged for."""

    mode: Literal["scrape", "crawl"]
    """How pages were selected. Matches `input.mode` on the submit request."""

    page_errors: List[PageErrorCount]
    """Individual page failures grouped by error code, sorted by count.

    Unrelated to `failure`, which is the batch itself failing.
    """

    progress: DataProgress
    """Pages attempted so far. Use `status` to check completion."""

    results: Optional[DataResults] = None
    """
    Download links, available once the batch reaches a final status and null before
    then. GET /batch/{batch_id}/results serves the same records as paginated JSON.
    """

    status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Current state. `completed`, `cancelled`, and `failed` are final."""

    tags: List[str]
    """Tags stored on the batch at submission."""

    timing: DataTiming


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class BatchListResponse(BaseModel):
    data: Optional[List[Data]] = None
    """Batches on this page."""

    has_more: Optional[bool] = None
    """Whether another page is available."""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """

    next_cursor: Optional[str] = None
    """Cursor for the next page."""
