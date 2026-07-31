# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Failure"]


class Failure(BaseModel):
    """
    A failure of the batch as a whole, distinct from the per-page failures in `page_errors`.
    """

    code: str
    """Why the batch itself stopped."""

    message: str
    """Human-readable explanation."""
