# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["RetryConfigParam"]


class RetryConfigParam(TypedDict, total=False):
    """Webhook retry settings. Use {} for the default schedule."""

    delays_seconds: Iterable[int]
    """Retry delays in seconds, totaling at most 72 hours.

    Use [] to disable automatic retries.
    """
