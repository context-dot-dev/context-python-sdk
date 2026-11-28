# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PersonEnrichParams", "Company", "Education", "EducationInstitution", "Location", "Name", "TimeoutOpts"]


class PersonEnrichParams(TypedDict, total=False):
    company: Company
    """Company associated with the person. Send a `name`, a `domain`, or both."""

    education: Iterable[Education]
    """Education history to help distinguish people with similar names."""

    email: str
    """Work email address of the person.

    Free and disposable email providers return 422.
    """

    location: Location
    """Location associated with the person.

    Send at least one of `city`, `region`, or `country`.
    """

    name: Name
    """Name of the person.

    Without an email or profile URL, send both `first` and `last` plus `company`,
    `education`, or `location`.
    """

    social_urls: SequenceNotStr[str]
    """Public profile URLs for the person.

    A person-profile URL is enough to identify them without a name.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Company(TypedDict, total=False):
    """Company associated with the person. Send a `name`, a `domain`, or both."""

    domain: str
    """Website domain of a company associated with the person."""

    name: str
    """Name of a company associated with the person."""


class EducationInstitution(TypedDict, total=False):
    """School or university, identified by name or domain."""

    domain: str
    """Website domain of the school or university."""

    name: str
    """Name of the school or university."""


class Education(TypedDict, total=False):
    degree: str
    """Degree or qualification earned."""

    field_of_study: str
    """Subject or major studied."""

    graduation_year: int
    """Four-digit graduation year."""

    institution: EducationInstitution
    """School or university, identified by name or domain."""


class Location(TypedDict, total=False):
    """Location associated with the person.

    Send at least one of `city`, `region`, or `country`.
    """

    city: str
    """City associated with the person."""

    country: str
    """Country associated with the person."""

    region: str
    """State, province, or region associated with the person."""


class Name(TypedDict, total=False):
    """Name of the person.

    Without an email or profile URL, send both `first` and `last` plus `company`, `education`, or `location`.
    """

    first: str
    """First or given name."""

    last: str
    """Last or family name."""


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """
