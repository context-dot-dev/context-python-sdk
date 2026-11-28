# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import scholar_search_params
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
from ..types.scholar_search_response import ScholarSearchResponse

__all__ = ["ScholarResource", "AsyncScholarResource"]


class ScholarResource(SyncAPIResource):
    """Search full-text academic papers from arXiv and Europe PMC."""

    @cached_property
    def with_raw_response(self) -> ScholarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScholarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScholarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return ScholarResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        query: str,
        cursor: Optional[str] | Omit = omit,
        filter_by: scholar_search_params.FilterBy | Omit = omit,
        limit: int | Omit = omit,
        sort: Literal["relevance", "date_desc"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScholarSearchResponse:
        """
        Search the full text of papers from arXiv and Europe PMC by topic or question.
        Each result includes the matching passage and a direct link to the full text.
        Page through up to 250 matches, ranked by relevance or newest first.

        Args:
          query: Topic or question to search for. Append one `arxiv:`, `pmcid:`, `pmid:`, or
              `doi:` ID to search within that paper, such as `protein folding pmid:34265844`,
              or send the ID on its own.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          filter_by: Filter by publication date.

          limit: Maximum number of papers to return per page.

          sort: `relevance` puts the closest matches first; `date_desc` puts the newest papers
              first, with undated papers last. Both orders apply to the top 250 matches.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scholar/search",
            body=maybe_transform(
                {
                    "query": query,
                    "cursor": cursor,
                    "filter_by": filter_by,
                    "limit": limit,
                    "sort": sort,
                    "tags": tags,
                },
                scholar_search_params.ScholarSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScholarSearchResponse,
        )


class AsyncScholarResource(AsyncAPIResource):
    """Search full-text academic papers from arXiv and Europe PMC."""

    @cached_property
    def with_raw_response(self) -> AsyncScholarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScholarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScholarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncScholarResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        query: str,
        cursor: Optional[str] | Omit = omit,
        filter_by: scholar_search_params.FilterBy | Omit = omit,
        limit: int | Omit = omit,
        sort: Literal["relevance", "date_desc"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScholarSearchResponse:
        """
        Search the full text of papers from arXiv and Europe PMC by topic or question.
        Each result includes the matching passage and a direct link to the full text.
        Page through up to 250 matches, ranked by relevance or newest first.

        Args:
          query: Topic or question to search for. Append one `arxiv:`, `pmcid:`, `pmid:`, or
              `doi:` ID to search within that paper, such as `protein folding pmid:34265844`,
              or send the ID on its own.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          filter_by: Filter by publication date.

          limit: Maximum number of papers to return per page.

          sort: `relevance` puts the closest matches first; `date_desc` puts the newest papers
              first, with undated papers last. Both orders apply to the top 250 matches.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scholar/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "cursor": cursor,
                    "filter_by": filter_by,
                    "limit": limit,
                    "sort": sort,
                    "tags": tags,
                },
                scholar_search_params.ScholarSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScholarSearchResponse,
        )


class ScholarResourceWithRawResponse:
    def __init__(self, scholar: ScholarResource) -> None:
        self._scholar = scholar

        self.search = to_raw_response_wrapper(
            scholar.search,
        )


class AsyncScholarResourceWithRawResponse:
    def __init__(self, scholar: AsyncScholarResource) -> None:
        self._scholar = scholar

        self.search = async_to_raw_response_wrapper(
            scholar.search,
        )


class ScholarResourceWithStreamingResponse:
    def __init__(self, scholar: ScholarResource) -> None:
        self._scholar = scholar

        self.search = to_streamed_response_wrapper(
            scholar.search,
        )


class AsyncScholarResourceWithStreamingResponse:
    def __init__(self, scholar: AsyncScholarResource) -> None:
        self._scholar = scholar

        self.search = async_to_streamed_response_wrapper(
            scholar.search,
        )
