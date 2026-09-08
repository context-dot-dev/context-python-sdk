# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebExtractFontsParams"]


class WebExtractFontsParams(TypedDict, total=False):
    direct_url: Annotated[str, PropertyInfo(alias="directUrl")]
    """
    A specific URL to fetch fonts from directly, bypassing domain resolution (e.g.,
    'https://example.com/design-system'). When provided, fonts are extracted from
    this exact URL. You must provide either 'domain' or 'directUrl', but not both.
    """

    domain: str
    """Domain name to extract fonts from (e.g., 'example.com', 'google.com').

    The domain will be automatically normalized and validated. You must provide
    either 'domain' or 'directUrl', but not both.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Maximum age in milliseconds for cached brand data before the API performs a hard
    refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
    are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
    year.
    """

    tags: SequenceNotStr[str]
    """Comma-separated tags for tracking request usage.

    Up to 20 tags, each 1-50 characters.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """
