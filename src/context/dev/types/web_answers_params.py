# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebAnswersParams", "Controls", "TimeoutOpts"]


class WebAnswersParams(TypedDict, total=False):
    task: Required[str]
    """Research task, up to 2000 characters.

    The agent selects company/profile lookups, web searches, or page reads. Include
    domains or URLs to focus the research.
    """

    controls: Controls
    """Limits what the research may use."""

    json_format: Dict[str, object]
    """Example answer object, not JSON Schema.

    Up to 8 levels, 500 values, and 16000 characters; unknowns may be null.
    """

    mode: Literal["fast", "ultra"]
    """
    `fast` prioritizes speed, with extra verification for people and companies;
    `ultra` supports deeper research (default).
    """

    policies: SequenceNotStr[str]
    """Access policy IDs to apply.

    A URL must pass every policy. Leave it out unless access policies are enabled
    for your organization; otherwise the request fails with
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Controls(TypedDict, total=False):
    """Limits what the research may use."""

    exclude_sources: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSources")]
    """Never search, read or cite these sites, sections or pages.

    Same format as `sources`. Up to 100 entries.
    """

    sources: SequenceNotStr[str]
    """Only search, read and cite these sites, sections or pages.

    Each entry is a URL prefix: "example.com" covers the site and its subdomains,
    "example.com/docs" covers that section, and "example.com/docs/setup.html" is one
    page. Up to 20 entries.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    """
