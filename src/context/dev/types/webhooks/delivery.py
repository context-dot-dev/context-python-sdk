# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .attempt import Attempt
from ..._models import BaseModel
from ..retry_config import RetryConfig

__all__ = ["Delivery", "LastAttempt", "LastError", "Source", "SourceUnionMember0", "SourceUnionMember1"]


class LastAttempt(Attempt):
    pass


class LastError(BaseModel):
    code: str

    message: str


class SourceUnionMember0(BaseModel):
    batch_id: str

    type: Literal["batch"]


class SourceUnionMember1(BaseModel):
    monitor_id: str

    run_id: str

    type: Literal["monitor"]


Source: TypeAlias = Union[SourceUnionMember0, SourceUnionMember1]


class Delivery(BaseModel):
    id: str

    attempt_count: int
    """Number of delivery attempts started, including any attempt in progress."""

    created_at: datetime

    delivered_at: Optional[datetime] = None
    """Most recent successful acknowledgment; retained if a later forced resend fails."""

    event: Literal["batch.completed", "batch.failed", "batch.cancelled", "change.detected", "run.completed"]

    event_id: str
    """Stable event ID.

    Unchanged across automatic and manual attempts; use it to deduplicate events.
    """

    last_attempt: LastAttempt

    last_error: Optional[LastError] = None

    next_attempt_at: Optional[datetime] = None

    retry: RetryConfig
    """Opt into durable webhook delivery.

    An empty object uses the default retry schedule. Omit retry to preserve legacy
    delivery behavior. The policy is snapshotted for each event.
    """

    retry_expires_at: datetime
    """Seven days after event creation.

    Manual retries after this time return 410. Delivery and attempt metadata remain
    available for up to 30 days.
    """

    source: Source

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]

    url: str
    """Destination recorded for this delivery.

    Each attempt records the URL it used. Monitor retries use the currently
    configured URL and signing secret.
    """
