# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PersonEnrichParams", "Company", "Education", "EducationInstitution", "Location", "Name", "TimeoutOpts"]


class PersonEnrichParams(TypedDict, total=False):
    company: Company

    education: Iterable[Education]

    email: str

    location: Location

    name: Name

    social_urls: SequenceNotStr[str]

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """


class Company(TypedDict, total=False):
    domain: str

    name: str


class EducationInstitution(TypedDict, total=False):
    domain: str

    name: str


class Education(TypedDict, total=False):
    degree: str

    field_of_study: str

    graduation_year: int

    institution: EducationInstitution


class Location(TypedDict, total=False):
    city: str

    country: str

    region: str


class Name(TypedDict, total=False):
    first: str

    last: str


class TimeoutOpts(TypedDict, total=False):
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded timeoutOpts object.
    """

    milliseconds: Required[int]
    """Request deadline in milliseconds. Maximum: 300000 (5 minutes)."""

    behavior: Literal["fail", "return-partial"]
    """What to do at the deadline.

    "fail" returns 408 REQUEST_TIMEOUT without charging credits. "return-partial"
    returns usable results collected so far; if none are available, the request
    still fails without charging credits. Partial results are not cached as complete
    results.
    """
