# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebScreenshotResponse", "CacheMetadata", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Cache status of this response."""

    age_ms: int
    """Age of the cached data, in milliseconds. `0` for `miss` and `zdr`."""

    status: Literal["hit", "miss", "zdr"]
    """
    `hit` when served from cache, `miss` when fetched fresh, `zdr` when zero data
    retention bypassed the cache.
    """


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class WebScreenshotResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache status of this response."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    code: Optional[int] = None
    """HTTP status code, repeated in the body."""

    domain: Optional[str] = None
    """Normalized domain that was captured."""

    final_dom_state: Optional[Literal["loaded", "still-loading"]] = FieldInfo(alias="finalDOMState", default=None)
    """
    `loaded`, or `still-loading` when capture ended before the page finished
    loading.
    """

    height: Optional[int] = None
    """Height of the returned image, in pixels."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    screenshot: Optional[str] = None
    """URL of the screenshot image.

    A data URL instead when `zdr` is `enabled` or `headers` are sent.
    """

    screenshot_type: Optional[Literal["viewport", "fullPage"]] = FieldInfo(alias="screenshotType", default=None)
    """Whether the image covers the viewport or the full page."""

    status: Optional[str] = None
    """Always `ok` on success."""

    width: Optional[int] = None
    """Width of the returned image, in pixels."""
