# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebScreenshotResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class WebScreenshotResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    domain: Optional[str] = None
    """The normalized domain that was processed"""

    height: Optional[int] = None
    """Height in pixels of the returned screenshot image"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """

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
