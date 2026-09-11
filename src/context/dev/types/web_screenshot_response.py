# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebScreenshotResponse", "CacheMetadata", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing to the output was a hit; age_ms is the oldest contributing hit.
    """

    age_ms: int
    """Age of the cached data in milliseconds. Zero for miss and zdr responses."""

    status: Literal["hit", "miss", "zdr"]
    """
    Whether the response was served from cache, required fresh work, or honored
    zero-data-retention cache bypass.
    """


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebScreenshotResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    code: Optional[int] = None
    """HTTP status code"""

    domain: Optional[str] = None
    """The normalized domain that was processed"""

    height: Optional[int] = None
    """Height in pixels of the returned screenshot image"""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    screenshot: Optional[str] = None
    """
    Public image URL for standard requests, or an in-memory data URL when ZDR is
    enabled.
    """

    screenshot_type: Optional[Literal["viewport", "fullPage"]] = FieldInfo(alias="screenshotType", default=None)
    """Type of screenshot that was captured"""

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""

    width: Optional[int] = None
    """Width in pixels of the returned screenshot image"""
