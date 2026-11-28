# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WebExtractStyleguideResponse",
    "CacheMetadata",
    "KeyMetadata",
    "Styleguide",
    "StyleguideColors",
    "StyleguideComponents",
    "StyleguideComponentsButton",
    "StyleguideComponentsButtonLink",
    "StyleguideComponentsButtonPrimary",
    "StyleguideComponentsButtonSecondary",
    "StyleguideComponentsCard",
    "StyleguideElementSpacing",
    "StyleguideFontLinks",
    "StyleguideFontLinksFace",
    "StyleguideShadows",
    "StyleguideTypography",
    "StyleguideTypographyHeadings",
    "StyleguideTypographyHeadingsH1",
    "StyleguideTypographyHeadingsH2",
    "StyleguideTypographyHeadingsH3",
    "StyleguideTypographyHeadingsH4",
    "StyleguideTypographyP",
]


class CacheMetadata(BaseModel):
    """Cache status of this response."""

    age_ms: int
    """Age of the cached data, in milliseconds. `0` for `miss` and `zdr`."""

    status: Literal["hit", "miss", "zdr"]
    """
    `hit` when served from cache, `miss` when fetched fresh, `zdr` when zero data
    retention bypassed the cache.
    """


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class StyleguideColors(BaseModel):
    """Core colors used on the website."""

    accent: str
    """Accent color, in hex."""

    background: str
    """Background color, in hex."""

    text: str
    """Text color, in hex."""


class StyleguideComponentsButtonLink(BaseModel):
    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """Border color in hex: `#RRGGBB`, or `#RRGGBBAA` when the border is translucent."""

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")
    """Computed `box-shadow`, with layers separated by commas."""

    color: str

    css: str
    """Ready-to-use CSS declarations for this style."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    min_height: str = FieldInfo(alias="minHeight")
    """Minimum height as a CSS length, usually in pixels."""

    min_width: str = FieldInfo(alias="minWidth")
    """Minimum width as a CSS length, usually in pixels."""

    padding: str

    text_decoration: str = FieldInfo(alias="textDecoration")

    font_fallbacks: Optional[List[str]] = FieldInfo(alias="fontFallbacks", default=None)
    """Full font stack from the computed `font-family`, in order."""

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Button typeface, the first entry in `fontFallbacks`."""

    text_decoration_color: Optional[str] = FieldInfo(alias="textDecorationColor", default=None)
    """Underline color in hex, when it differs from the text color."""


class StyleguideComponentsButtonPrimary(BaseModel):
    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """Border color in hex: `#RRGGBB`, or `#RRGGBBAA` when the border is translucent."""

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")
    """Computed `box-shadow`, with layers separated by commas."""

    color: str

    css: str
    """Ready-to-use CSS declarations for this style."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    min_height: str = FieldInfo(alias="minHeight")
    """Minimum height as a CSS length, usually in pixels."""

    min_width: str = FieldInfo(alias="minWidth")
    """Minimum width as a CSS length, usually in pixels."""

    padding: str

    text_decoration: str = FieldInfo(alias="textDecoration")

    font_fallbacks: Optional[List[str]] = FieldInfo(alias="fontFallbacks", default=None)
    """Full font stack from the computed `font-family`, in order."""

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Button typeface, the first entry in `fontFallbacks`."""

    text_decoration_color: Optional[str] = FieldInfo(alias="textDecorationColor", default=None)
    """Underline color in hex, when it differs from the text color."""


class StyleguideComponentsButtonSecondary(BaseModel):
    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """Border color in hex: `#RRGGBB`, or `#RRGGBBAA` when the border is translucent."""

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")
    """Computed `box-shadow`, with layers separated by commas."""

    color: str

    css: str
    """Ready-to-use CSS declarations for this style."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    min_height: str = FieldInfo(alias="minHeight")
    """Minimum height as a CSS length, usually in pixels."""

    min_width: str = FieldInfo(alias="minWidth")
    """Minimum width as a CSS length, usually in pixels."""

    padding: str

    text_decoration: str = FieldInfo(alias="textDecoration")

    font_fallbacks: Optional[List[str]] = FieldInfo(alias="fontFallbacks", default=None)
    """Full font stack from the computed `font-family`, in order."""

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Button typeface, the first entry in `fontFallbacks`."""

    text_decoration_color: Optional[str] = FieldInfo(alias="textDecorationColor", default=None)
    """Underline color in hex, when it differs from the text color."""


class StyleguideComponentsButton(BaseModel):
    """Primary, secondary, and link button styles."""

    link: Optional[StyleguideComponentsButtonLink] = None

    primary: Optional[StyleguideComponentsButtonPrimary] = None

    secondary: Optional[StyleguideComponentsButtonSecondary] = None


class StyleguideComponentsCard(BaseModel):
    """Card style."""

    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """Border color in hex: `#RRGGBB`, or `#RRGGBBAA` when the border is translucent."""

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")

    css: str
    """Ready-to-use CSS declarations for this style."""

    padding: str

    text_color: str = FieldInfo(alias="textColor")


class StyleguideComponents(BaseModel):
    """Styles for buttons and cards."""

    button: StyleguideComponentsButton
    """Primary, secondary, and link button styles."""

    card: Optional[StyleguideComponentsCard] = None
    """Card style."""


class StyleguideElementSpacing(BaseModel):
    """Spacing scale used on the website, from `xs` to `xl`."""

    lg: str

    md: str

    sm: str

    xl: str

    xs: str


class StyleguideFontLinksFace(BaseModel):
    style: str
    """
    CSS `font-style` descriptor: `normal`, `italic`, or `oblique`, with an optional
    angle or angle range such as `oblique 10deg 20deg`.
    """

    url: str
    """URL of the font file, or an inline data URL."""

    weight: str
    """CSS `font-weight` descriptor.

    A variable font can have a range such as `300 500`, which covers every weight in
    between with one file.
    """

    unicode_range: Optional[str] = FieldInfo(alias="unicodeRange", default=None)
    """CSS `unicode-range` descriptor."""

    width: Optional[str] = None
    """CSS `font-width` or `font-stretch` descriptor."""


class StyleguideFontLinks(BaseModel):
    type: Literal["google", "custom"]
    """`google` for Google Fonts, `custom` for any other font source."""

    category: Optional[str] = None
    """
    Google Fonts category, such as `sans-serif`, `serif`, `monospace`, `display`, or
    `handwriting`. Omitted for custom fonts when unknown.
    """

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """
    Human-readable family name: the `fontLinks` key for custom fonts, or the
    official Google Fonts name for Google fonts.
    """

    faces: Optional[List[StyleguideFontLinksFace]] = None
    """Font faces found for this family, one per style, weight, and Unicode subset."""

    files: Optional[Dict[str, str]] = None
    """Deprecated upright font lookup keyed by weight string.

    A variable font can map several standard weight keys to the same URL; faces
    retains its actual weight range.
    """


class StyleguideShadows(BaseModel):
    """Box shadow scale used on the website, from `sm` to `xl`, plus `inner`."""

    inner: str

    lg: str

    md: str

    sm: str

    xl: str


class StyleguideTypographyHeadingsH1(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full font stack from the computed `font-family`, in order."""

    font_family: str = FieldInfo(alias="fontFamily")
    """First font in the stack."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadingsH2(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full font stack from the computed `font-family`, in order."""

    font_family: str = FieldInfo(alias="fontFamily")
    """First font in the stack."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadingsH3(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full font stack from the computed `font-family`, in order."""

    font_family: str = FieldInfo(alias="fontFamily")
    """First font in the stack."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadingsH4(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full font stack from the computed `font-family`, in order."""

    font_family: str = FieldInfo(alias="fontFamily")
    """First font in the stack."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadings(BaseModel):
    """Styles for `h1` through `h4` headings."""

    h1: Optional[StyleguideTypographyHeadingsH1] = None

    h2: Optional[StyleguideTypographyHeadingsH2] = None

    h3: Optional[StyleguideTypographyHeadingsH3] = None

    h4: Optional[StyleguideTypographyHeadingsH4] = None


class StyleguideTypographyP(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full font stack from the computed `font-family`, in order."""

    font_family: str = FieldInfo(alias="fontFamily")
    """First font in the stack."""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypography(BaseModel):
    """Text styles for headings and body text."""

    headings: StyleguideTypographyHeadings
    """Styles for `h1` through `h4` headings."""

    p: Optional[StyleguideTypographyP] = None


class Styleguide(BaseModel):
    """Design tokens and component styles extracted from the website."""

    colors: StyleguideColors
    """Core colors used on the website."""

    components: StyleguideComponents
    """Styles for buttons and cards."""

    element_spacing: StyleguideElementSpacing = FieldInfo(alias="elementSpacing")
    """Spacing scale used on the website, from `xs` to `xl`."""

    font_links: Dict[str, StyleguideFontLinks] = FieldInfo(alias="fontLinks")
    """
    Font files keyed by family name, as it appears in `fontFamily` and
    `fontFallbacks`. Generic families are left out. Match style and weight against
    `faces` to pick a file.
    """

    mode: Literal["light", "dark"]
    """Whether the site's design is mainly light or dark."""

    shadows: StyleguideShadows
    """Box shadow scale used on the website, from `sm` to `xl`, plus `inner`."""

    typography: StyleguideTypography
    """Text styles for headings and body text."""


class WebExtractStyleguideResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache status of this response."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    code: Optional[int] = None
    """HTTP status code, repeated in the body."""

    domain: Optional[str] = None
    """Normalized domain that was analyzed."""

    final_dom_state: Optional[Literal["loaded", "still-loading"]] = FieldInfo(alias="finalDOMState", default=None)
    """
    `loaded`, or `still-loading` when capture ended before the page finished
    loading.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    status: Optional[str] = None
    """Always `ok` on success."""

    styleguide: Optional[Styleguide] = None
    """Design tokens and component styles extracted from the website."""
