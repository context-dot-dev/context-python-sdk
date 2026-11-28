# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebMapURLsParams", "TimeoutOpts"]


class WebMapURLsParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to map, such as `stripe.com`."""

    exclude_url_regex: Annotated[str, PropertyInfo(alias="excludeUrlRegex")]
    """Leave out URLs matching this regex, even when they match `urlRegex`."""

    headers: Dict[str, str]
    """HTTP headers to send to the target site. Requests with headers skip the cache."""

    include_subdomains: Annotated[bool, PropertyInfo(alias="includeSubdomains")]
    """Include URLs on subdomains."""

    max_links: Annotated[int, PropertyInfo(alias="maxLinks")]
    """Maximum number of URLs to return."""

    policies: SequenceNotStr[str]
    """Comma-separated access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    search: str
    """Filter URLs by a topic or phrase, most relevant first."""

    sitemap_url: Annotated[str, PropertyInfo(alias="sitemapUrl")]
    """Fetch this sitemap instead of discovering sitemaps.

    Must belong to the domain or a subdomain.
    """

    tags: SequenceNotStr[str]
    """Comma-separated labels for this request, such as `production,team-alpha`.

    Filter usage and request logs by them.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Only return URLs matching this regex. Only matches count toward `maxLinks`."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
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
