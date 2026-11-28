# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LogRetrieveResponse", "Data", "DataInput", "KeyMetadata"]


class DataInput(BaseModel):
    """Input retained from the request."""

    query: Dict[str, object]
    """Query parameters of the request."""

    body: Optional[object] = None
    """Request body with credentials and uploaded content redacted."""


class Data(BaseModel):
    credits_used: int
    """Credits charged for this request."""

    error_code: Optional[str] = None
    """The response's `error_code`. `null` on success."""

    input: DataInput
    """Input retained from the request."""

    key_id: Optional[str] = None
    """ID of the API key that made the request.

    Can be `null` for `MONITOR` and `BATCH` entries.
    """

    latency_ms: float
    """Server-side processing time, in milliseconds."""

    method: str
    """HTTP method, or `MONITOR` for a monitor run and `BATCH` for a batch settlement."""

    path: str
    """Endpoint path that was called."""

    request_id: str
    """ID of the logged request."""

    status_code: int
    """HTTP status code of the response."""

    tags: List[str]
    """Tags sent with the request."""

    timestamp: datetime
    """When the request completed."""

    user_agent: Optional[str] = None
    """The request's `User-Agent` header."""

    zdr: bool
    """Whether the request used zero data retention (ZDR)."""

    response: Optional[object] = None
    """Retained JSON response with credentials redacted.

    `null` when unavailable, such as under ZDR.
    """


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class LogRetrieveResponse(BaseModel):
    data: Data

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
