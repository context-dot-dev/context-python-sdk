# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "PersonEnrichResponse",
    "Match",
    "MatchPersonEnrichmentCandidateMatch",
    "MatchPersonEnrichmentCandidateMatchPerson",
    "MatchPersonEnrichmentCandidateMatchPersonEducation",
    "MatchPersonEnrichmentCandidateMatchPersonEducationInstitution",
    "MatchPersonEnrichmentCandidateMatchPersonEducationEndDate",
    "MatchPersonEnrichmentCandidateMatchPersonEducationStartDate",
    "MatchPersonEnrichmentCandidateMatchPersonExperience",
    "MatchPersonEnrichmentCandidateMatchPersonExperienceOrganization",
    "MatchPersonEnrichmentCandidateMatchPersonExperienceEndDate",
    "MatchPersonEnrichmentCandidateMatchPersonExperienceStartDate",
    "MatchPersonEnrichmentCandidateMatchPersonCurrentRole",
    "MatchPersonEnrichmentCandidateMatchPersonCurrentRoleOrganization",
    "MatchPersonEnrichmentCandidateMatchPersonCurrentRoleEndDate",
    "MatchPersonEnrichmentCandidateMatchPersonCurrentRoleStartDate",
    "MatchPersonEnrichmentCandidateMatchPersonLocation",
    "MatchPersonEnrichmentCandidateMatchPersonName",
    "MatchPersonEnrichmentNotFoundMatch",
    "KeyMetadata",
]


class MatchPersonEnrichmentCandidateMatchPersonEducationInstitution(BaseModel):
    """School or university."""

    name: str
    """Name of the organization."""

    domain: Optional[str] = None
    """Website domain of the organization. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonEducationEndDate(BaseModel):
    """When the studies ended."""

    year: int
    """Four-digit year."""

    day: Optional[int] = None
    """Day of the month. Omitted when unknown."""

    month: Optional[int] = None
    """Month. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonEducationStartDate(BaseModel):
    """When the studies started."""

    year: int
    """Four-digit year."""

    day: Optional[int] = None
    """Day of the month. Omitted when unknown."""

    month: Optional[int] = None
    """Month. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonEducation(BaseModel):
    institution: MatchPersonEnrichmentCandidateMatchPersonEducationInstitution
    """School or university."""

    degree: Optional[str] = None
    """Degree or qualification."""

    description: Optional[str] = None
    """Description of the studies."""

    end_date: Optional[MatchPersonEnrichmentCandidateMatchPersonEducationEndDate] = None
    """When the studies ended."""

    field_of_study: Optional[str] = None
    """Subject or major studied."""

    start_date: Optional[MatchPersonEnrichmentCandidateMatchPersonEducationStartDate] = None
    """When the studies started."""


class MatchPersonEnrichmentCandidateMatchPersonExperienceOrganization(BaseModel):
    """Employer for this role."""

    name: str
    """Name of the organization."""

    domain: Optional[str] = None
    """Website domain of the organization. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonExperienceEndDate(BaseModel):
    """When the role ended."""

    year: int
    """Four-digit year."""

    day: Optional[int] = None
    """Day of the month. Omitted when unknown."""

    month: Optional[int] = None
    """Month. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonExperienceStartDate(BaseModel):
    """When the role started."""

    year: int
    """Four-digit year."""

    day: Optional[int] = None
    """Day of the month. Omitted when unknown."""

    month: Optional[int] = None
    """Month. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonExperience(BaseModel):
    organization: MatchPersonEnrichmentCandidateMatchPersonExperienceOrganization
    """Employer for this role."""

    title: str
    """Job title."""

    description: Optional[str] = None
    """Description of the role."""

    end_date: Optional[MatchPersonEnrichmentCandidateMatchPersonExperienceEndDate] = None
    """When the role ended."""

    is_current: Optional[bool] = None
    """Whether the person still holds this role."""

    location: Optional[str] = None
    """Where the role is based."""

    start_date: Optional[MatchPersonEnrichmentCandidateMatchPersonExperienceStartDate] = None
    """When the role started."""


class MatchPersonEnrichmentCandidateMatchPersonCurrentRoleOrganization(BaseModel):
    """Employer for this role."""

    name: str
    """Name of the organization."""

    domain: Optional[str] = None
    """Website domain of the organization. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonCurrentRoleEndDate(BaseModel):
    """When the role ended."""

    year: int
    """Four-digit year."""

    day: Optional[int] = None
    """Day of the month. Omitted when unknown."""

    month: Optional[int] = None
    """Month. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonCurrentRoleStartDate(BaseModel):
    """When the role started."""

    year: int
    """Four-digit year."""

    day: Optional[int] = None
    """Day of the month. Omitted when unknown."""

    month: Optional[int] = None
    """Month. Omitted when unknown."""


class MatchPersonEnrichmentCandidateMatchPersonCurrentRole(BaseModel):
    """The person's current job. See `current_role_status` when it is missing."""

    organization: MatchPersonEnrichmentCandidateMatchPersonCurrentRoleOrganization
    """Employer for this role."""

    title: str
    """Job title."""

    description: Optional[str] = None
    """Description of the role."""

    end_date: Optional[MatchPersonEnrichmentCandidateMatchPersonCurrentRoleEndDate] = None
    """When the role ended."""

    is_current: Optional[bool] = None
    """Whether the person still holds this role."""

    location: Optional[str] = None
    """Where the role is based."""

    start_date: Optional[MatchPersonEnrichmentCandidateMatchPersonCurrentRoleStartDate] = None
    """When the role started."""


class MatchPersonEnrichmentCandidateMatchPersonLocation(BaseModel):
    """Where the person is based."""

    city: Optional[str] = None
    """City."""

    country: Optional[str] = None
    """Country name."""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code."""

    display: Optional[str] = None
    """Location as a single display string."""

    region: Optional[str] = None
    """State, province, or region."""


class MatchPersonEnrichmentCandidateMatchPersonName(BaseModel):
    """Name of the person."""

    first: Optional[str] = None
    """First or given name."""

    full: Optional[str] = None
    """Full name."""

    last: Optional[str] = None
    """Last or family name."""


class MatchPersonEnrichmentCandidateMatchPerson(BaseModel):
    """Profile of the matched person."""

    current_role_status: Literal["present", "none", "unknown"]
    """Whether the person's current role is known.

    `present` means `current_role` is filled in; `none` means the work history shows
    every role has ended; `unknown` means it could not be confirmed either way, so
    treat a missing `current_role` as unverified, not vacant.
    """

    education: List[MatchPersonEnrichmentCandidateMatchPersonEducation]
    """Education history."""

    experience: List[MatchPersonEnrichmentCandidateMatchPersonExperience]
    """Work history. Each entry has the same fields as `current_role`."""

    skills: List[str]
    """Professional skills."""

    social_urls: List[str]
    """Public profile URLs for the person."""

    website_urls: List[str]
    """Other websites associated with the person."""

    avatar_url: Optional[str] = None
    """URL of the hosted profile picture. Omitted with zero data retention."""

    bio: Optional[str] = None
    """Short bio from the person's profile."""

    checked_at: Optional[str] = None
    """
    When Context.dev last refreshed the profile from its sources, as an ISO 8601
    timestamp.
    """

    current_role: Optional[MatchPersonEnrichmentCandidateMatchPersonCurrentRole] = None
    """The person's current job. See `current_role_status` when it is missing."""

    email: Optional[str] = None
    """Email address of the person."""

    last_updated: Optional[str] = None
    """When the profile data last changed at its sources, as an ISO 8601 timestamp.

    Omitted when unknown.
    """

    location: Optional[MatchPersonEnrichmentCandidateMatchPersonLocation] = None
    """Where the person is based."""

    name: Optional[MatchPersonEnrichmentCandidateMatchPersonName] = None
    """Name of the person."""


class MatchPersonEnrichmentCandidateMatch(BaseModel):
    """The best-matching person, with an identity-match score."""

    person: MatchPersonEnrichmentCandidateMatchPerson
    """Profile of the matched person."""

    score: int
    """Identity-match score from 0 to 100.

    Higher is a stronger match; weak candidates are still returned.
    """

    status: Literal["candidate"]
    """Always `candidate` for a match."""


class MatchPersonEnrichmentNotFoundMatch(BaseModel):
    """No usable candidate was found."""

    person: None = None
    """Always `null`."""

    score: None = None
    """Always `null`."""

    status: Literal["not_found"]
    """Always `not_found` when no candidate exists."""


Match: TypeAlias = Annotated[
    Union[MatchPersonEnrichmentCandidateMatch, MatchPersonEnrichmentNotFoundMatch], PropertyInfo(discriminator="status")
]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class PersonEnrichResponse(BaseModel):
    match: Match
    """The best-matching person, with an identity-match score."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """`true` when the `timeoutOpts` deadline ended processing early.

    The response holds the data completed so far; unfinished fields are omitted.
    """
