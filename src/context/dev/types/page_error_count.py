# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PageErrorCount"]


class PageErrorCount(BaseModel):
    """Page failures sharing one error code."""

    code: str
    """Error code for these failures."""

    count: int
    """Pages that failed with this code."""
