# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    monitor_list_params,
    monitor_create_params,
    monitor_update_params,
    monitor_list_runs_params,
    monitor_list_changes_params,
    monitor_get_credit_usage_params,
    monitor_list_account_runs_params,
    monitor_list_account_changes_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.monitor_run_response import MonitorRunResponse
from ..types.monitor_list_response import MonitorListResponse
from ..types.monitor_create_response import MonitorCreateResponse
from ..types.monitor_delete_response import MonitorDeleteResponse
from ..types.monitor_update_response import MonitorUpdateResponse
from ..types.monitor_retrieve_response import MonitorRetrieveResponse
from ..types.monitor_list_runs_response import MonitorListRunsResponse
from ..types.monitor_get_limits_response import MonitorGetLimitsResponse
from ..types.monitor_list_changes_response import MonitorListChangesResponse
from ..types.monitor_retrieve_change_response import MonitorRetrieveChangeResponse
from ..types.monitor_get_credit_usage_response import MonitorGetCreditUsageResponse
from ..types.monitor_list_account_runs_response import MonitorListAccountRunsResponse
from ..types.monitor_list_account_changes_response import MonitorListAccountChangesResponse

__all__ = ["MonitorsResource", "AsyncMonitorsResource"]


class MonitorsResource(SyncAPIResource):
    """
    Monitor pages, sitemaps, and extracted website data for exact or semantic changes. Webhook payloads are documented by the MonitorsChangeDetectedWebhookPayload and MonitorsRunCompletedWebhookPayload schemas.
    """

    @cached_property
    def with_raw_response(self) -> MonitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return MonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return MonitorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        target: monitor_create_params.Target,
        change_detection: monitor_create_params.ChangeDetection | Omit = omit,
        mode: Literal["web"] | Omit = omit,
        schedule: monitor_create_params.Schedule | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook: Optional[monitor_create_params.Webhook] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorCreateResponse:
        """Creates a monitor.

        The request body is a union of the supported target/change
        detection combinations. The monitor runs immediately after creation to create
        its initial baseline.

        Args:
          target: Discriminated union describing what the monitor watches.

          change_detection: Discriminated union describing how changes are detected.

          mode: Top-level monitor category. Always `web` today; the concrete behavior is
              described by `target` and `change_detection`.

          schedule: Run the monitor on a fixed interval defined by a frequency and a unit, e.g.
              every 6 hours or every 2 days. The total interval (frequency × unit) must be
              between 10 minutes and 1 year.

          tags: User-defined tags for grouping and filtering monitors and their changes.
              Duplicates are removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/monitors",
            body=maybe_transform(
                {
                    "name": name,
                    "target": target,
                    "change_detection": change_detection,
                    "mode": mode,
                    "schedule": schedule,
                    "tags": tags,
                    "webhook": webhook,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateResponse,
        )

    def retrieve(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRetrieveResponse:
        """
        Get a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._get(
            path_template("/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRetrieveResponse,
        )

    def update(
        self,
        monitor_id: str,
        *,
        change_detection: monitor_update_params.ChangeDetection | Omit = omit,
        name: str | Omit = omit,
        schedule: monitor_update_params.Schedule | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target: monitor_update_params.Target | Omit = omit,
        webhook: Optional[monitor_update_params.Webhook] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorUpdateResponse:
        """Updates a monitor.

        If `target` or `change_detection` changes, the monitor
        creates a new baseline. Unsupported target/change detection combinations are
        rejected.

        Args:
          change_detection: Discriminated union describing how changes are detected.

          schedule: Run the monitor on a fixed interval defined by a frequency and a unit, e.g.
              every 6 hours or every 2 days. The total interval (frequency × unit) must be
              between 10 minutes and 1 year.

          tags: User-defined tags for grouping and filtering monitors and their changes.
              Duplicates are removed.

          target: Discriminated union describing what the monitor watches.

          webhook: Set to null to remove the webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._patch(
            path_template("/monitors/{monitor_id}", monitor_id=monitor_id),
            body=maybe_transform(
                {
                    "change_detection": change_detection,
                    "name": name,
                    "schedule": schedule,
                    "status": status,
                    "tags": tags,
                    "target": target,
                    "webhook": webhook,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorUpdateResponse,
        )

    def list(
        self,
        *,
        change_detection_type: Literal["exact", "semantic"] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        search_by: Optional[List[Literal["name", "url", "instructions", "tags"]]] | Omit = omit,
        search_type: Literal["exact", "prefix"] | Omit = omit,
        status: Literal["active", "paused", "failed"] | Omit = omit,
        tag: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_type: Literal["page", "sitemap", "extract"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """Lists monitors for the authenticated organization.

        Supports free-text search
        (`q` over `search_by` fields, `prefix` or `exact` via `search_type`) plus
        status/type/tag filters. Results are paginated via the opaque `cursor`.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          q: Free-text search term, matched against the fields named in `search_by`.

          search_by: Comma-separated fields to search with `q`. Defaults to all of them. Note
              `instructions` only exists on extract monitors.

          search_type: `prefix` for as-you-type prefix matching (default), `exact` for full-token
              matching.

          status: Filter monitors by lifecycle status.

          tag: Filter to items that have this tag.

          tags: Comma-separated list of tags to filter by (matches monitors having any of them).

          target_type: Filter by target type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "change_detection_type": change_detection_type,
                        "cursor": cursor,
                        "limit": limit,
                        "q": q,
                        "search_by": search_by,
                        "search_type": search_type,
                        "status": status,
                        "tag": tag,
                        "tags": tags,
                        "target_type": target_type,
                    },
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=MonitorListResponse,
        )

    def delete(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorDeleteResponse:
        """
        Delete a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._delete(
            path_template("/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorDeleteResponse,
        )

    def get_credit_usage(
        self,
        *,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGetCreditUsageResponse:
        """
        Returns credits charged per monitor over an optional [since, until] window,
        newest spenders first.

        Args:
          since: Only include items at or after this ISO 8601 timestamp.

          until: Only include items before this ISO 8601 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/monitors/credit-usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "since": since,
                        "until": until,
                    },
                    monitor_get_credit_usage_params.MonitorGetCreditUsageParams,
                ),
            ),
            cast_to=MonitorGetCreditUsageResponse,
        )

    def get_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGetLimitsResponse:
        """Returns how many monitors the account has and the maximum it allows."""
        return self._get(
            "/monitors/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorGetLimitsResponse,
        )

    def list_account_changes(
        self,
        *,
        change_detection_type: Literal["exact", "semantic"] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        monitor_id: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        tag: str | Omit = omit,
        target_type: Literal["page", "sitemap", "extract"] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListAccountChangesResponse:
        """
        Returns an account-wide feed of detected changes across monitors.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          monitor_id: Filter changes to a single monitor.

          since: Only include items at or after this ISO 8601 timestamp.

          tag: Filter to items that have this tag.

          target_type: Filter by target type.

          until: Only include items before this ISO 8601 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/monitors/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "change_detection_type": change_detection_type,
                        "cursor": cursor,
                        "limit": limit,
                        "monitor_id": monitor_id,
                        "since": since,
                        "tag": tag,
                        "target_type": target_type,
                        "until": until,
                    },
                    monitor_list_account_changes_params.MonitorListAccountChangesParams,
                ),
            ),
            cast_to=MonitorListAccountChangesResponse,
        )

    def list_account_runs(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "running", "completed", "failed", "skipped"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListAccountRunsResponse:
        """
        Returns an account-wide feed of monitor runs across all monitors.

        Args:
          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          status: Filter runs by lifecycle status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/monitors/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    monitor_list_account_runs_params.MonitorListAccountRunsParams,
                ),
            ),
            cast_to=MonitorListAccountRunsResponse,
        )

    def list_changes(
        self,
        monitor_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        tag: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListChangesResponse:
        """
        List changes for a monitor

        Args:
          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          since: Only include items at or after this ISO 8601 timestamp.

          tag: Filter to items that have this tag.

          until: Only include items before this ISO 8601 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._get(
            path_template("/monitors/{monitor_id}/changes", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "since": since,
                        "tag": tag,
                        "until": until,
                    },
                    monitor_list_changes_params.MonitorListChangesParams,
                ),
            ),
            cast_to=MonitorListChangesResponse,
        )

    def list_runs(
        self,
        monitor_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "running", "completed", "failed", "skipped"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListRunsResponse:
        """
        List monitor runs

        Args:
          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          status: Filter runs by lifecycle status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._get(
            path_template("/monitors/{monitor_id}/runs", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    monitor_list_runs_params.MonitorListRunsParams,
                ),
            ),
            cast_to=MonitorListRunsResponse,
        )

    def retrieve_change(
        self,
        change_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRetrieveChangeResponse:
        """
        Get a change

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not change_id:
            raise ValueError(f"Expected a non-empty value for `change_id` but received {change_id!r}")
        return self._get(
            path_template("/monitors/changes/{change_id}", change_id=change_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRetrieveChangeResponse,
        )

    def run(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRunResponse:
        """Triggers an immediate run of the monitor outside its normal schedule.

        The run is
        queued and processed asynchronously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._post(
            path_template("/monitors/{monitor_id}/run", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRunResponse,
        )


class AsyncMonitorsResource(AsyncAPIResource):
    """
    Monitor pages, sitemaps, and extracted website data for exact or semantic changes. Webhook payloads are documented by the MonitorsChangeDetectedWebhookPayload and MonitorsRunCompletedWebhookPayload schemas.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMonitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncMonitorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        target: monitor_create_params.Target,
        change_detection: monitor_create_params.ChangeDetection | Omit = omit,
        mode: Literal["web"] | Omit = omit,
        schedule: monitor_create_params.Schedule | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook: Optional[monitor_create_params.Webhook] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorCreateResponse:
        """Creates a monitor.

        The request body is a union of the supported target/change
        detection combinations. The monitor runs immediately after creation to create
        its initial baseline.

        Args:
          target: Discriminated union describing what the monitor watches.

          change_detection: Discriminated union describing how changes are detected.

          mode: Top-level monitor category. Always `web` today; the concrete behavior is
              described by `target` and `change_detection`.

          schedule: Run the monitor on a fixed interval defined by a frequency and a unit, e.g.
              every 6 hours or every 2 days. The total interval (frequency × unit) must be
              between 10 minutes and 1 year.

          tags: User-defined tags for grouping and filtering monitors and their changes.
              Duplicates are removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/monitors",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "target": target,
                    "change_detection": change_detection,
                    "mode": mode,
                    "schedule": schedule,
                    "tags": tags,
                    "webhook": webhook,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateResponse,
        )

    async def retrieve(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRetrieveResponse:
        """
        Get a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._get(
            path_template("/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRetrieveResponse,
        )

    async def update(
        self,
        monitor_id: str,
        *,
        change_detection: monitor_update_params.ChangeDetection | Omit = omit,
        name: str | Omit = omit,
        schedule: monitor_update_params.Schedule | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target: monitor_update_params.Target | Omit = omit,
        webhook: Optional[monitor_update_params.Webhook] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorUpdateResponse:
        """Updates a monitor.

        If `target` or `change_detection` changes, the monitor
        creates a new baseline. Unsupported target/change detection combinations are
        rejected.

        Args:
          change_detection: Discriminated union describing how changes are detected.

          schedule: Run the monitor on a fixed interval defined by a frequency and a unit, e.g.
              every 6 hours or every 2 days. The total interval (frequency × unit) must be
              between 10 minutes and 1 year.

          tags: User-defined tags for grouping and filtering monitors and their changes.
              Duplicates are removed.

          target: Discriminated union describing what the monitor watches.

          webhook: Set to null to remove the webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._patch(
            path_template("/monitors/{monitor_id}", monitor_id=monitor_id),
            body=await async_maybe_transform(
                {
                    "change_detection": change_detection,
                    "name": name,
                    "schedule": schedule,
                    "status": status,
                    "tags": tags,
                    "target": target,
                    "webhook": webhook,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorUpdateResponse,
        )

    async def list(
        self,
        *,
        change_detection_type: Literal["exact", "semantic"] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        search_by: Optional[List[Literal["name", "url", "instructions", "tags"]]] | Omit = omit,
        search_type: Literal["exact", "prefix"] | Omit = omit,
        status: Literal["active", "paused", "failed"] | Omit = omit,
        tag: str | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_type: Literal["page", "sitemap", "extract"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """Lists monitors for the authenticated organization.

        Supports free-text search
        (`q` over `search_by` fields, `prefix` or `exact` via `search_type`) plus
        status/type/tag filters. Results are paginated via the opaque `cursor`.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          q: Free-text search term, matched against the fields named in `search_by`.

          search_by: Comma-separated fields to search with `q`. Defaults to all of them. Note
              `instructions` only exists on extract monitors.

          search_type: `prefix` for as-you-type prefix matching (default), `exact` for full-token
              matching.

          status: Filter monitors by lifecycle status.

          tag: Filter to items that have this tag.

          tags: Comma-separated list of tags to filter by (matches monitors having any of them).

          target_type: Filter by target type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "change_detection_type": change_detection_type,
                        "cursor": cursor,
                        "limit": limit,
                        "q": q,
                        "search_by": search_by,
                        "search_type": search_type,
                        "status": status,
                        "tag": tag,
                        "tags": tags,
                        "target_type": target_type,
                    },
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=MonitorListResponse,
        )

    async def delete(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorDeleteResponse:
        """
        Delete a monitor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._delete(
            path_template("/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorDeleteResponse,
        )

    async def get_credit_usage(
        self,
        *,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGetCreditUsageResponse:
        """
        Returns credits charged per monitor over an optional [since, until] window,
        newest spenders first.

        Args:
          since: Only include items at or after this ISO 8601 timestamp.

          until: Only include items before this ISO 8601 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/monitors/credit-usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "since": since,
                        "until": until,
                    },
                    monitor_get_credit_usage_params.MonitorGetCreditUsageParams,
                ),
            ),
            cast_to=MonitorGetCreditUsageResponse,
        )

    async def get_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGetLimitsResponse:
        """Returns how many monitors the account has and the maximum it allows."""
        return await self._get(
            "/monitors/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorGetLimitsResponse,
        )

    async def list_account_changes(
        self,
        *,
        change_detection_type: Literal["exact", "semantic"] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        monitor_id: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        tag: str | Omit = omit,
        target_type: Literal["page", "sitemap", "extract"] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListAccountChangesResponse:
        """
        Returns an account-wide feed of detected changes across monitors.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          monitor_id: Filter changes to a single monitor.

          since: Only include items at or after this ISO 8601 timestamp.

          tag: Filter to items that have this tag.

          target_type: Filter by target type.

          until: Only include items before this ISO 8601 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/monitors/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "change_detection_type": change_detection_type,
                        "cursor": cursor,
                        "limit": limit,
                        "monitor_id": monitor_id,
                        "since": since,
                        "tag": tag,
                        "target_type": target_type,
                        "until": until,
                    },
                    monitor_list_account_changes_params.MonitorListAccountChangesParams,
                ),
            ),
            cast_to=MonitorListAccountChangesResponse,
        )

    async def list_account_runs(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "running", "completed", "failed", "skipped"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListAccountRunsResponse:
        """
        Returns an account-wide feed of monitor runs across all monitors.

        Args:
          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          status: Filter runs by lifecycle status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/monitors/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    monitor_list_account_runs_params.MonitorListAccountRunsParams,
                ),
            ),
            cast_to=MonitorListAccountRunsResponse,
        )

    async def list_changes(
        self,
        monitor_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        tag: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListChangesResponse:
        """
        List changes for a monitor

        Args:
          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          since: Only include items at or after this ISO 8601 timestamp.

          tag: Filter to items that have this tag.

          until: Only include items before this ISO 8601 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._get(
            path_template("/monitors/{monitor_id}/changes", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "since": since,
                        "tag": tag,
                        "until": until,
                    },
                    monitor_list_changes_params.MonitorListChangesParams,
                ),
            ),
            cast_to=MonitorListChangesResponse,
        )

    async def list_runs(
        self,
        monitor_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["queued", "running", "completed", "failed", "skipped"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListRunsResponse:
        """
        List monitor runs

        Args:
          cursor: Opaque pagination cursor from a previous response.

          limit: Maximum number of items to return per page (1-100). Defaults to 25.

          status: Filter runs by lifecycle status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._get(
            path_template("/monitors/{monitor_id}/runs", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    monitor_list_runs_params.MonitorListRunsParams,
                ),
            ),
            cast_to=MonitorListRunsResponse,
        )

    async def retrieve_change(
        self,
        change_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRetrieveChangeResponse:
        """
        Get a change

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not change_id:
            raise ValueError(f"Expected a non-empty value for `change_id` but received {change_id!r}")
        return await self._get(
            path_template("/monitors/changes/{change_id}", change_id=change_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRetrieveChangeResponse,
        )

    async def run(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRunResponse:
        """Triggers an immediate run of the monitor outside its normal schedule.

        The run is
        queued and processed asynchronously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._post(
            path_template("/monitors/{monitor_id}/run", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRunResponse,
        )


class MonitorsResourceWithRawResponse:
    def __init__(self, monitors: MonitorsResource) -> None:
        self._monitors = monitors

        self.create = to_raw_response_wrapper(
            monitors.create,
        )
        self.retrieve = to_raw_response_wrapper(
            monitors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            monitors.update,
        )
        self.list = to_raw_response_wrapper(
            monitors.list,
        )
        self.delete = to_raw_response_wrapper(
            monitors.delete,
        )
        self.get_credit_usage = to_raw_response_wrapper(
            monitors.get_credit_usage,
        )
        self.get_limits = to_raw_response_wrapper(
            monitors.get_limits,
        )
        self.list_account_changes = to_raw_response_wrapper(
            monitors.list_account_changes,
        )
        self.list_account_runs = to_raw_response_wrapper(
            monitors.list_account_runs,
        )
        self.list_changes = to_raw_response_wrapper(
            monitors.list_changes,
        )
        self.list_runs = to_raw_response_wrapper(
            monitors.list_runs,
        )
        self.retrieve_change = to_raw_response_wrapper(
            monitors.retrieve_change,
        )
        self.run = to_raw_response_wrapper(
            monitors.run,
        )


class AsyncMonitorsResourceWithRawResponse:
    def __init__(self, monitors: AsyncMonitorsResource) -> None:
        self._monitors = monitors

        self.create = async_to_raw_response_wrapper(
            monitors.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            monitors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            monitors.update,
        )
        self.list = async_to_raw_response_wrapper(
            monitors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            monitors.delete,
        )
        self.get_credit_usage = async_to_raw_response_wrapper(
            monitors.get_credit_usage,
        )
        self.get_limits = async_to_raw_response_wrapper(
            monitors.get_limits,
        )
        self.list_account_changes = async_to_raw_response_wrapper(
            monitors.list_account_changes,
        )
        self.list_account_runs = async_to_raw_response_wrapper(
            monitors.list_account_runs,
        )
        self.list_changes = async_to_raw_response_wrapper(
            monitors.list_changes,
        )
        self.list_runs = async_to_raw_response_wrapper(
            monitors.list_runs,
        )
        self.retrieve_change = async_to_raw_response_wrapper(
            monitors.retrieve_change,
        )
        self.run = async_to_raw_response_wrapper(
            monitors.run,
        )


class MonitorsResourceWithStreamingResponse:
    def __init__(self, monitors: MonitorsResource) -> None:
        self._monitors = monitors

        self.create = to_streamed_response_wrapper(
            monitors.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            monitors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            monitors.update,
        )
        self.list = to_streamed_response_wrapper(
            monitors.list,
        )
        self.delete = to_streamed_response_wrapper(
            monitors.delete,
        )
        self.get_credit_usage = to_streamed_response_wrapper(
            monitors.get_credit_usage,
        )
        self.get_limits = to_streamed_response_wrapper(
            monitors.get_limits,
        )
        self.list_account_changes = to_streamed_response_wrapper(
            monitors.list_account_changes,
        )
        self.list_account_runs = to_streamed_response_wrapper(
            monitors.list_account_runs,
        )
        self.list_changes = to_streamed_response_wrapper(
            monitors.list_changes,
        )
        self.list_runs = to_streamed_response_wrapper(
            monitors.list_runs,
        )
        self.retrieve_change = to_streamed_response_wrapper(
            monitors.retrieve_change,
        )
        self.run = to_streamed_response_wrapper(
            monitors.run,
        )


class AsyncMonitorsResourceWithStreamingResponse:
    def __init__(self, monitors: AsyncMonitorsResource) -> None:
        self._monitors = monitors

        self.create = async_to_streamed_response_wrapper(
            monitors.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            monitors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            monitors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            monitors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            monitors.delete,
        )
        self.get_credit_usage = async_to_streamed_response_wrapper(
            monitors.get_credit_usage,
        )
        self.get_limits = async_to_streamed_response_wrapper(
            monitors.get_limits,
        )
        self.list_account_changes = async_to_streamed_response_wrapper(
            monitors.list_account_changes,
        )
        self.list_account_runs = async_to_streamed_response_wrapper(
            monitors.list_account_runs,
        )
        self.list_changes = async_to_streamed_response_wrapper(
            monitors.list_changes,
        )
        self.list_runs = async_to_streamed_response_wrapper(
            monitors.list_runs,
        )
        self.retrieve_change = async_to_streamed_response_wrapper(
            monitors.retrieve_change,
        )
        self.run = async_to_streamed_response_wrapper(
            monitors.run,
        )
