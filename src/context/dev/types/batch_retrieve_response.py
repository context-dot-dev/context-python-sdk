# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "BatchRetrieveResponse",
    "Credits",
    "Error",
    "Input",
    "InvalidURL",
    "Progress",
    "Results",
    "ResultsFile",
    "Timing",
    "KeyMetadata",
]


class Credits(BaseModel):
    """Reserved and used credits."""

    charged: int
    """Credits used by successful pages."""

    estimated: int
    """Credits reserved when the batch was accepted."""


class Error(BaseModel):
    """Batch-level error. Null unless `status` is `failed`."""

    code: str
    """Batch error code."""

    message: str
    """Batch error message."""


class Input(BaseModel):
    """Submission counts."""

    accepted: int
    """Pages accepted, or the crawl page limit. Credits are reserved for this count."""

    duplicates: int
    """Duplicate URL and `itemId` pairs skipped. Always 0 for crawls."""

    invalid: int
    """Pages rejected during validation."""

    submitted: int
    """Pages submitted before validation. For a crawl, the page limit."""


class InvalidURL(BaseModel):
    reason: str
    """Why it was rejected."""

    url: str
    """Rejected URL."""


class Progress(BaseModel):
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


class ResultsFile(BaseModel):
    bytes: int
    """Compressed file size in bytes."""

    items: int
    """Results in this file."""

    url: str
    """Temporary URL for a gzipped NDJSON file."""


class Results(BaseModel):
    """Download links available when the batch finishes.

    GET /batch/{batch_id}/results serves the same records as paginated JSON.
    """

    expires_at: str
    """When the download URLs expire."""

    files: List[ResultsFile]
    """Result files. Order is not guaranteed."""


class Timing(BaseModel):
    completed_at: Optional[str] = None
    """When processing finished. Null while active."""

    created_at: str
    """When the batch was created."""

    started_at: Optional[str] = None
    """When processing started. Null while queued."""


class KeyMetadata(BaseModel):
    """API key usage for this request."""

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class BatchRetrieveResponse(BaseModel):
    id: str
    """Batch ID used to retrieve or cancel the job."""

    credits: Credits
    """Reserved and used credits."""

    error: Optional[Error] = None
    """Batch-level error. Null unless `status` is `failed`."""

    errors: List[Error]
    """Page failures grouped by error code."""

    input: Input
    """Submission counts."""

    invalid_urls: List[InvalidURL]
    """Rejected URLs, up to 100. These are not charged."""

    mode: Literal["scrape", "crawl"]
    """How pages are selected."""

    progress: Progress
    """Current processing counts. Use `status` to check completion."""

    results: Optional[Results] = None
    """Download links available when the batch finishes.

    GET /batch/{batch_id}/results serves the same records as paginated JSON.
    """

    status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Current state. `completed`, `cancelled`, and `failed` are final."""

    tags: List[str]
    """Tags stored on the batch at submission."""

    timing: Timing

    type: Literal["markdown", "html"]
    """Output format."""

    key_metadata: Optional[KeyMetadata] = None
    """API key usage for this request."""

    webhook_secret: Optional[str] = None
    """Webhook signing secret. Also returned by GET /batch/{batch_id}."""
