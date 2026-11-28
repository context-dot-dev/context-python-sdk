# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Failure"]


class Failure(BaseModel):
    """Why the batch as a whole failed.

    Individual page failures are counted in `page_errors`.
    """

    code: str
    """Machine-readable failure code, such as `stalled` or `USAGE_EXCEEDED`."""

    message: str
    """Human-readable explanation of the failure."""
