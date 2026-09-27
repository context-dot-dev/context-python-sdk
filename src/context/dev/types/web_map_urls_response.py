# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebMapURLsResponse", "URL", "KeyMetadata"]


class URL(BaseModel):
    url: str

    description: Optional[str] = None

    keywords: Optional[List[str]] = None

    language: Optional[str] = None

    title: Optional[str] = None


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebMapURLsResponse(BaseModel):
    domain: str

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    success: Literal[True]

    urls: List[URL]

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
