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
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebMapURLsResponse(BaseModel):
    domain: str

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    success: Literal[True]

    urls: List[URL]

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
