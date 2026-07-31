# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BatchSubmitResponse",
    "Metadata",
    "MetadataIdentifiers",
    "Person",
    "PersonEducation",
    "PersonEducationInstitution",
    "PersonEducationDates",
    "PersonEducationDatesEndDate",
    "PersonEducationDatesStartDate",
    "PersonExperience",
    "PersonExperienceCompany",
    "PersonExperienceDates",
    "PersonExperienceDatesEndDate",
    "PersonExperienceDatesStartDate",
    "PersonProfile",
    "PersonSkill",
    "KeyMetadata",
]


class MetadataIdentifiers(BaseModel):
    """Identifiers returned for the person."""

    linkedin_url: Optional[str] = FieldInfo(alias="linkedinUrl", default=None)
    """LinkedIn profile URL."""


class Metadata(BaseModel):
    """Additional response details."""

    identifiers: MetadataIdentifiers
    """Identifiers returned for the person."""

    sources_attempted: List[Literal["linkedin", "cv", "manual", "github", "other"]] = FieldInfo(
        alias="sourcesAttempted"
    )
    """Source categories checked."""

    sources_succeeded: List[Literal["linkedin", "cv", "manual", "github", "other"]] = FieldInfo(
        alias="sourcesSucceeded"
    )
    """Source categories with data."""

    urls_analyzed: List[str] = FieldInfo(alias="urlsAnalyzed")
    """URLs reviewed for this profile."""

    personal_website_url: Optional[str] = FieldInfo(alias="personalWebsiteUrl", default=None)
    """Personal website URL, when found."""


class PersonEducationInstitution(BaseModel):
    """School or institution name."""

    display: str
    """Display name."""

    normalized: Optional[str] = None
    """Standardized name, when available."""


class PersonEducationDatesEndDate(BaseModel):
    """End date, when known."""

    year: int
    """Year value."""

    day: Optional[int] = None
    """Day value, when known."""

    month: Optional[int] = None
    """Month value, when known."""


class PersonEducationDatesStartDate(BaseModel):
    """Start date, when known."""

    year: int
    """Year value."""

    day: Optional[int] = None
    """Day value, when known."""

    month: Optional[int] = None
    """Month value, when known."""


class PersonEducationDates(BaseModel):
    """Education dates."""

    end_date: Optional[PersonEducationDatesEndDate] = FieldInfo(alias="endDate", default=None)
    """End date, when known."""

    is_current: Optional[bool] = FieldInfo(alias="isCurrent", default=None)
    """Whether the entry is current."""

    start_date: Optional[PersonEducationDatesStartDate] = FieldInfo(alias="startDate", default=None)
    """Start date, when known."""


class PersonEducation(BaseModel):
    institution: PersonEducationInstitution
    """School or institution name."""

    dates: Optional[PersonEducationDates] = None
    """Education dates."""

    description: Optional[str] = None
    """Additional education details."""

    field_of_study: Optional[str] = FieldInfo(alias="fieldOfStudy", default=None)
    """Area of study."""

    qualification: Optional[str] = None
    """Degree, certificate, or credential."""


class PersonExperienceCompany(BaseModel):
    """Company or organization name."""

    display: str
    """Display name."""

    normalized: Optional[str] = None
    """Standardized name, when available."""


class PersonExperienceDatesEndDate(BaseModel):
    """End date, when known."""

    year: int
    """Year value."""

    day: Optional[int] = None
    """Day value, when known."""

    month: Optional[int] = None
    """Month value, when known."""


class PersonExperienceDatesStartDate(BaseModel):
    """Start date, when known."""

    year: int
    """Year value."""

    day: Optional[int] = None
    """Day value, when known."""

    month: Optional[int] = None
    """Month value, when known."""


class PersonExperienceDates(BaseModel):
    """Role dates."""

    end_date: Optional[PersonExperienceDatesEndDate] = FieldInfo(alias="endDate", default=None)
    """End date, when known."""

    is_current: Optional[bool] = FieldInfo(alias="isCurrent", default=None)
    """Whether the entry is current."""

    start_date: Optional[PersonExperienceDatesStartDate] = FieldInfo(alias="startDate", default=None)
    """Start date, when known."""


class PersonExperience(BaseModel):
    company: PersonExperienceCompany
    """Company or organization name."""

    title: str
    """Role or job title."""

    dates: Optional[PersonExperienceDates] = None
    """Role dates."""

    description: Optional[str] = None
    """Role description."""


class PersonProfile(BaseModel):
    """Core profile details."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """Person's full name."""

    headline: Optional[str] = None
    """Short professional headline."""

    location: Optional[str] = None
    """Person's listed location."""

    profile_picture_url: Optional[str] = FieldInfo(alias="profilePictureUrl", default=None)
    """Profile image URL."""

    summary: Optional[str] = None
    """Brief profile summary."""


class PersonSkill(BaseModel):
    name: str
    """Skill name."""

    normalized: Optional[str] = None
    """Standardized skill name, when available."""

    proficiency: Optional[str] = None
    """Skill proficiency, when available."""


class Person(BaseModel):
    """Retrieved person profile."""

    education: List[PersonEducation]
    """Education history."""

    experience: List[PersonExperience]
    """Work history."""

    profile: PersonProfile
    """Core profile details."""

    skills: List[PersonSkill]
    """Listed skills."""


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class BatchSubmitResponse(BaseModel):
    code: Literal[200]
    """HTTP status code."""

    metadata: Metadata
    """Additional response details."""

    person: Person
    """Retrieved person profile."""

    status: Literal["ok"]
    """Response status."""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
