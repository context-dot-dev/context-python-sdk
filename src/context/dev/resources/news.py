# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import news_search_params
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
from ..types.news_search_response import NewsSearchResponse

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    """Search live first-party RSS and free historical news data by company identity."""

    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return NewsResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        search_by: news_search_params.SearchBy,
        cursor: Optional[str] | Omit = omit,
        filter_by: news_search_params.FilterBy | Omit = omit,
        limit: int | Omit = omit,
        sort_by: news_search_params.SortBy | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsSearchResponse:
        """
        Searches live and historical company news for one company, identified in
        searchBy by name, domain, ticker (optionally disambiguated by exchange), or
        ISIN. Results can be filtered by publisher domain, publisher country, article
        language, article type, and published-at date, and include stable story IDs,
        source metadata, verified entity relevance, and cursor pagination.

        Args:
          search_by: What to search for.

          cursor: Opaque next_cursor from the previous response, or null for the first page.

          filter_by: Optional result filters.

          limit: Maximum results to return. Defaults to 10.

          sort_by: Result ordering. Defaults to newest.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/news/search",
            body=maybe_transform(
                {
                    "search_by": search_by,
                    "cursor": cursor,
                    "filter_by": filter_by,
                    "limit": limit,
                    "sort_by": sort_by,
                    "tags": tags,
                },
                news_search_params.NewsSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsSearchResponse,
        )


class AsyncNewsResource(AsyncAPIResource):
    """Search live first-party RSS and free historical news data by company identity."""

    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncNewsResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        search_by: news_search_params.SearchBy,
        cursor: Optional[str] | Omit = omit,
        filter_by: news_search_params.FilterBy | Omit = omit,
        limit: int | Omit = omit,
        sort_by: news_search_params.SortBy | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsSearchResponse:
        """
        Searches live and historical company news for one company, identified in
        searchBy by name, domain, ticker (optionally disambiguated by exchange), or
        ISIN. Results can be filtered by publisher domain, publisher country, article
        language, article type, and published-at date, and include stable story IDs,
        source metadata, verified entity relevance, and cursor pagination.

        Args:
          search_by: What to search for.

          cursor: Opaque next_cursor from the previous response, or null for the first page.

          filter_by: Optional result filters.

          limit: Maximum results to return. Defaults to 10.

          sort_by: Result ordering. Defaults to newest.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/news/search",
            body=await async_maybe_transform(
                {
                    "search_by": search_by,
                    "cursor": cursor,
                    "filter_by": filter_by,
                    "limit": limit,
                    "sort_by": sort_by,
                    "tags": tags,
                },
                news_search_params.NewsSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsSearchResponse,
        )


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.search = to_raw_response_wrapper(
            news.search,
        )


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.search = async_to_raw_response_wrapper(
            news.search,
        )


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.search = to_streamed_response_wrapper(
            news.search,
        )


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.search = async_to_streamed_response_wrapper(
            news.search,
        )
