# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Error"]


class Error(BaseModel):
    """Why the batch failed."""

    code: str
    """Batch error code."""

    message: str
    """Batch error message."""
