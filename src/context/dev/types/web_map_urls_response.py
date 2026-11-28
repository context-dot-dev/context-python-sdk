# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebMapURLsResponse", "URL", "KeyMetadata"]


class URL(BaseModel):
    url: str
    """Page URL."""

    description: Optional[str] = None
    """Page description, when available."""

    keywords: Optional[List[str]] = None
    """Keywords from the page's `keywords` meta tag."""

    language: Optional[str] = None
    """Page language, when available."""

    title: Optional[str] = None
    """Page title, when available."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class WebMapURLsResponse(BaseModel):
    domain: str
    """Normalized domain that was mapped."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    success: Literal[True]
    """Always `true` on success."""

    urls: List[URL]
    """URLs found on the domain, with page metadata when available."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """
    `true` when the deadline passed with `timeoutOpts.behavior` set to
    `return-partial`. Only results finished in time are included.
    """
