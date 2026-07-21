# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebScrapeSitemapParams"]


class WebWebScrapeSitemapParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to build a sitemap for"""

    headers: Dict[str, str]
    """
    Optional outbound HTTP headers forwarded only to the target URL, sent as
    deep-object query params such as headers[X-Custom]=value. When provided, caching
    is bypassed: the result is neither read from nor written to cache.
    """

    max_links: Annotated[int, PropertyInfo(alias="maxLinks")]
    """Maximum number of links to return from the sitemap crawl.

    Defaults to 10,000. Minimum is 1, maximum is 100,000.
    """

    sitemap_url: Annotated[str, PropertyInfo(alias="sitemapUrl")]
    """Optional explicit sitemap URL.

    When provided, exactly this sitemap is crawled instead of discovering the
    domain's sitemaps.
    """

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
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
