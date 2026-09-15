# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebExtractCompetitorsResponse", "Competitor", "Target", "KeyMetadata"]


class Competitor(BaseModel):
    confidence: Literal["high", "medium"]
    """Confidence that this company is a direct competitor."""

    description: str
    """Short description of the competitor."""

    domain: str
    """Competitor's normalized official domain."""

    name: str
    """Competitor company or product name."""

    source_urls: List[str] = FieldInfo(alias="sourceUrls")
    """Search result URLs used as evidence for this competitor."""

    url: str
    """Competitor website URL."""


class Target(BaseModel):
    """Target company profile inferred from the landing page."""

    company_name: str = FieldInfo(alias="companyName")
    """Company or product name inferred from the landing page."""

    field: str
    """Specific operating field, product category, or market."""

    field_description: str = FieldInfo(alias="fieldDescription")
    """One-sentence description of what the target company sells and who it serves."""

    website_url: str = FieldInfo(alias="websiteUrl")
    """Resolved URL used for the landing page analysis."""


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebExtractCompetitorsResponse(BaseModel):
    competitors: List[Competitor]
    """Direct competitors ordered by relevance and confidence."""

    domain: str
    """Normalized input domain."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    status: Literal["ok"]
    """Status of the response."""

    target: Target
    """Target company profile inferred from the landing page."""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
    """
    True when the timeout ended processing and this response contains only usable
    results completed so far. Unfinished results are omitted.
    """
