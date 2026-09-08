# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RetryConfig"]


class RetryConfig(BaseModel):
    """Webhook retry settings. Use {} for the default schedule."""

    delays_seconds: Optional[List[int]] = None
    """Retry delays in seconds, totaling at most 72 hours.

    Use [] to disable automatic retries.
    """
