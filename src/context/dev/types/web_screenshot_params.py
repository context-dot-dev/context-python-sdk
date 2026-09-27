# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebScreenshotParams", "TimeoutOpts", "Viewport"]


class WebScreenshotParams(TypedDict, total=False):
    clear_popups: Annotated[bool, PropertyInfo(alias="clearPopups")]
    """Optional parameter for comprehensive popup cleanup.

    If 'true', the browser dismisses detected cookie/consent UI and clears other
    detected obstructive popups and overlays before capture. If 'false' or not
    provided, this parameter requests no cleanup; handleCookiePopup can still
    request cookie/consent handling independently.
    """

    color_scheme: Annotated[Literal["light", "dark"], PropertyInfo(alias="colorScheme")]
    """Optional parameter to choose the site's visual theme in the screenshot.

    Use 'light' or 'dark' when the site offers both appearances.
    """

    country: Literal[
        "ad",
        "ae",
        "af",
        "ag",
        "ai",
        "al",
        "am",
        "ao",
        "ar",
        "at",
        "au",
        "aw",
        "az",
        "ba",
        "bb",
        "bd",
        "be",
        "bf",
        "bg",
        "bh",
        "bi",
        "bj",
        "bm",
        "bn",
        "bo",
        "bq",
        "br",
        "bs",
        "bw",
        "by",
        "bz",
        "ca",
        "cd",
        "cf",
        "cg",
        "ch",
        "ci",
        "cl",
        "cm",
        "cn",
        "co",
        "cr",
        "cv",
        "cw",
        "cy",
        "cz",
        "de",
        "dj",
        "dk",
        "dm",
        "do",
        "dz",
        "ec",
        "ee",
        "eg",
        "es",
        "et",
        "fi",
        "fj",
        "fr",
        "ga",
        "gb",
        "gd",
        "ge",
        "gf",
        "gg",
        "gh",
        "gm",
        "gn",
        "gp",
        "gq",
        "gr",
        "gt",
        "gu",
        "gw",
        "gy",
        "hk",
        "hn",
        "hr",
        "ht",
        "hu",
        "id",
        "ie",
        "il",
        "im",
        "in",
        "iq",
        "ir",
        "is",
        "it",
        "je",
        "jm",
        "jo",
        "jp",
        "ke",
        "kg",
        "kh",
        "kn",
        "kr",
        "kw",
        "ky",
        "kz",
        "la",
        "lb",
        "lc",
        "lk",
        "lr",
        "ls",
        "lt",
        "lu",
        "lv",
        "ly",
        "ma",
        "mc",
        "md",
        "me",
        "mf",
        "mg",
        "mk",
        "ml",
        "mm",
        "mn",
        "mo",
        "mq",
        "mr",
        "mt",
        "mu",
        "mv",
        "mw",
        "mx",
        "my",
        "mz",
        "na",
        "nc",
        "ne",
        "ng",
        "ni",
        "nl",
        "no",
        "np",
        "nz",
        "om",
        "pa",
        "pe",
        "pf",
        "pg",
        "ph",
        "pk",
        "pl",
        "pr",
        "ps",
        "pt",
        "py",
        "qa",
        "re",
        "ro",
        "rs",
        "ru",
        "rw",
        "sa",
        "sc",
        "sd",
        "se",
        "sg",
        "si",
        "sk",
        "sl",
        "sm",
        "sn",
        "so",
        "sr",
        "ss",
        "st",
        "sv",
        "sx",
        "sy",
        "sz",
        "tc",
        "td",
        "tg",
        "th",
        "tj",
        "tl",
        "tm",
        "tn",
        "tr",
        "tt",
        "tw",
        "tz",
        "ua",
        "ug",
        "us",
        "uy",
        "uz",
        "vc",
        "ve",
        "vg",
        "vi",
        "vn",
        "ye",
        "yt",
        "za",
        "zm",
        "zw",
    ]
    """Fetch from this country (ISO 3166-1 alpha-2)."""

    direct_url: Annotated[str, PropertyInfo(alias="directUrl")]
    """
    A specific URL to screenshot directly, bypassing domain resolution (e.g.,
    'https://example.com/pricing'). When provided, the screenshot is taken of this
    exact URL. You must provide either 'domain' or 'directUrl', but not both.
    """

    domain: str
    """Domain name to take screenshot of (e.g., 'example.com', 'google.com').

    The domain will be automatically normalized and validated. You must provide
    either 'domain' or 'directUrl', but not both.
    """

    full_screenshot: Annotated[Literal["true", "false"], PropertyInfo(alias="fullScreenshot")]
    """Optional parameter to determine screenshot type.

    If 'true', takes a full page screenshot capturing all content. If 'false' or not
    provided, takes a viewport screenshot (standard browser view).
    """

    handle_cookie_popup: Annotated[bool, PropertyInfo(alias="handleCookiePopup")]
    """Optional parameter to control cookie/consent popup handling.

    If 'true', we dismiss cookie banner before capture. If 'false' or not provided,
    captures the page without that step.
    """

    headers: Dict[str, str]
    """
    Optional outbound HTTP headers, using the same JSON object or deep-object query
    format as other scrape endpoints (for example headers[Authorization]=Bearer
    token). Headers are scoped to the target origin during capture. For domain/page
    requests, discovery receives no custom headers and only pages on the resolved
    origin are eligible. Non-empty headers bypass screenshot caching and return an
    in-memory data URL; no screenshot is uploaded. Empty objects behave like omitted
    headers.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached screenshot if a prior screenshot for the same parameters exists
    and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.
    """

    page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"]
    """Optional parameter to specify which page type to screenshot.

    If provided, the system will scrape the domain's links and use heuristics to
    find the most appropriate URL for the specified page type (30 supported
    languages). If not provided, screenshots the main domain landing page. Only
    applicable when using 'domain', not 'directUrl'.
    """

    scroll_offset: Annotated[Optional[int], PropertyInfo(alias="scrollOffset")]
    """
    Optional vertical scroll offset in pixels for capturing a long page in
    viewport-sized chunks. When provided, the full page is captured once and the
    returned image is the viewport-sized slice that begins at this Y offset (e.g.
    request scrollOffset=0, then 1080, then 2160 to walk a 1920x1080 landing page
    top to bottom). The final slice may be shorter than the viewport height. Takes
    precedence over fullScreenshot. Max: 100000.
    """

    tags: SequenceNotStr[str]
    """Comma-separated labels for filtering usage, e.g. `production,team-alpha`."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    viewport: Viewport
    """Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080."""

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before taking
    the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
    omitted. When combined with timeoutOpts, timeoutOpts.milliseconds must be at
    least waitForMs + 10000 ms; a shorter deadline is rejected with 400
    TIMEOUT_TOO_SHORT_FOR_WAIT.
    """

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """


class Viewport(TypedDict, total=False):
    """Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080."""

    height: int
    """Viewport height in pixels."""

    width: int
    """Viewport width in pixels."""
