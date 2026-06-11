# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IndustryRetrieveSicResponse", "Code", "KeyMetadata"]


class Code(BaseModel):
    code: str
    """SIC code (4-digit)."""

    confidence: Literal["high", "medium", "low"]
    """Confidence level for how well this SIC code matches the company description."""

    name: str
    """SIC industry title."""

    major_group: Optional[str] = FieldInfo(alias="majorGroup", default=None)
    """2-digit major group identifier (the leading two digits of the code).

    Only present when `classification` is `original_sic`.
    """

    major_group_name: Optional[str] = FieldInfo(alias="majorGroupName", default=None)
    """Description of the 2-digit major group.

    Only present when `classification` is `original_sic`.
    """

    office: Optional[str] = None
    """SEC review office responsible for filings under this code.

    Only present when `classification` is `latest_sec`.
    """


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class IndustryRetrieveSicResponse(BaseModel):
    classification: Optional[Literal["original_sic", "latest_sec"]] = None
    """Echoes back which SIC dataset was used to classify the brand."""

    codes: Optional[List[Code]] = None
    """Array of SIC codes with confidence scores.

    Extra fields depend on the requested classification: `original_sic` results
    include `majorGroup` and `majorGroupName`; `latest_sec` results include
    `office`.
    """

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
    """Industry classification type, for sic api it will be `sic`"""
