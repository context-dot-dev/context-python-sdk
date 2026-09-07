# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["RetryConfigParam"]


class RetryConfigParam(TypedDict, total=False):
    """Opt into durable webhook delivery.

    An empty object uses the default retry schedule. Omit retry to preserve legacy delivery behavior. The policy is snapshotted for each event.
    """

    delays_seconds: Iterable[int]
    """Wait in seconds after each failed attempt.

    The first attempt is immediate. At most 10 delays, each 1–86400 seconds,
    totaling at most 72 hours. Small jitter is added automatically. An empty array
    disables automatic retries; manual retries remain available.
    """
