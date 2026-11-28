# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RetryConfig"]


class RetryConfig(BaseModel):
    """Automatic retry settings. Pass `{}` for the default schedule."""

    delays_seconds: Optional[List[int]] = None
    """Delay before each automatic retry, in seconds, totaling at most 72 hours.

    Pass `[]` to disable automatic retries.
    """
