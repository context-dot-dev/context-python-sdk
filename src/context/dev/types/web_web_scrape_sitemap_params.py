# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebScrapeSitemapParams", "TimeoutOpts"]


class WebWebScrapeSitemapParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to build a sitemap for"""

    headers: Dict[str, str]
    """
    Optional outbound HTTP headers forwarded only to the target URL, sent as
    deep-object query params such as headers[X-Custom]=value. When provided, caching
    is bypassed: the result is neither read from nor written to cache.
    """

    include_subdomains: Annotated[bool, PropertyInfo(alias="includeSubdomains")]
    """
    When true, discover and include public pages and sitemaps on subdomains of the
    requested domain. Defaults to false.
    """

    max_links: Annotated[int, PropertyInfo(alias="maxLinks")]
    """Maximum number of links to return from the sitemap crawl.

    Defaults to 10,000. Minimum is 1, maximum is 100,000.
    """

    search: str
    """Optional search phrase.

    When provided, the crawled sitemap is filtered to the pages whose URLs are about
    that phrase, most relevant first, and the request costs 2 credits instead of 1.
    """

    sitemap_url: Annotated[str, PropertyInfo(alias="sitemapUrl")]
    """Optional explicit sitemap URL.

    When provided, exactly this sitemap is crawled instead of discovering the
    domain's sitemaps.
    """

    tags: SequenceNotStr[str]
    """Comma-separated tags for tracking request usage.

    Up to 20 tags, each 1-50 characters.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Optional RE2-compatible regex pattern.

    Only URLs matching this pattern are returned and counted against maxLinks.
    """

    zdr: Literal["enabled", "disabled"]
    """
    Set to enabled to bypass shared caches and omit request and response content
    from retained usage logs. Requires zero data retention to be enabled for your
    organization (contact support@context.dev), otherwise the request fails with
    ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.
    """


class TimeoutOpts(TypedDict, total=False):
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded timeoutOpts object.
    """

    milliseconds: Required[int]
    """Request deadline in milliseconds. Maximum: 300000 (5 minutes)."""

    behavior: Literal["fail", "return-partial"]
    """What to do at the deadline.

    "fail" returns 408 REQUEST_TIMEOUT without charging credits. "return-partial"
    returns usable results collected so far; if none are available, the request
    still fails without charging credits. Partial results are not cached as complete
    results.
    """
