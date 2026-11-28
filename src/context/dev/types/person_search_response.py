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
    """ISO 3166-1 alpha-2 country code, such as `US`."""

    region: Optional[str] = None
    """State or region."""


class ResultRoleCompany(BaseModel):
    """Current employer. `null` when unknown."""

    domain: Optional[str] = None
    """Website domain of the company."""

    name: Optional[str] = None
    """Company name."""


class ResultRole(BaseModel):
    """The person's current role."""

    company: Optional[ResultRoleCompany] = None
    """Current employer. `null` when unknown."""

    functions: List[str]
    """Areas of responsibility, such as `sales`."""

    seniority: Optional[str] = None
    """Seniority level, such as `executive`."""

    started_on: Optional[str] = None
    """When the role started, as `YYYY-MM-DD`."""

    title: Optional[str] = None
    """Job title."""


class ResultMatch(BaseModel):
    """How well the person matches the query. Returned only in `ultra` mode."""

    confidence: float
    """How well the person matches the query, from 0 to 1."""


class Result(BaseModel):
    """A person who matches your search. Unknown details are `null` or empty lists."""

    description: Optional[str] = None
    """What the person does."""

    is_founder: Optional[bool] = None
    """Whether the person is currently a founder or co-founder. `null` when unknown."""

    location: ResultLocation
    """Where the person lives."""

    name: Optional[str] = None
    """Full name."""

    profiles: List[str]
    """Public professional profile URLs.

    Send one to `POST /people/enrich` as `social_urls` for the full profile.
    """

    role: ResultRole
    """The person's current role."""

    schools: List[str]
    """Schools attended."""

    skills: List[str]
    """Professional skills."""

    years_of_experience: Optional[int] = None
    """Years of professional experience. `null` when unknown."""

    match: Optional[ResultMatch] = None
    """How well the person matches the query. Returned only in `ultra` mode."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


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
    """Pass as `cursor` to fetch the next page. `null` on the last page."""
