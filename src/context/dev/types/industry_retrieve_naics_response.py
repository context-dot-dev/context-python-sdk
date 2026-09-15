# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IndustryRetrieveNaicsResponse", "Code", "KeyMetadata"]


class Code(BaseModel):
    code: str
    """NAICS code"""

    confidence: Literal["high", "medium", "low"]
    """Confidence level for how well this NAICS code matches the company description"""

    name: str
    """NAICS title"""


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class IndustryRetrieveNaicsResponse(BaseModel):
    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    codes: Optional[List[Code]] = None
    """Array of NAICS codes and titles."""

    domain: Optional[str] = None
    """Domain found for the brand"""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
    """
    True when the timeout ended processing and this response contains only usable
    results completed so far. Unfinished results are omitted.
    """

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""

    type: Optional[str] = None
    """Industry classification type, for naics api it will be `naics`"""
