# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebWebScrapeBytesResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebWebScrapeBytesResponse(BaseModel):
    bytes: str
    """Base64-encoded resource bytes, without a data URI prefix.

    Decode this field to recover the downloaded file.
    """

    content_length: int = FieldInfo(alias="contentLength")
    """Number of decoded resource bytes, before base64 encoding."""

    content_type: str = FieldInfo(alias="contentType")
    """The Content-Type returned by the origin, including any charset.

    Defaults to application/octet-stream when absent.
    """

    encoding: Literal["base64"]

    final_url: str = FieldInfo(alias="finalUrl")
    """The resource URL after redirects."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    status_code: int = FieldInfo(alias="statusCode")
    """HTTP status returned by the origin."""

    success: Literal[True]

    url: str
    """The requested resource URL."""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
