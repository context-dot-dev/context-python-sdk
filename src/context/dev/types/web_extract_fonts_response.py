# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebExtractFontsResponse", "CacheMetadata", "Font", "FontLinks", "KeyMetadata"]


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


class Font(BaseModel):
    fallbacks: List[str]
    """Array of fallback font families"""

    font: str
    """Font family name"""

    num_elements: float
    """Number of elements using this font"""

    num_words: float
    """Number of words using this font"""

    percent_elements: float
    """Percentage of elements using this font"""

    percent_words: float
    """Percentage of words using this font"""

    uses: List[str]
    """Array of CSS selectors or element types where this font is used"""


class FontLinks(BaseModel):
    files: Dict[str, str]
    """Upright font files keyed by weight string (e.g.

    "400" for regular, "500", "700"). Values are absolute URLs.
    """

    type: Literal["google", "custom"]

    category: Optional[str] = None
    """Google Fonts category when type is google (e.g.

    sans-serif, serif, monospace, display, handwriting). Omitted for custom fonts
    when unknown.
    """

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """
    Present when type is custom: human-readable name derived from the fontLinks key
    (strip build/hash suffixes, split camelCase / PascalCase, normalize separators).
    Google entries omit this.
    """


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebExtractFontsResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    code: int
    """HTTP status code, e.g., 200"""

    domain: str
    """The normalized domain that was processed"""

    fonts: List[Font]
    """Array of font usage information"""

    status: str
    """Status of the response, e.g., 'ok'"""

    font_links: Optional[Dict[str, FontLinks]] = FieldInfo(alias="fontLinks", default=None)
    """
    Font assets keyed by family name as it appears in the fonts array (non-generic
    names only). Clients match entries in fonts to pick a file URL from files.
    Omitted when no families resolve to Google or custom @font-face URLs.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
