# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebScrapeImagesParams", "Enrichment"]


class WebWebScrapeImagesParams(TypedDict, total=False):
    url: Required[str]
    """Page URL to inspect. Must include http:// or https://."""

    dedupe: Union[bool, Literal["true", "false"]]
    """
    When true, visually duplicate images are removed: every image is loaded and
    perceptually hashed, and only the highest-resolution copy of each duplicate
    group is kept. Images that cannot be downloaded or hashed are kept. Default:
    false.
    """

    enrichment: Optional[Enrichment]
    """
    Optional per-image processing, sent as deep-object query params such as
    enrichment[resolution]=true.
    """

    headers: Dict[str, str]
    """
    Optional outbound HTTP headers forwarded only to the target URL, sent as
    deep-object query params such as headers[X-Custom]=value. When provided, caching
    is bypassed: the result is neither read from nor written to cache.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Reuse a cached result this many milliseconds old or newer.

    Default: 86400000 (1 day). Set to 0 to bypass cache. Maximum: 2592000000 (30
    days).
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

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before
    collecting images. Min: 0. Max: 30000 (30 seconds).
    """


class Enrichment(TypedDict, total=False):
    """
    Optional per-image processing, sent as deep-object query params such as enrichment[resolution]=true.
    """

    classification: Union[bool, Literal["true", "false"]]
    """Classify each image by visual asset type."""

    hosted_url: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="hostedUrl")]
    """
    Host materializable images on the Brand.dev CDN and return their URL and MIME
    type.
    """

    max_time_per_ms: Annotated[int, PropertyInfo(alias="maxTimePerMs")]
    """Per-image enrichment timeout in milliseconds. Default: 30000. Maximum: 60000."""

    resolution: Union[bool, Literal["true", "false"]]
    """Measure image width and height when possible."""
