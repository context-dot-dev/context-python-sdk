# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ScholarSearchResponse", "Data", "Meta", "KeyMetadata"]


class Data(BaseModel):
    id: str
    """Stable paper identifier."""

    full_text_format: Literal["pdf", "html", "jats"]
    """Format of the linked full text. jats is XML."""

    full_text_url: str
    """Direct link to the full text."""

    published_at: Optional[datetime] = None
    """Publication time in ISO 8601, or null when unknown."""

    snippet: str
    """Matching passage, or opening passage for an ID-only query."""

    title: str
    """Paper title."""

    url: str
    """Paper landing page."""


class Meta(BaseModel):
    """Page summary."""

    count: int
    """Papers in this page."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class ScholarSearchResponse(BaseModel):
    data: List[Data]
    """Matching papers in the requested order."""

    has_more: bool
    """Whether another page is available."""

    meta: Meta
    """Page summary."""

    next_cursor: Optional[str] = None
    """Cursor for the next page, or null on the last page."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
