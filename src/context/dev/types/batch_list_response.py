# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .error import Error
from .._models import BaseModel
from .error_count import ErrorCount

__all__ = [
    "BatchListResponse",
    "Data",
    "DataCredits",
    "DataInput",
    "DataProgress",
    "DataResults",
    "DataResultsFile",
    "DataTiming",
    "KeyMetadata",
]


class DataCredits(BaseModel):
    """Reserved and used credits."""

    charged: int
    """Credits used by successful pages."""

    estimated: int
    """Credits reserved when the batch was accepted."""


class DataInput(BaseModel):
    """Submission counts."""

    accepted: int
    """Pages accepted, or the crawl page limit. Credits are reserved for this count."""

    duplicates: int
    """Duplicate URL and `itemId` pairs skipped. Always 0 for crawls."""

    invalid: int
    """Pages rejected during validation."""

    submitted: int
    """Pages submitted before validation. For a crawl, the page limit."""


class DataProgress(BaseModel):
    """Current processing counts. Use `status` to check completion."""

    failed: int
    """Pages that could not be scraped."""

    pending: int
    """Accepted pages not yet attempted.

    Always 0 once the batch completes; a crawl can finish under its page limit when
    the site has no more reachable pages.
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
    """Download links available when the batch finishes.

    GET /batch/{batch_id}/results serves the same records as paginated JSON.
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

    credits: DataCredits
    """Reserved and used credits."""

    error: Optional[Error] = None
    """Why the batch failed."""

    errors: List[ErrorCount]
    """Page failures grouped by error code."""

    input: DataInput
    """Submission counts."""

    mode: Literal["scrape", "crawl"]
    """How pages are selected."""

    progress: DataProgress
    """Current processing counts. Use `status` to check completion."""

    results: Optional[DataResults] = None
    """Download links available when the batch finishes.

    GET /batch/{batch_id}/results serves the same records as paginated JSON.
    """

    status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Current state. `completed`, `cancelled`, and `failed` are final."""

    tags: List[str]
    """Tags stored on the batch at submission."""

    timing: DataTiming

    type: Literal["markdown", "html"]
    """Output format."""


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
