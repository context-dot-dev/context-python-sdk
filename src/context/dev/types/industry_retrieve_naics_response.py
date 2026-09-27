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
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class IndustryRetrieveNaicsResponse(BaseModel):
    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    codes: Optional[List[Code]] = None
    """Array of NAICS codes and titles."""

    domain: Optional[str] = None
    """Domain found for the brand"""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """
    True when the timeout ended processing and this response contains only usable
    results completed so far. Unfinished results are omitted.
    """

    status: Optional[str] = None
    """Always `ok` on success."""

    type: Optional[str] = None
    """Industry classification type, for naics api it will be `naics`"""
