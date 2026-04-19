# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

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

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """
