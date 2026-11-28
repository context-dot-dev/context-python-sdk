# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebAnswersParams", "Controls", "TimeoutOpts"]


class WebAnswersParams(TypedDict, total=False):
    task: Required[str]
    """What to research, in plain language, up to 2000 characters.

    Include domains or URLs to focus the research.
    """

    controls: Controls
    """Limit which sites the research can search, read, and cite."""

    json_format: Dict[str, object]
    """Example of the answer object to return, not a JSON Schema.

    Up to 8 levels deep, 500 values, and 16,000 characters. Values that cannot be
    found come back as `null`. Defaults to `{ "result": "" }`.
    """

    mode: Literal["fast", "ultra"]
    """
    `fast` prioritizes speed and adds extra verification for people and companies;
    `ultra` searches and reads more sources for deeper research. Defaults to
    `ultra`.
    """

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Controls(TypedDict, total=False):
    """Limit which sites the research can search, read, and cite."""

    exclude_sources: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSources")]
    """Never search, read, or cite these sites, sections, or pages.

    Same format as `sources`.
    """

    sources: SequenceNotStr[str]
    """Only search, read, and cite these sites, sections, or pages.

    Each entry is a URL prefix: `example.com` covers the site and its subdomains,
    `example.com/docs` covers that section, and `example.com/docs/setup.html` is one
    page.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """
