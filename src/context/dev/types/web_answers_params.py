# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebAnswersParams"]


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

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """
