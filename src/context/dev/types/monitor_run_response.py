# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MonitorRunResponse"]


class MonitorRunResponse(BaseModel):
    monitor_id: str

    queued: bool

    run_id: str
    """The queued run.

    Poll GET /monitors/{monitor_id}/runs or use it to correlate results.
    """
