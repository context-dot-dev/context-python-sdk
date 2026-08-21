# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebExtractResponse", "Metadata", "MetadataActionsApplied", "KeyMetadata"]


class MetadataActionsApplied(BaseModel):
    instruction: str

    status: Literal["applied", "failed", "skipped"]
    """Applied means the requested page state was visibly verified.

    Failed means it was not verified. Skipped means it was not attempted.
    """

    completion_evidence: Optional[str] = FieldInfo(alias="completionEvidence", default=None)
    """Visible page evidence used to verify an applied action."""

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    error: Optional[str] = None

    method: Optional[str] = None

    target_description: Optional[str] = FieldInfo(alias="targetDescription", default=None)


class Metadata(BaseModel):
    max_crawl_depth: int = FieldInfo(alias="maxCrawlDepth")

    num_blocked: int = FieldInfo(alias="numBlocked")
    """
    Number of crawled pages excluded because they were anti-bot challenges, error
    pages, or parked-domain placeholders.
    """

    num_failed: int = FieldInfo(alias="numFailed")

    num_skipped: int = FieldInfo(alias="numSkipped")

    num_succeeded: int = FieldInfo(alias="numSucceeded")

    num_urls: int = FieldInfo(alias="numUrls")

    actions_applied: Optional[List[MetadataActionsApplied]] = FieldInfo(alias="actionsApplied", default=None)
    """One verified outcome per requested browser action, in request order."""


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class WebExtractResponse(BaseModel):
    data: Dict[str, object]
    """Extracted data matching the request schema"""

    metadata: Metadata

    status: str
    """Status of the response, e.g., 'ok'"""

    url: str
    """The starting URL that was analyzed"""

    urls_analyzed: List[str]
    """List of URLs whose Markdown was used for extraction"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
