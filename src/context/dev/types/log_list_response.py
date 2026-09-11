# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LogListResponse", "Data", "KeyMetadata"]


class Data(BaseModel):
    credits_used: int
    """Credits charged for this request."""

    error_code: Optional[str] = None
    """The `error_code` from the response, or null on success."""

    key_id: Optional[str] = None
    """ID of the API key that made the request."""

    latency_ms: float
    """Server-side processing time in milliseconds."""

    method: str
    """HTTP method."""

    path: str
    """Endpoint path as called."""

    request_id: str
    """Request ID of the logged API call."""

    status_code: int
    """HTTP status code returned."""

    tags: List[str]
    """Request tags supplied by the caller."""

    timestamp: datetime
    """When the request completed."""

    zdr: bool
    """Whether the request was made under zero data retention."""


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class LogListResponse(BaseModel):
    data: List[Data]
    """Log entries, newest first."""

    has_more: bool
    """Whether a next page exists."""

    limit: int
    """Entries per page."""

    page: int
    """Current page number."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
