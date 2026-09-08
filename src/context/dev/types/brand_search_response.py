# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BrandSearchResponse", "Result", "KeyMetadata"]


class Result(BaseModel):
    domain: str
    """The brand's domain."""

    logo: str
    """
    Logo link URL that serves the brand's logo, generated per request for the
    calling organization.
    """

    name: str
    """The brand's name. Empty string when unknown."""


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class BrandSearchResponse(BaseModel):
    results: List[Result]
    """
    Up to 10 matching brands, name matches first, then domain matches, most popular
    first within each group. Empty when nothing matches.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
