# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MonitorRunResponse"]


class MonitorRunResponse(BaseModel):
    monitor_id: str

    queued: bool
