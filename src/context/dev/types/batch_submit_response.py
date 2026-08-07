# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .intake import Intake
from .._models import BaseModel
from .crawl_controls import CrawlControls

__all__ = ["BatchSubmitResponse", "Credits", "InvalidURL", "KeyMetadata"]


class Credits(BaseModel):
    """What accepting this batch cost."""

    reserved: int
    """Credits just debited from your balance.

    Whatever the batch does not spend is refunded when it settles.
    """


class InvalidURL(BaseModel):
    reason: str
    """Why it was rejected."""

    url: str
    """Rejected URL."""


class KeyMetadata(BaseModel):
    """API key usage for this request."""

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class BatchSubmitResponse(BaseModel):
    id: str
    """Batch ID. Poll GET /batch/{batch_id} with it."""

    crawl: Optional[CrawlControls] = None
    """
    The crawl controls as submitted, so the limits requested can be compared against
    what the crawl reached.
    """

    created_at: str
    """When the batch was created."""

    credits: Credits
    """What accepting this batch cost."""

    format: Literal["markdown", "html"]
    """What each page will be returned as."""

    input: Intake
    """What submission took in, and what it charged for."""

    invalid_urls: List[InvalidURL]
    """Rejected URLs, up to 100. These are not charged."""

    mode: Literal["scrape", "crawl"]
    """How pages will be selected."""

    status: Literal["queued"]
    """Always `queued`. An accepted batch has not started yet."""

    tags: List[str]
    """Tags stored on the batch."""

    key_metadata: Optional[KeyMetadata] = None
    """API key usage for this request."""

    webhook_secret: Optional[str] = None
    """Signing secret for the completion webhook, returned only here and never again.

    Store it now; it is not repeated by GET /batch/{batch_id}.
    """
