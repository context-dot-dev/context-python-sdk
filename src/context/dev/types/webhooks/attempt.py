# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Attempt", "Error"]


class Error(BaseModel):
    """Attempt error, or null if none."""

    code: str
    """Error code."""

    message: str
    """Error details."""


class Attempt(BaseModel):
    attempt: int
    """Attempt number, starting at 1."""

    completed_at: Optional[datetime] = None
    """Completion time, or null while in progress."""

    error: Optional[Error] = None
    """Attempt error, or null if none."""

    http_status: Optional[int] = None
    """HTTP response status, or null if no response was received."""

    started_at: datetime
    """Attempt start time."""

    trigger: Literal["initial", "automatic", "manual"]
    """`initial`, `automatic` (scheduled retry), or `manual` (Retry endpoint)."""

    url: str
    """URL used for this attempt."""
