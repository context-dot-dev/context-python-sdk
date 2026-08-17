# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NewsSearchResponse", "Data", "DataMatch", "DataSource", "Meta", "KeyMetadata"]


class DataMatch(BaseModel):
    confidence: Optional[float] = None

    level: Literal["primary", "secondary"]


class DataSource(BaseModel):
    direct: bool
    """True when Context observed this article in the publisher-owned feed."""

    domain: str

    name: str


class Data(BaseModel):
    id: str

    authors: List[str]

    description: Optional[str] = None

    image_url: Optional[str] = None

    language: Optional[str] = None

    match: DataMatch

    published_at: Optional[datetime] = None

    source: DataSource

    story_id: str
    """Groups matching normalized headlines published on the same UTC day."""

    title: str

    type: Literal["editorial", "press_release", "regulatory_filing", "advisory"]

    url: str


class Meta(BaseModel):
    count: int


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class NewsSearchResponse(BaseModel):
    data: List[Data]

    has_more: bool

    meta: Meta

    next_cursor: Optional[str] = None

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
