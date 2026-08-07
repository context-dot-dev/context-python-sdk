# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PersonEnrichParams", "Company", "Education", "EducationInstitution", "Location", "Name"]


class PersonEnrichParams(TypedDict, total=False):
    company: Company

    education: Iterable[Education]

    email: str

    location: Location

    name: Name

    social_urls: SequenceNotStr[str]

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
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
