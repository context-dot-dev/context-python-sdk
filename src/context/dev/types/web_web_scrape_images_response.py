# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebWebScrapeImagesResponse", "Image", "ImageEnrichment", "KeyMetadata"]


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


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class WebWebScrapeImagesResponse(BaseModel):
    images: List[Image]
    """Images found on the page."""

    success: Literal[True]
    """Always true on success."""

    url: str
    """Page URL that was scraped."""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
