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
from ..types.monitor_retrieve_run_response import MonitorRetrieveRunResponse
from ..types.monitor_retrieve_change_response import MonitorRetrieveChangeResponse
from ..types.monitor_get_credit_usage_response import MonitorGetCreditUsageResponse
from ..types.monitor_list_account_runs_response import MonitorListAccountRunsResponse
from ..types.monitor_list_account_changes_response import MonitorListAccountChangesResponse
from ..types.monitor_rotate_webhook_secret_response import MonitorRotateWebhookSecretResponse

__all__ = ["MonitorsResource", "AsyncMonitorsResource"]


class MonitorsResource(SyncAPIResource):
    """Watch websites on a schedule for exact or meaningful changes."""

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
        policies: SequenceNotStr[str] | Omit = omit,
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
        """
        Watch a web page, a sitemap, data extracted from a site, or web search results
        on a schedule, and get a webhook when something changes. Creating a monitor
        queues its baseline run right away.

        Args:
          name: Display name for the monitor.

          target: What to watch: a page, a sitemap, data extracted from a site, or web search
              results.

          change_detection: How changes are judged. Defaults to `semantic` for extract and search targets
              and for page targets with `instructions`; otherwise `exact`. Sitemap targets
              support only `exact`, and extract targets only `semantic`.

          mode: Monitor category. Always `web`.

          policies: Access policy IDs to apply to every run. Requires access policies enabled for
              your organization; otherwise returns `ACCESS_POLICIES_NOT_ENABLED`.

          schedule: Run the monitor at a fixed interval, such as every 6 hours or every 2 days. The
              interval must be between 10 minutes and 1 year.

          tags: Labels for grouping monitors. Filter monitors, changes, and credit usage by tag.

          webhook: Webhook that receives monitor events. `null` when no webhook is configured.

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
                    "policies": policies,
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
        Retrieve a monitor's configuration, status, and current baseline.

        Args:
          monitor_id: ID of the monitor.

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
        policies: SequenceNotStr[str] | Omit = omit,
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
        """Change a monitor's settings, or pause and resume it.

        Changing the target or
        change detection replaces the baseline and queues a new baseline run.

        Args:
          monitor_id: ID of the monitor.

          change_detection: How changes are judged. Defaults to `semantic` for extract and search targets
              and for page targets with `instructions`; otherwise `exact`. Sitemap targets
              support only `exact`, and extract targets only `semantic`.

          name: Display name for the monitor.

          policies: Access policy IDs to apply to every run, or an empty list to remove them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          schedule: Run the monitor at a fixed interval, such as every 6 hours or every 2 days. The
              interval must be between 10 minutes and 1 year.

          status: Set `paused` to stop scheduled runs or `active` to resume them. A resumed
              monitor runs promptly instead of waiting a full interval.

          tags: Labels for grouping monitors. Filter monitors, changes, and credit usage by tag.

          target: What to watch: a page, a sitemap, data extracted from a site, or web search
              results.

          webhook: Set to `null` to remove the webhook. Changing `url` generates a new secret.

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
                    "policies": policies,
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_type: Literal["page", "sitemap", "extract", "search"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """List your monitors, newest first.

        Search by name, URL, or instructions, and
        filter by status, target type, detection type, or tags.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of monitors to return per page. Defaults to 25.

          q: Text to search for in the fields listed in `search_by`.

          search_by: Comma-separated fields to search with `q`. Defaults to all fields. For search
              targets, `url` matches the target's `query`.

          search_type: How `q` matches. `prefix` matches the start of words and tolerates one typo, for
              search as you type; `exact` matches whole words only. Defaults to `prefix`.

          status: Filter by monitor status.

          tags: Comma-separated tags. Returns monitors that have any of them.

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
        """Delete a monitor along with its runs, changes, and baseline.

        Future runs and
        pending webhook retries stop.

        Args:
          monitor_id: ID of the monitor.

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
        tag: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGetCreditUsageResponse:
        """
        List credits charged per monitor, highest first, from up to the 10,000 most
        recent runs in the time window. Pass `tag` to report on one group of monitors,
        such as a single customer's.

        Args:
          since: Count only runs created at or after this time.

          tag: Return usage only for monitors that currently have this tag. Deleted monitors
              are excluded.

          until: Count only runs created at or before this time.

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
                        "tag": tag,
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
        """Retrieve how many monitors your organization has and how many your plan allows."""
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
        target_type: Literal["page", "sitemap", "extract", "search"] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListAccountChangesResponse:
        """List detected changes across all your monitors, newest first.

        Filter by monitor,
        target type, detection type, tag, or time range.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of changes to return per page. Defaults to 25.

          monitor_id: Return only changes from this monitor.

          since: Return only changes detected at or after this time.

          tag: Return only changes that have this tag.

          target_type: Filter by target type.

          until: Return only changes detected at or before this time.

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
        List runs across all your monitors, newest first.

        Args:
          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of runs to return per page. Defaults to 25.

          status: Filter by run status.

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
        """List a monitor's detected changes, newest first.

        Each change includes its full
        diff and evidence.

        Args:
          monitor_id: ID of the monitor.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of changes to return per page. Defaults to 25.

          since: Return only changes detected at or after this time.

          tag: Return only changes that have this tag.

          until: Return only changes detected at or before this time.

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
        List a monitor's runs, newest first.

        Args:
          monitor_id: ID of the monitor.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of runs to return per page. Defaults to 25.

          status: Filter by run status.

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
        Retrieve a detected change with its summary, diff, URLs, and evidence.

        Args:
          change_id: ID of the change.

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

    def retrieve_run(
        self,
        run_id: str,
        *,
        monitor_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRetrieveRunResponse:
        """Retrieve a run's status, timing, credit charge, and webhook deliveries.

        If the
        run found a change, `change_id` points to it.

        Args:
          monitor_id: ID of the monitor.

          run_id: ID of the run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/monitors/{monitor_id}/runs/{run_id}", monitor_id=monitor_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRetrieveRunResponse,
        )

    def rotate_webhook_secret(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRotateWebhookSecretResponse:
        """Replace the monitor's webhook signing secret.

        The new secret signs every
        delivery attempt from now on, including retries.

        Args:
          monitor_id: ID of the monitor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._post(
            path_template("/monitors/{monitor_id}/webhook/rotate-secret", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRotateWebhookSecretResponse,
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
        """Queue a run now without changing the monitor's schedule.

        Returns the run ID to
        poll. Paused monitors return `409`.

        Args:
          monitor_id: ID of the monitor.

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
    """Watch websites on a schedule for exact or meaningful changes."""

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
        policies: SequenceNotStr[str] | Omit = omit,
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
        """
        Watch a web page, a sitemap, data extracted from a site, or web search results
        on a schedule, and get a webhook when something changes. Creating a monitor
        queues its baseline run right away.

        Args:
          name: Display name for the monitor.

          target: What to watch: a page, a sitemap, data extracted from a site, or web search
              results.

          change_detection: How changes are judged. Defaults to `semantic` for extract and search targets
              and for page targets with `instructions`; otherwise `exact`. Sitemap targets
              support only `exact`, and extract targets only `semantic`.

          mode: Monitor category. Always `web`.

          policies: Access policy IDs to apply to every run. Requires access policies enabled for
              your organization; otherwise returns `ACCESS_POLICIES_NOT_ENABLED`.

          schedule: Run the monitor at a fixed interval, such as every 6 hours or every 2 days. The
              interval must be between 10 minutes and 1 year.

          tags: Labels for grouping monitors. Filter monitors, changes, and credit usage by tag.

          webhook: Webhook that receives monitor events. `null` when no webhook is configured.

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
                    "policies": policies,
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
        Retrieve a monitor's configuration, status, and current baseline.

        Args:
          monitor_id: ID of the monitor.

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
        policies: SequenceNotStr[str] | Omit = omit,
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
        """Change a monitor's settings, or pause and resume it.

        Changing the target or
        change detection replaces the baseline and queues a new baseline run.

        Args:
          monitor_id: ID of the monitor.

          change_detection: How changes are judged. Defaults to `semantic` for extract and search targets
              and for page targets with `instructions`; otherwise `exact`. Sitemap targets
              support only `exact`, and extract targets only `semantic`.

          name: Display name for the monitor.

          policies: Access policy IDs to apply to every run, or an empty list to remove them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          schedule: Run the monitor at a fixed interval, such as every 6 hours or every 2 days. The
              interval must be between 10 minutes and 1 year.

          status: Set `paused` to stop scheduled runs or `active` to resume them. A resumed
              monitor runs promptly instead of waiting a full interval.

          tags: Labels for grouping monitors. Filter monitors, changes, and credit usage by tag.

          target: What to watch: a page, a sitemap, data extracted from a site, or web search
              results.

          webhook: Set to `null` to remove the webhook. Changing `url` generates a new secret.

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
                    "policies": policies,
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
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        target_type: Literal["page", "sitemap", "extract", "search"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """List your monitors, newest first.

        Search by name, URL, or instructions, and
        filter by status, target type, detection type, or tags.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of monitors to return per page. Defaults to 25.

          q: Text to search for in the fields listed in `search_by`.

          search_by: Comma-separated fields to search with `q`. Defaults to all fields. For search
              targets, `url` matches the target's `query`.

          search_type: How `q` matches. `prefix` matches the start of words and tolerates one typo, for
              search as you type; `exact` matches whole words only. Defaults to `prefix`.

          status: Filter by monitor status.

          tags: Comma-separated tags. Returns monitors that have any of them.

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
        """Delete a monitor along with its runs, changes, and baseline.

        Future runs and
        pending webhook retries stop.

        Args:
          monitor_id: ID of the monitor.

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
        tag: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorGetCreditUsageResponse:
        """
        List credits charged per monitor, highest first, from up to the 10,000 most
        recent runs in the time window. Pass `tag` to report on one group of monitors,
        such as a single customer's.

        Args:
          since: Count only runs created at or after this time.

          tag: Return usage only for monitors that currently have this tag. Deleted monitors
              are excluded.

          until: Count only runs created at or before this time.

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
                        "tag": tag,
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
        """Retrieve how many monitors your organization has and how many your plan allows."""
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
        target_type: Literal["page", "sitemap", "extract", "search"] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListAccountChangesResponse:
        """List detected changes across all your monitors, newest first.

        Filter by monitor,
        target type, detection type, tag, or time range.

        Args:
          change_detection_type: Filter by change detection type.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of changes to return per page. Defaults to 25.

          monitor_id: Return only changes from this monitor.

          since: Return only changes detected at or after this time.

          tag: Return only changes that have this tag.

          target_type: Filter by target type.

          until: Return only changes detected at or before this time.

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
        List runs across all your monitors, newest first.

        Args:
          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of runs to return per page. Defaults to 25.

          status: Filter by run status.

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
        """List a monitor's detected changes, newest first.

        Each change includes its full
        diff and evidence.

        Args:
          monitor_id: ID of the monitor.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of changes to return per page. Defaults to 25.

          since: Return only changes detected at or after this time.

          tag: Return only changes that have this tag.

          until: Return only changes detected at or before this time.

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
        List a monitor's runs, newest first.

        Args:
          monitor_id: ID of the monitor.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of runs to return per page. Defaults to 25.

          status: Filter by run status.

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
        Retrieve a detected change with its summary, diff, URLs, and evidence.

        Args:
          change_id: ID of the change.

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

    async def retrieve_run(
        self,
        run_id: str,
        *,
        monitor_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRetrieveRunResponse:
        """Retrieve a run's status, timing, credit charge, and webhook deliveries.

        If the
        run found a change, `change_id` points to it.

        Args:
          monitor_id: ID of the monitor.

          run_id: ID of the run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/monitors/{monitor_id}/runs/{run_id}", monitor_id=monitor_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRetrieveRunResponse,
        )

    async def rotate_webhook_secret(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorRotateWebhookSecretResponse:
        """Replace the monitor's webhook signing secret.

        The new secret signs every
        delivery attempt from now on, including retries.

        Args:
          monitor_id: ID of the monitor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._post(
            path_template("/monitors/{monitor_id}/webhook/rotate-secret", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorRotateWebhookSecretResponse,
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
        """Queue a run now without changing the monitor's schedule.

        Returns the run ID to
        poll. Paused monitors return `409`.

        Args:
          monitor_id: ID of the monitor.

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
        self.retrieve_run = to_raw_response_wrapper(
            monitors.retrieve_run,
        )
        self.rotate_webhook_secret = to_raw_response_wrapper(
            monitors.rotate_webhook_secret,
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
        self.retrieve_run = async_to_raw_response_wrapper(
            monitors.retrieve_run,
        )
        self.rotate_webhook_secret = async_to_raw_response_wrapper(
            monitors.rotate_webhook_secret,
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
        self.retrieve_run = to_streamed_response_wrapper(
            monitors.retrieve_run,
        )
        self.rotate_webhook_secret = to_streamed_response_wrapper(
            monitors.rotate_webhook_secret,
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
        self.retrieve_run = async_to_streamed_response_wrapper(
            monitors.retrieve_run,
        )
        self.rotate_webhook_secret = async_to_streamed_response_wrapper(
            monitors.rotate_webhook_secret,
        )
        self.run = async_to_streamed_response_wrapper(
            monitors.run,
        )
