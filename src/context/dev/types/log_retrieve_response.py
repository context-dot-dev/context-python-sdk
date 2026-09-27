# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LogRetrieveResponse", "Data", "DataInput", "KeyMetadata"]


class DataInput(BaseModel):
    """What was sent with the request."""

    query: Dict[str, object]
    """Query parameters as sent."""

    body: Optional[object] = None
    """Request body with credentials and uploaded content redacted."""


class Data(BaseModel):
    credits_used: int
    """Credits charged for this request."""

    error_code: Optional[str] = None
    """The `error_code` from the response, or null on success."""

    input: DataInput
    """What was sent with the request."""

    key_id: Optional[str] = None
    """ID of the API key that made the request."""

    latency_ms: float
    """Server-side processing time in milliseconds."""

    method: str
    """
    HTTP method, or `MONITOR` / `BATCH` for monitor-run and batch-settlement
    entries.
    """

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

    user_agent: Optional[str] = None
    """User-Agent header of the request."""

    zdr: bool
    """Whether the request was made under zero data retention."""

    response: Optional[object] = None
    """The retained JSON response with credentials redacted, or null when unavailable."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class LogRetrieveResponse(BaseModel):
    data: Data

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
