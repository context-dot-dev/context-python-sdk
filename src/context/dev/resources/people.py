# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import person_enrich_params
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

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
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
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonEnrichResponse:
        """
        Finds and normalizes the best available person candidate from additive identity
        clues, then assigns an identity match score from 0 to 100. Available on all paid
        plans. Successful requests cost 20 credits. Disposable and free email addresses
        (like gmail.com, yahoo.com) will throw a 422 error.

        Args:
          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

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
                    "timeout_ms": timeout_ms,
                },
                person_enrich_params.PersonEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonEnrichResponse,
        )


class AsyncPeopleResource(AsyncAPIResource):
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
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonEnrichResponse:
        """
        Finds and normalizes the best available person candidate from additive identity
        clues, then assigns an identity match score from 0 to 100. Available on all paid
        plans. Successful requests cost 20 credits. Disposable and free email addresses
        (like gmail.com, yahoo.com) will throw a 422 error.

        Args:
          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

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
                    "timeout_ms": timeout_ms,
                },
                person_enrich_params.PersonEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonEnrichResponse,
        )


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.enrich = to_raw_response_wrapper(
            people.enrich,
        )


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.enrich = async_to_raw_response_wrapper(
            people.enrich,
        )


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.enrich = to_streamed_response_wrapper(
            people.enrich,
        )


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.enrich = async_to_streamed_response_wrapper(
            people.enrich,
        )
