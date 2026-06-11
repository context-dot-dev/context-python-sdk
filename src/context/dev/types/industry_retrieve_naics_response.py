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
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class IndustryRetrieveNaicsResponse(BaseModel):
    codes: Optional[List[Code]] = None
    """Array of NAICS codes and titles."""

    domain: Optional[str] = None
    """Domain found for the brand"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""

    type: Optional[str] = None
    """Industry classification type, for naics api it will be `naics`"""
