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
    """Batch credit usage and settlement."""

    net: int
    """`reserved` minus `refunded` plus `ocr_charged`."""

    ocr_charged: int
    """OCR usage charged when the batch settles."""

    refunded: int
    """Credits returned for unsuccessful pages when the batch settles."""

    reserved: int
    """Credits held when the batch was accepted."""


class DataProgress(BaseModel):
    """Pages attempted so far. Use `status` to check completion."""

    failed: int
    """Pages that could not be scraped."""

    pending: int
    """Accepted pages not yet attempted.

    Unused crawl capacity is excluded after completion.
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
    """Result download links; null until the batch finishes.

    Files are deleted 180 days after the batch finishes.
    """

    expires_at: str
    """When these links expire (24 hours after this response)."""

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
    """Batch ID."""

    crawl: Optional[CrawlControls] = None
    """Crawl settings as submitted."""

    credits: DataCredits
    """Batch credit usage and settlement."""

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
    """What the submission accepted."""

    mode: Literal["scrape", "crawl"]
    """`scrape` (URL list) or `crawl`."""

    page_errors: List[PageErrorCount]
    """Individual page failures grouped by error code, sorted by count.

    Unrelated to `failure`, which is the batch itself failing.
    """

    progress: DataProgress
    """Pages attempted so far. Use `status` to check completion."""

    results: Optional[DataResults] = None
    """Result download links; null until the batch finishes.

    Files are deleted 180 days after the batch finishes.
    """

    status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Current state. `completed`, `cancelled`, and `failed` are final."""

    tags: List[str]
    """Tags stored on the batch at submission."""

    timing: DataTiming


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class BatchListResponse(BaseModel):
    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    data: Optional[List[Data]] = None
    """Batches on this page."""

    has_more: Optional[bool] = None
    """Whether another page is available."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    next_cursor: Optional[str] = None
    """Cursor for the next page."""
