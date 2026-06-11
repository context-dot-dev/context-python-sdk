# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from .._models import BaseModel

__all__ = ["AIAIQueryResponse", "DataExtracted", "KeyMetadata"]


class DataExtracted(BaseModel):
    datapoint_name: Optional[str] = None
    """Name of the extracted data point"""

    datapoint_value: Union[str, float, bool, List[str], List[float], List[object], None] = None
    """Value of the extracted data point.

    Can be a primitive type, an array of primitives, or an array of objects when
    datapoint_list_type is 'object'.
    """


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class AIAIQueryResponse(BaseModel):
    data_extracted: Optional[List[DataExtracted]] = None
    """Array of extracted data points"""

    domain: Optional[str] = None
    """The domain that was analyzed"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""

    urls_analyzed: Optional[List[str]] = None
    """List of URLs that were analyzed"""
