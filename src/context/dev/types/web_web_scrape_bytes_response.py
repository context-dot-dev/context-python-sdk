# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebWebScrapeBytesResponse", "CacheMetadata", "KeyMetadata"]


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


class WebWebScrapeBytesResponse(BaseModel):
    bytes: str
    """Base64-encoded resource bytes, without a data URI prefix.

    Decode this field to recover the downloaded file.
    """

    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
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
