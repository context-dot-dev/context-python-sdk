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
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class BrandSearchResponse(BaseModel):
    results: List[Result]
    """
    Up to 10 matching brands, name matches first, then domain matches, most popular
    first within each group. Empty when nothing matches.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
