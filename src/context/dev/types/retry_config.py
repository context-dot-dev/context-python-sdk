# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RetryConfig"]


class RetryConfig(BaseModel):
    """Opt into durable webhook delivery.

    An empty object uses the default retry schedule. Omit retry to preserve legacy delivery behavior. The policy is snapshotted for each event.
    """

    delays_seconds: Optional[List[int]] = None
    """Wait in seconds after each failed attempt.

    The first attempt is immediate. At most 10 delays, each 1–86400 seconds,
    totaling at most 72 hours. Small jitter is added automatically. An empty array
    disables automatic retries; manual retries remain available.
    """
