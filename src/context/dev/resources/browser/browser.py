# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BrowserResource", "AsyncBrowserResource"]


class BrowserResource(SyncAPIResource):
    @cached_property
    def profiles(self) -> ProfilesResource:
        """See the authenticated browser profiles your organization created."""
        return ProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return BrowserResourceWithStreamingResponse(self)


class AsyncBrowserResource(AsyncAPIResource):
    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        """See the authenticated browser profiles your organization created."""
        return AsyncProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncBrowserResourceWithStreamingResponse(self)


class BrowserResourceWithRawResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        """See the authenticated browser profiles your organization created."""
        return ProfilesResourceWithRawResponse(self._browser.profiles)


class AsyncBrowserResourceWithRawResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        """See the authenticated browser profiles your organization created."""
        return AsyncProfilesResourceWithRawResponse(self._browser.profiles)


class BrowserResourceWithStreamingResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        """See the authenticated browser profiles your organization created."""
        return ProfilesResourceWithStreamingResponse(self._browser.profiles)


class AsyncBrowserResourceWithStreamingResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        """See the authenticated browser profiles your organization created."""
        return AsyncProfilesResourceWithStreamingResponse(self._browser.profiles)
