# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebScreenshotParams", "Viewport"]


class WebScreenshotParams(TypedDict, total=False):
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

    handle_cookie_popup: Annotated[Literal["true", "false"], PropertyInfo(alias="handleCookiePopup")]
    """Optional parameter to control cookie/consent popup handling.

    If 'true', we dismiss cookie banner before capture. If 'false' or not provided,
    captures the page without that step.
    """

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
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

    scroll_offset: Annotated[int, PropertyInfo(alias="scrollOffset")]
    """
    Optional vertical scroll offset in pixels for capturing a long page in
    viewport-sized chunks. When provided, the full page is captured once and the
    returned image is the viewport-sized slice that begins at this Y offset (e.g.
    request scrollOffset=0, then 1080, then 2160 to walk a 1920x1080 landing page
    top to bottom). The final slice may be shorter than the viewport height. Takes
    precedence over fullScreenshot. Max: 100000.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    viewport: Viewport
    """Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before taking
    the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
    omitted.
    """


class Viewport(TypedDict, total=False):
    """Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080."""

    height: int
    """Viewport height in pixels."""

    width: int
    """Viewport width in pixels."""
