# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import person_enrich_params, person_search_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.person_enrich_response import PersonEnrichResponse
from ..types.person_search_response import PersonSearchResponse

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
    """
    Enrich a person from identity clues, or find people with a natural-language query.
    """

    @cached_property
    def with_raw_response(self) -> PeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return PeopleResourceWithStreamingResponse(self)

    def enrich(
        self,
        *,
        company: person_enrich_params.Company | Omit = omit,
        education: Iterable[person_enrich_params.Education] | Omit = omit,
        email: str | Omit = omit,
        location: person_enrich_params.Location | Omit = omit,
        name: person_enrich_params.Name | Omit = omit,
        social_urls: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: person_enrich_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonEnrichResponse:
        """
        Match a person from a work email, a profile URL, or a name with company,
        education, or location context, and get their profile with an identity-match
        score from 0 to 100. The best candidate is returned even when the match is weak,
        so set a score threshold for your workflow. `not_found` results are free.

        Args:
          company: Company associated with the person. Send a `name`, a `domain`, or both.

          education: Education history to help distinguish people with similar names.

          email: Work email address of the person. Free and disposable email providers
              return 422.

          location: Location associated with the person. Send at least one of `city`, `region`, or
              `country`.

          name: Name of the person. Without an email or profile URL, send both `first` and
              `last` plus `company`, `education`, or `location`.

          social_urls: Public profile URLs for the person. A person-profile URL is enough to identify
              them without a name.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/people/enrich",
            body=maybe_transform(
                {
                    "company": company,
                    "education": education,
                    "email": email,
                    "location": location,
                    "name": name,
                    "social_urls": social_urls,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                person_enrich_params.PersonEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonEnrichResponse,
        )

    def search(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        filters: person_search_params.Filters | Omit = omit,
        mode: Literal["fast", "ultra"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonSearchResponse:
        """
        Find people from a plain-language description, such as
        `VPs of sales at solar companies in California`. Each result includes the
        current role and employer, location, years of experience, skills, schools, and
        public profile URLs. Pages with no matches are free.

        Args:
          query: Plain-language description of the people to find. Up to 500 characters in `fast`
              mode and 5000 in `ultra` mode.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page. Send the
              same `query`, `mode`, and `filters` with it.

          filters: Constraints every result must match, in addition to `query`.

          mode: `fast` matches people on basic criteria such as role, location, or background;
              `ultra` runs a deeper search, checks every candidate against each criterion in
              your query, and adds a `match` score. Complex `ultra` searches can take up to 30
              seconds, so set your client timeout to match.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/people/search",
            body=maybe_transform(
                {
                    "query": query,
                    "cursor": cursor,
                    "filters": filters,
                    "mode": mode,
                    "tags": tags,
                    "zdr": zdr,
                },
                person_search_params.PersonSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonSearchResponse,
        )


class AsyncPeopleResource(AsyncAPIResource):
    """
    Enrich a person from identity clues, or find people with a natural-language query.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncPeopleResourceWithStreamingResponse(self)

    async def enrich(
        self,
        *,
        company: person_enrich_params.Company | Omit = omit,
        education: Iterable[person_enrich_params.Education] | Omit = omit,
        email: str | Omit = omit,
        location: person_enrich_params.Location | Omit = omit,
        name: person_enrich_params.Name | Omit = omit,
        social_urls: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: person_enrich_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonEnrichResponse:
        """
        Match a person from a work email, a profile URL, or a name with company,
        education, or location context, and get their profile with an identity-match
        score from 0 to 100. The best candidate is returned even when the match is weak,
        so set a score threshold for your workflow. `not_found` results are free.

        Args:
          company: Company associated with the person. Send a `name`, a `domain`, or both.

          education: Education history to help distinguish people with similar names.

          email: Work email address of the person. Free and disposable email providers
              return 422.

          location: Location associated with the person. Send at least one of `city`, `region`, or
              `country`.

          name: Name of the person. Without an email or profile URL, send both `first` and
              `last` plus `company`, `education`, or `location`.

          social_urls: Public profile URLs for the person. A person-profile URL is enough to identify
              them without a name.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/people/enrich",
            body=await async_maybe_transform(
                {
                    "company": company,
                    "education": education,
                    "email": email,
                    "location": location,
                    "name": name,
                    "social_urls": social_urls,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                person_enrich_params.PersonEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonEnrichResponse,
        )

    async def search(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        filters: person_search_params.Filters | Omit = omit,
        mode: Literal["fast", "ultra"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonSearchResponse:
        """
        Find people from a plain-language description, such as
        `VPs of sales at solar companies in California`. Each result includes the
        current role and employer, location, years of experience, skills, schools, and
        public profile URLs. Pages with no matches are free.

        Args:
          query: Plain-language description of the people to find. Up to 500 characters in `fast`
              mode and 5000 in `ultra` mode.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page. Send the
              same `query`, `mode`, and `filters` with it.

          filters: Constraints every result must match, in addition to `query`.

          mode: `fast` matches people on basic criteria such as role, location, or background;
              `ultra` runs a deeper search, checks every candidate against each criterion in
              your query, and adds a `match` score. Complex `ultra` searches can take up to 30
              seconds, so set your client timeout to match.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/people/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "cursor": cursor,
                    "filters": filters,
                    "mode": mode,
                    "tags": tags,
                    "zdr": zdr,
                },
                person_search_params.PersonSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonSearchResponse,
        )


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.enrich = to_raw_response_wrapper(
            people.enrich,
        )
        self.search = to_raw_response_wrapper(
            people.search,
        )


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.enrich = async_to_raw_response_wrapper(
            people.enrich,
        )
        self.search = async_to_raw_response_wrapper(
            people.search,
        )


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.enrich = to_streamed_response_wrapper(
            people.enrich,
        )
        self.search = to_streamed_response_wrapper(
            people.search,
        )


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.enrich = async_to_streamed_response_wrapper(
            people.enrich,
        )
        self.search = async_to_streamed_response_wrapper(
            people.search,
        )
