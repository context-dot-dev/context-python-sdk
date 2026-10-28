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
    """Batch credit usage and settlement."""

    net: int
    """`reserved` minus `refunded` plus `ocr_charged`."""

    ocr_charged: int
    """OCR usage charged when the batch settles."""

    refunded: int
    """Credits returned for unsuccessful pages when the batch settles."""

    reserved: int
    """Credits held when the batch was accepted."""


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


class Progress(BaseModel):
    """Pages attempted so far. Use `status` to check completion."""

    failed: int
    """Pages that could not be scraped."""

    pending: int
    """Accepted pages not yet attempted.

    Unused crawl capacity is excluded after completion.
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
    """Result download links; null until the batch finishes.

    Files are deleted 180 days after the batch finishes.
    """

    expires_at: str
    """When these links expire (24 hours after this response)."""

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
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class BatchRetrieveResponse(BaseModel):
    id: str
    """Batch ID."""

    crawl: Optional[CrawlControls] = None
    """Crawl settings as submitted."""

    credits: Credits
    """Batch credit usage and settlement."""

    failure: Optional[Failure] = None
    """
    A failure of the batch as a whole, distinct from the per-page failures in
    `page_errors`.
    """

    formats: Formats
    """Outputs requested for each page. Matches input.data.formats on submission."""

    input: Intake
    """What the submission accepted."""

    invalid_urls: List[InvalidURL]
    """Rejected URLs (first 100)."""

    mode: Literal["scrape", "crawl"]
    """`scrape` (URL list) or `crawl`."""

    page_errors: List[PageErrorCount]
    """Individual page failures grouped by error code, sorted by count.

    Unrelated to `failure`, which is the batch itself failing.
    """

    progress: Progress
    """Pages attempted so far. Use `status` to check completion."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    results: Optional[Results] = None
    """Result download links; null until the batch finishes.

    Files are deleted 180 days after the batch finishes.
    """

    status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"]
    """Current state. `completed`, `cancelled`, and `failed` are final."""

    tags: List[str]
    """Tags stored on the batch at submission."""

    timing: Timing

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    policies: Optional[List[str]] = None
    """Access policy IDs applied to every page."""

    webhook_delivery_id: Optional[str] = None
    """Batch completion delivery ID, when available."""
