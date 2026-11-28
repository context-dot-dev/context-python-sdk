# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebScreenshotParams", "TimeoutOpts", "Viewport"]


class WebScreenshotParams(TypedDict, total=False):
    clear_popups: Annotated[bool, PropertyInfo(alias="clearPopups")]
    """Dismiss cookie banners and close other popups and overlays before capture."""

    color_scheme: Annotated[Literal["light", "dark"], PropertyInfo(alias="colorScheme")]
    """Emulate a light or dark color scheme."""

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
    """Country to fetch from, as an ISO 3166-1 alpha-2 code."""

    direct_url: Annotated[str, PropertyInfo(alias="directUrl")]
    """Exact URL to capture, such as `https://example.com/pricing`.

    Provide either `domain` or `directUrl`, not both.
    """

    domain: str
    """Domain to capture, such as `stripe.com`.

    Provide either `domain` or `directUrl`, not both.
    """

    full_screenshot: Annotated[Literal["true", "false"], PropertyInfo(alias="fullScreenshot")]
    """Capture the full scrollable page instead of only the viewport."""

    handle_cookie_popup: Annotated[bool, PropertyInfo(alias="handleCookiePopup")]
    """Dismiss cookie consent banners before capture."""

    headers: Dict[str, str]
    """
    HTTP headers to send to the target origin, such as
    `headers[Authorization]=Bearer token`. Requests with headers skip the cache and
    return the image as a data URL.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached result, in milliseconds.

    `0` always fetches fresh. Defaults to 1 day (86400000 ms). Maximum: 30 days
    (2592000000 ms).
    """

    page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"]
    """Capture this type of page instead of the home page.

    Context.dev finds it among the domain's links, in 30 languages. Only with
    `domain`.
    """

    scroll_offset: Annotated[Optional[int], PropertyInfo(alias="scrollOffset")]
    """
    Return the viewport-sized slice of the full page that starts this many pixels
    from the top. Step by the viewport height, such as `0`, `1080`, `2160`, to walk
    a long page. The last slice can be shorter. Overrides `fullScreenshot`.
    """

    tags: SequenceNotStr[str]
    """Comma-separated labels for this request, such as `production,team-alpha`.

    Filter usage and request logs by them.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    viewport: Viewport
    """Browser viewport size in pixels."""

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """Time to wait after the page loads before capturing, in milliseconds.

    `0` waits 500 ms. `timeoutOpts.milliseconds` must be at least `waitForMs` plus
    10000 ms, or the request fails with `TIMEOUT_TOO_SHORT_FOR_WAIT`.
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
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial. `return-partial` requires at least 5000 ms. On `POST /web/scrape`, an
    output that is not ready in time fails with `REQUEST_TIMEOUT` inside a 200
    response under either behavior; 408 means the whole request could not respond by
    the deadline.
    """


class Viewport(TypedDict, total=False):
    """Browser viewport size in pixels."""

    height: int
    """Viewport height in pixels."""

    width: int
    """Viewport width in pixels."""
