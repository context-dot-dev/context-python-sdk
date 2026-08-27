# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "BrandRetrieveSimplifiedResponse",
    "CacheMetadata",
    "Brand",
    "BrandBackdrop",
    "BrandBackdropColor",
    "BrandBackdropResolution",
    "BrandColor",
    "BrandLogo",
    "BrandLogoColor",
    "BrandLogoResolution",
    "KeyMetadata",
]


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


class BrandBackdropColor(BaseModel):
    hex: Optional[str] = None
    """Color in hexadecimal format"""

    name: Optional[str] = None
    """Name of the color"""


class BrandBackdropResolution(BaseModel):
    """Resolution of the backdrop image"""

    aspect_ratio: Optional[float] = None
    """Aspect ratio of the image (width/height)"""

    height: Optional[int] = None
    """Height of the image in pixels"""

    width: Optional[int] = None
    """Width of the image in pixels"""


class BrandBackdrop(BaseModel):
    colors: Optional[List[BrandBackdropColor]] = None
    """Array of colors in the backdrop image"""

    resolution: Optional[BrandBackdropResolution] = None
    """Resolution of the backdrop image"""

    url: Optional[str] = None
    """URL of the backdrop image"""


class BrandColor(BaseModel):
    hex: Optional[str] = None
    """Color in hexadecimal format"""

    name: Optional[str] = None
    """Name of the color"""

    source: Optional[Literal["site", "logo"]] = None
    """
    Where the color was observed: 'site' colors come from the website's own theme
    signals (rendered page colors, manifest, theme-color meta), 'logo' colors from
    logo image pixels.
    """


class BrandLogoColor(BaseModel):
    hex: Optional[str] = None
    """Color in hexadecimal format"""

    name: Optional[str] = None
    """Name of the color"""


class BrandLogoResolution(BaseModel):
    """Resolution of the logo image"""

    aspect_ratio: Optional[float] = None
    """Aspect ratio of the image (width/height)"""

    height: Optional[int] = None
    """Height of the image in pixels"""

    width: Optional[int] = None
    """Width of the image in pixels"""


class BrandLogo(BaseModel):
    colors: Optional[List[BrandLogoColor]] = None
    """Array of colors in the logo"""

    mode: Optional[Literal["light", "dark", "has_opaque_background"]] = None
    """
    Indicates when this logo is best used: 'light' = best for light mode, 'dark' =
    best for dark mode, 'has_opaque_background' = can be used for either as image
    has its own background
    """

    resolution: Optional[BrandLogoResolution] = None
    """Resolution of the logo image"""

    type: Optional[Literal["icon", "logo"]] = None
    """Type of the logo based on resolution (e.g., 'icon', 'logo')"""

    url: Optional[str] = None
    """CDN hosted url of the logo (ready for display)"""


class Brand(BaseModel):
    """Simplified brand information"""

    backdrops: Optional[List[BrandBackdrop]] = None
    """An array of backdrop images for the brand"""

    colors: Optional[List[BrandColor]] = None
    """An array of brand colors"""

    domain: Optional[str] = None
    """The domain name of the brand"""

    logos: Optional[List[BrandLogo]] = None
    """An array of logos associated with the brand"""

    title: Optional[str] = None
    """The title or name of the brand"""


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class BrandRetrieveSimplifiedResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    brand: Optional[Brand] = None
    """Simplified brand information"""

    code: Optional[int] = None
    """HTTP status code of the response"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""
