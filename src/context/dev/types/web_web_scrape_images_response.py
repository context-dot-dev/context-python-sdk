# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebWebScrapeImagesResponse", "CacheMetadata", "Image", "ImageEnrichment", "ActionsApplied", "KeyMetadata"]


class CacheMetadata(BaseModel):
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing to the output was a hit; age_ms is the oldest contributing hit.
    """

    age_ms: int
    """Age of the cached data in milliseconds. Zero for miss and zdr responses."""

    status: Literal["hit", "miss", "zdr"]
    """
    Whether the response was served from cache, required fresh work, or honored
    zero-data-retention cache bypass.
    """


class ImageEnrichment(BaseModel):
    """Requested metadata for images that could be processed."""

    height: Optional[int] = None
    """Image height in pixels, when measured."""

    mimetype: Optional[str] = None
    """Detected MIME type, when hosted."""

    type: Optional[
        Literal["photography", "illustration", "logo", "wordmark", "icon", "pattern", "graphic", "other"]
    ] = None
    """Visual asset category, when classified."""

    url: Optional[str] = None
    """Brand.dev CDN URL, when hosted."""

    width: Optional[int] = None
    """Image width in pixels, when measured."""


class Image(BaseModel):
    alt: Optional[str] = None
    """Image alt text, or null when unavailable."""

    element: Literal["img", "svg", "link", "source", "video", "css", "object", "meta", "background"]
    """Where the image was found."""

    src: str
    """Original image value: URL, inline SVG or HTML, or base64 data URI."""

    type: Literal["url", "html", "base64"]
    """Format of src."""

    enrichment: Optional[ImageEnrichment] = None
    """Requested metadata for images that could be processed."""


class ActionsApplied(BaseModel):
    instruction: str

    status: Literal["applied", "failed", "skipped"]
    """Applied means the requested page state was visibly verified.

    Failed means it was not verified. Skipped means it was not attempted.
    """

    completion_evidence: Optional[str] = FieldInfo(alias="completionEvidence", default=None)
    """Visible page evidence used to verify an applied action."""

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    error: Optional[str] = None

    method: Optional[str] = None

    target_description: Optional[str] = FieldInfo(alias="targetDescription", default=None)


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebWebScrapeImagesResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    images: List[Image]
    """Images found on the page."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    success: Literal[True]
    """Always true on success."""

    url: str
    """Page URL that was scraped."""

    actions_applied: Optional[List[ActionsApplied]] = FieldInfo(alias="actionsApplied", default=None)
    """One verified outcome per requested browser action, in request order."""

    final_dom_state: Optional[Literal["loaded", "still-loading"]] = FieldInfo(alias="finalDOMState", default=None)
    """How complete the returned content is.

    `loaded` means the page finished the waits the request asked for.
    `still-loading` only occurs with timeoutOpts.behavior=return-partial: the
    timeoutOpts.milliseconds deadline was reached first, so the content reflects the
    DOM at that moment and late-rendering parts may be missing. Partial results are
    billed at the base request cost.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
    """True when the deadline interrupted rendering or image enrichment.

    Partial results are billed at the base request cost, without enrichment or
    actions surcharges.
    """
