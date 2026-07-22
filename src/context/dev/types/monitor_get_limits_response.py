# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorGetLimitsResponse"]


class MonitorGetLimitsResponse(BaseModel):
    monitors_limit: int
    """Maximum number of monitors allowed for the account.

    Defaults to the plan allowance unless a custom limit is set for the
    organization.
    """

    monitors_used: int
    """Number of monitors the account currently has."""

    plan: Literal["free", "starter", "pro", "scale"]
    """The plan tier the limit was resolved from."""
