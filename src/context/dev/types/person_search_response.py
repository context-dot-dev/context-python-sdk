# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "PersonSearchResponse",
    "Result",
    "ResultLocation",
    "ResultRole",
    "ResultRoleCompany",
    "ResultMatch",
    "KeyMetadata",
]


class ResultLocation(BaseModel):
    """Where the person lives."""

    city: Optional[str] = None
    """City."""

    country_code: Optional[str] = None
    """Country as a two-letter code, such as US or GB."""

    region: Optional[str] = None
    """State or region."""


class ResultRoleCompany(BaseModel):
    """Current employer, when known."""

    domain: Optional[str] = None
    """The company’s website domain."""

    name: Optional[str] = None
    """Company name."""


class ResultRole(BaseModel):
    """The person’s current role."""

    company: Optional[ResultRoleCompany] = None
    """Current employer, when known."""

    functions: List[str]
    """Areas of responsibility."""

    seniority: Optional[str] = None
    """Seniority level."""

    started_on: Optional[str] = None
    """Role start date (YYYY-MM-DD)."""

    title: Optional[str] = None
    """Job title."""


class ResultMatch(BaseModel):
    """How well the person matches the query. Only returned in `ultra` mode."""

    confidence: float
    """How well the person matches the query, from 0 to 1."""


class Result(BaseModel):
    """A person matching your search; unavailable details are null or empty lists."""

    description: Optional[str] = None
    """What the person does."""

    is_founder: Optional[bool] = None
    """Whether the person is currently a founder or co-founder."""

    location: ResultLocation
    """Where the person lives."""

    name: Optional[str] = None
    """Full name."""

    profiles: List[str]
    """Public professional profile URLs."""

    role: ResultRole
    """The person’s current role."""

    schools: List[str]
    """Schools attended."""

    skills: List[str]
    """Professional skills."""

    years_of_experience: Optional[int] = None
    """Years of professional experience."""

    match: Optional[ResultMatch] = None
    """How well the person matches the query. Only returned in `ultra` mode."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class PersonSearchResponse(BaseModel):
    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    results: List[Result]
    """Up to 10 matching people, most relevant first."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    next_cursor: Optional[str] = None
    """Pass as cursor to fetch the next page; null when there are no more results."""
