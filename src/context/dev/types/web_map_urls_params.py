# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebMapURLsParams", "TimeoutOpts"]


class WebMapURLsParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to map, e.g. `stripe.com`."""

    headers: Dict[str, str]
    """HTTP headers for the target origin. Non-empty headers bypass caching."""

    include_subdomains: Annotated[bool, PropertyInfo(alias="includeSubdomains")]
    """Include URLs on subdomains."""

    max_links: Annotated[int, PropertyInfo(alias="maxLinks")]
    """Maximum number of URLs to return."""

    search: str
    """Filter URLs by a topic or phrase, most relevant first."""

    sitemap_url: Annotated[str, PropertyInfo(alias="sitemapUrl")]
    """Fetch this sitemap instead of discovering sitemaps.

    Must belong to the domain or a subdomain.
    """

    tags: SequenceNotStr[str]
    """Comma-separated labels for filtering usage, e.g. `production,team-alpha`."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Optional RE2-compatible regex pattern.

    Only URLs matching this pattern are returned and counted against maxLinks.
    """

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
