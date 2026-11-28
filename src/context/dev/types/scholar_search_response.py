# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ScholarSearchResponse", "Data", "Meta", "KeyMetadata"]


class Data(BaseModel):
    id: str
    """Unique ID of the paper."""

    full_text_format: Literal["pdf", "html", "jats"]
    """Format of the full text at `full_text_url`. `jats` is JATS XML."""

    full_text_url: str
    """Direct URL of the full text."""

    published_at: Optional[datetime] = None
    """When the paper was published. `null` when unknown."""

    snippet: str
    """
    Passage that matches the query, or the opening passage when the query is only a
    paper ID.
    """

    title: str
    """Title of the paper."""

    url: str
    """URL of the paper's landing page."""


class Meta(BaseModel):
    """Summary of this page."""

    count: int
    """Number of papers on this page."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class ScholarSearchResponse(BaseModel):
    data: List[Data]
    """Papers on this page, in the requested order."""

    has_more: bool
    """Whether more results are available after this page."""

    meta: Meta
    """Summary of this page."""

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page. `null` on the last page."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
