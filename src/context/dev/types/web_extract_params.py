# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebExtractParams", "Pdf"]


class WebExtractParams(TypedDict, total=False):
    schema: Required[Dict[str, object]]
    """JSON Schema for the returned data object.

    TypeScript Zod users can pass a JSON Schema generated from a Zod object; Python
    users can pass the equivalent JSON Schema object.
    """

    url: Required[str]
    """The starting website URL to crawl and extract from.

    Must include http:// or https://.
    """

    fact_check: Annotated[bool, PropertyInfo(alias="factCheck")]
    """
    When true, every returned value must be grounded in facts stated on the page;
    fields that cannot be supported by the page are returned as null/empty. When
    false (default), the model may make reasonable inferences and derivations from
    the page content (e.g. ideal customer, competitor analysis, recommendations)
    while keeping verifiable specifics (names, quotes, URLs, dates, metrics)
    faithful to the source.
    """

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """When true, follow links on subdomains of the starting URL's domain."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """When true, iframe contents are included in Markdown before extraction."""

    instructions: str
    """
    Optional extraction guidance, such as which facts to prioritize or how to
    interpret fields in the schema.
    """

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return cached scrape results if a prior scrape for the same parameters is
    younger than this many milliseconds. Defaults to 7 days (604800000 ms).
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Optional maximum link depth from the starting URL (0 = only the starting page).

    If omitted, there is no crawl depth limit.
    """

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum number of pages to analyze for extraction. Hard cap: 50. Defaults to 5."""

    pdf: Pdf

    stop_after_ms: Annotated[int, PropertyInfo(alias="stopAfterMs")]
    """Soft time budget for the crawl in milliseconds.

    Min: 10000 (10s). Max: 110000 (110s). Default: 80000 (80s).
    """

    tags: SequenceNotStr[str]
    """Optional caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load for each
    crawled page.
    """


class Pdf(TypedDict, total=False):
    end: int
    """Last 1-based PDF page to parse.

    Must be greater than or equal to start when both are provided.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF pages are fetched and parsed. When false, PDF pages are skipped."""

    start: int
    """First 1-based PDF page to parse."""
