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
    name: str

    domain: Optional[str] = None


class MatchPersonEnrichmentCandidateMatchPersonEducationEndDate(BaseModel):
    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchPersonEnrichmentCandidateMatchPersonEducationStartDate(BaseModel):
    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchPersonEnrichmentCandidateMatchPersonEducation(BaseModel):
    institution: MatchPersonEnrichmentCandidateMatchPersonEducationInstitution

    degree: Optional[str] = None

    description: Optional[str] = None

    end_date: Optional[MatchPersonEnrichmentCandidateMatchPersonEducationEndDate] = None

    field_of_study: Optional[str] = None

    start_date: Optional[MatchPersonEnrichmentCandidateMatchPersonEducationStartDate] = None


class MatchPersonEnrichmentCandidateMatchPersonExperienceOrganization(BaseModel):
    name: str

    domain: Optional[str] = None


class MatchPersonEnrichmentCandidateMatchPersonExperienceEndDate(BaseModel):
    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchPersonEnrichmentCandidateMatchPersonExperienceStartDate(BaseModel):
    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchPersonEnrichmentCandidateMatchPersonExperience(BaseModel):
    organization: MatchPersonEnrichmentCandidateMatchPersonExperienceOrganization

    title: str

    description: Optional[str] = None

    end_date: Optional[MatchPersonEnrichmentCandidateMatchPersonExperienceEndDate] = None

    is_current: Optional[bool] = None

    location: Optional[str] = None

    start_date: Optional[MatchPersonEnrichmentCandidateMatchPersonExperienceStartDate] = None


class MatchPersonEnrichmentCandidateMatchPersonCurrentRoleOrganization(BaseModel):
    name: str

    domain: Optional[str] = None


class MatchPersonEnrichmentCandidateMatchPersonCurrentRoleEndDate(BaseModel):
    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchPersonEnrichmentCandidateMatchPersonCurrentRoleStartDate(BaseModel):
    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchPersonEnrichmentCandidateMatchPersonCurrentRole(BaseModel):
    organization: MatchPersonEnrichmentCandidateMatchPersonCurrentRoleOrganization

    title: str

    description: Optional[str] = None

    end_date: Optional[MatchPersonEnrichmentCandidateMatchPersonCurrentRoleEndDate] = None

    is_current: Optional[bool] = None

    location: Optional[str] = None

    start_date: Optional[MatchPersonEnrichmentCandidateMatchPersonCurrentRoleStartDate] = None


class MatchPersonEnrichmentCandidateMatchPersonLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    country_code: Optional[str] = None

    display: Optional[str] = None

    region: Optional[str] = None


class MatchPersonEnrichmentCandidateMatchPersonName(BaseModel):
    first: Optional[str] = None

    full: Optional[str] = None

    last: Optional[str] = None


class MatchPersonEnrichmentCandidateMatchPerson(BaseModel):
    current_role_status: Literal["present", "none", "unknown"]
    """Whether the person's current role is known.

    `present` — current_role is populated. `none` — the work history explicitly
    shows every role has ended. `unknown` — our data sources could not confirm
    either way; treat a missing current_role as unverified rather than vacant.
    """

    education: List[MatchPersonEnrichmentCandidateMatchPersonEducation]

    experience: List[MatchPersonEnrichmentCandidateMatchPersonExperience]

    skills: List[str]

    social_urls: List[str]

    website_urls: List[str]

    avatar_url: Optional[str] = None

    bio: Optional[str] = None

    checked_at: Optional[str] = None
    """When we last refreshed this profile from our data sources (ISO 8601)."""

    current_role: Optional[MatchPersonEnrichmentCandidateMatchPersonCurrentRole] = None

    email: Optional[str] = None

    last_updated: Optional[str] = None
    """When the underlying profile data last changed in our data sources (ISO 8601).

    Omitted when unknown.
    """

    location: Optional[MatchPersonEnrichmentCandidateMatchPersonLocation] = None

    name: Optional[MatchPersonEnrichmentCandidateMatchPersonName] = None


class MatchPersonEnrichmentCandidateMatch(BaseModel):
    """The highest-scoring person candidate."""

    person: MatchPersonEnrichmentCandidateMatchPerson

    score: int

    status: Literal["candidate"]


class MatchPersonEnrichmentNotFoundMatch(BaseModel):
    """No usable person candidate was found."""

    person: None = None

    score: None = None

    status: Literal["not_found"]


Match: TypeAlias = Annotated[
    Union[MatchPersonEnrichmentCandidateMatch, MatchPersonEnrichmentNotFoundMatch], PropertyInfo(discriminator="status")
]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class PersonEnrichResponse(BaseModel):
    match: Match
    """The highest-scoring person candidate."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
