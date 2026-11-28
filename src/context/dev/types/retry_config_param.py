# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["RetryConfigParam"]


class RetryConfigParam(TypedDict, total=False):
    """Automatic retry settings. Pass `{}` for the default schedule."""

    delays_seconds: Iterable[int]
    """Delay before each automatic retry, in seconds, totaling at most 72 hours.

    Pass `[]` to disable automatic retries.
    """
