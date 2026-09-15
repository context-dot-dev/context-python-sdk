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
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class IndustryRetrieveSicResponse(BaseModel):
    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

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
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
    """
    True when the timeout ended processing and this response contains only usable
    results completed so far. Unfinished results are omitted.
    """

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""

    type: Optional[str] = None
    """Industry classification type, for sic api it will be `sic`"""
