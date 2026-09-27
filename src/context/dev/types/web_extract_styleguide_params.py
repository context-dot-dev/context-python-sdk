# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebExtractStyleguideParams", "TimeoutOpts"]


class WebExtractStyleguideParams(TypedDict, total=False):
    color_scheme: Annotated[Literal["light", "dark"], PropertyInfo(alias="colorScheme")]
    """
    Optional browser color scheme to emulate for websites that respond to
    prefers-color-scheme. This value is part of the styleguide cache key.
    """

    direct_url: Annotated[str, PropertyInfo(alias="directUrl")]
    """Exact URL to inspect. Provide either `domain` or `directUrl`, not both."""

    domain: str
    """Domain name to extract styleguide from (e.g., 'example.com', 'google.com').

    The domain will be automatically normalized and validated. You must provide
    either 'domain' or 'directUrl', but not both.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum age of cached brand data in ms.

    Defaults to 3 months; clamped to 0–1 year. `0` refreshes.
    """

    tags: SequenceNotStr[str]
    """Comma-separated labels for filtering usage, e.g. `production,team-alpha`."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """
