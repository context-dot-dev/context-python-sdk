# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebScrapeScreenshotParams", "TimeoutOpts", "Viewport"]


class WebWebScrapeScreenshotParams(TypedDict, total=False):
    url: Required[str]

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
    """
    Fetch the target page through a residential proxy in this country (ISO 3166-1
    alpha-2).
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

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached screenshot if a prior screenshot for the same parameters exists
    and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.
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
    """Comma-separated tags for tracking request usage.

    Up to 20 tags, each 1-50 characters.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """

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
    """
    Set to enabled to bypass shared caches and omit request and response content
    from retained usage logs. Asset uploads are skipped, so hosted image URLs are
    omitted. Requires zero data retention to be enabled for your organization
    (contact support@context.dev), otherwise the request fails with ZDR_NOT_ENABLED.
    Successful ZDR responses include X-Context-ZDR: true.
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
    results. "return-partial" requires milliseconds of at least 5000.
    """


class Viewport(TypedDict, total=False):
    """Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080."""

    height: int
    """Viewport height in pixels."""

    width: int
    """Viewport width in pixels."""
