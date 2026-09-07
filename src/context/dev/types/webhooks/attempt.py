# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Attempt", "Error"]


class Error(BaseModel):
    code: str

    message: str


class Attempt(BaseModel):
    id: str

    attempt: int

    completed_at: Optional[datetime] = None

    error: Optional[Error] = None

    http_status: Optional[int] = None

    started_at: datetime

    trigger: Literal["initial", "automatic", "manual"]

    url: str
