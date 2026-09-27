# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebScreenshotResponse", "CacheMetadata", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Whether this response came from cache."""

    age_ms: int
    """Age of the cached data in milliseconds. Zero for miss and zdr responses."""

    status: Literal["hit", "miss", "zdr"]
    """
    Whether the response was served from cache, required fresh work, or honored
    zero-data-retention cache bypass.
    """


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebScreenshotResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Whether this response came from cache."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    code: Optional[int] = None
    """HTTP status code"""

    domain: Optional[str] = None
    """The normalized domain that was processed"""

    final_dom_state: Optional[Literal["loaded", "still-loading"]] = FieldInfo(alias="finalDOMState", default=None)
    """
    `loaded`, or `still-loading` when capture ended before the page finished
    loading.
    """

    height: Optional[int] = None
    """Height in pixels of the returned screenshot image"""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    screenshot: Optional[str] = None
    """
    Public image URL for standard requests, or an in-memory data URL when ZDR or
    non-empty custom headers are supplied.
    """

    screenshot_type: Optional[Literal["viewport", "fullPage"]] = FieldInfo(alias="screenshotType", default=None)
    """Type of screenshot that was captured"""

    status: Optional[str] = None
    """Always `ok` on success."""

    width: Optional[int] = None
    """Width in pixels of the returned screenshot image"""
