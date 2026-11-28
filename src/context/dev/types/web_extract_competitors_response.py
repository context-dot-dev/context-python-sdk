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
    """Short description of what the competitor offers."""

    domain: str
    """Competitor's official domain, normalized."""

    name: str
    """Competitor company or product name."""

    source_urls: List[str] = FieldInfo(alias="sourceUrls")
    """Search result URLs used as evidence for this competitor."""

    url: str
    """Competitor's website URL."""


class Target(BaseModel):
    """Profile of the requested company, inferred from its website."""

    company_name: str = FieldInfo(alias="companyName")
    """Company or product name, inferred from its website."""

    field: str
    """Product category or market the company operates in."""

    field_description: str = FieldInfo(alias="fieldDescription")
    """One-sentence summary of what the company sells and who it serves."""

    website_url: str = FieldInfo(alias="websiteUrl")
    """Website URL that was analyzed."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class WebExtractCompetitorsResponse(BaseModel):
    competitors: List[Competitor]
    """Direct competitors, ordered by relevance and confidence."""

    domain: str
    """Normalized domain from the request."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: Literal["ok"]
    """Always `ok` on success."""

    target: Target
    """Profile of the requested company, inferred from its website."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """
    `true` when the deadline passed with `timeoutOpts.behavior` set to
    `return-partial`. Only results finished in time are included.
    """
