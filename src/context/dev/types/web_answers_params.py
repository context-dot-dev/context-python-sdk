# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebAnswersParams", "TimeoutOpts"]


class WebAnswersParams(TypedDict, total=False):
    task: Required[str]
    """What to research and answer, in plain language.

    Naming a domain in the task (for example "pricing on context.dev") makes the
    agent read that site before it searches.
    """

    json_format: Dict[str, object]
    """
    An example object with placeholder values (for example {"pricing_page_url": "",
    "plans": [{"name": "", "price": 0}]}). Object keys and value types are
    preserved; unknown values may be null. Empty arrays accept any JSON items.
    Defaults to {"result": ""}. Maximum 8 levels, 500 values, and 16000 characters.
    """

    mode: Literal["fast", "ultra"]
    """
    Research level: fast uses a smaller model and research budget for 10 credits;
    ultra uses deeper reasoning and research for 100 credits. Defaults to ultra.
    Only successful requests consume credits.
    """

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
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
    results.
    """
