# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .intake import Intake
from .._models import BaseModel
from .crawl_controls import CrawlControls
from .page_error_count import PageErrorCount

__all__ = ["BatchCancelResponse", "Credits", "Progress", "Timing", "KeyMetadata"]


class Credits(BaseModel):
    """What this batch cost so far."""

    reserved: int
    """Credits debited at submission.

    The unspent remainder is refunded once the batch settles — read
    `credits.refunded` from GET /batch/{batch_id} then.
    """


class Progress(BaseModel):
    """How far the batch got before cancellation."""

    failed: int
    """Pages that could not be scraped before the request landed."""

    pending: int
    """Reserved pages that will now be skipped, and refunded when the batch settles."""

    succeeded: int
    """Pages scraped successfully before the request landed."""


class Timing(BaseModel):
    """There is no finish time yet — the batch is still winding down."""

    created_at: str
    """When the batch was created."""

    started_at: Optional[str] = None
    """When processing started. Null if it was cancelled while still queued."""


class KeyMetadata(BaseModel):
    """API key usage for this request."""

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class BatchCancelResponse(BaseModel):
    id: str
    """Batch ID."""

    crawl: Optional[CrawlControls] = None
    """
    The crawl controls as submitted, so the limits requested can be compared against
    what the crawl reached.
    """

    credits: Credits
    """What this batch cost so far."""

    format: Literal["markdown", "html"]
    """What each page is returned as."""

    input: Intake
    """What submission took in, and what it charged for."""

    mode: Literal["scrape", "crawl"]
    """How pages were selected."""

    page_errors: List[PageErrorCount]
    """Page failures so far, grouped by error code and sorted by count."""

    progress: Progress
    """How far the batch got before cancellation."""

    status: Literal["cancelling"]
    """Always `cancelling`.

    Work already in flight finishes; the batch reaches `cancelled` shortly after.
    """

    tags: List[str]
    """Tags stored on the batch at submission."""

    timing: Timing
    """There is no finish time yet — the batch is still winding down."""

    key_metadata: Optional[KeyMetadata] = None
    """API key usage for this request."""
