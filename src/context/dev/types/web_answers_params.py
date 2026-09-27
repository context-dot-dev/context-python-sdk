# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebAnswersParams", "TimeoutOpts"]


class WebAnswersParams(TypedDict, total=False):
    task: Required[str]
    """Research task. Name a domain to have it read before searching."""

    json_format: Dict[str, object]
    """Example answer object, not JSON Schema.

    Up to 8 levels, 500 values, and 16000 characters; unknowns may be null.
    """

    mode: Literal["fast", "ultra"]
    """`fast` for short tasks; `ultra` for deeper research (default)."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

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
    """
