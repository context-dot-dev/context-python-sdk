# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    MonitorRunResponse,
    MonitorListResponse,
    MonitorCreateResponse,
    MonitorDeleteResponse,
    MonitorUpdateResponse,
    MonitorListRunsResponse,
    MonitorRetrieveResponse,
    MonitorListChangesResponse,
    MonitorRetrieveChangeResponse,
    MonitorListAccountRunsResponse,
    MonitorListAccountChangesResponse,
)
from context.dev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: ContextDev) -> None:
        monitor = client.monitors.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
            },
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ContextDev) -> None:
        monitor = client.monitors.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
                "normalize_whitespace": True,
            },
            mode="web",
            tags=["pricing", "competitor"],
            webhook={
                "url": "https://example.com/webhook",
                "events": ["change.detected", "run.completed"],
            },
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ContextDev) -> None:
        monitor = client.monitors.retrieve(
            "mon_123",
        )
        assert_matches_type(MonitorRetrieveResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.retrieve(
            "mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorRetrieveResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.retrieve(
            "mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorRetrieveResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: ContextDev) -> None:
        monitor = client.monitors.update(
            monitor_id="mon_123",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ContextDev) -> None:
        monitor = client.monitors.update(
            monitor_id="mon_123",
            change_detection={"type": "exact"},
            name="Acme pricing monitor",
            schedule={
                "frequency": 1,
                "type": "interval",
                "unit": "hours",
            },
            status="active",
            tags=["pricing", "competitor"],
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
                "normalize_whitespace": True,
            },
            webhook={
                "url": "https://example.com/webhook",
                "events": ["change.detected", "run.completed"],
            },
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.update(
            monitor_id="mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.update(
            monitor_id="mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitors.with_raw_response.update(
                monitor_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ContextDev) -> None:
        monitor = client.monitors.list()
        assert_matches_type(MonitorListResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ContextDev) -> None:
        monitor = client.monitors.list(
            change_detection_type="exact",
            cursor="cursor",
            limit=1,
            q="q",
            search_by=["name"],
            search_type="exact",
            status="active",
            tag="tag",
            tags=["string"],
            target_type="page",
        )
        assert_matches_type(MonitorListResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorListResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorListResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: ContextDev) -> None:
        monitor = client.monitors.delete(
            "mon_123",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.delete(
            "mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.delete(
            "mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_account_changes(self, client: ContextDev) -> None:
        monitor = client.monitors.list_account_changes()
        assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_account_changes_with_all_params(self, client: ContextDev) -> None:
        monitor = client.monitors.list_account_changes(
            change_detection_type="exact",
            cursor="cursor",
            limit=1,
            monitor_id="monitor_id",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
            target_type="page",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_account_changes(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.list_account_changes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_account_changes(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.list_account_changes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_account_runs(self, client: ContextDev) -> None:
        monitor = client.monitors.list_account_runs()
        assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_account_runs_with_all_params(self, client: ContextDev) -> None:
        monitor = client.monitors.list_account_runs(
            cursor="cursor",
            limit=1,
            status="queued",
        )
        assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_account_runs(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.list_account_runs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_account_runs(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.list_account_runs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_changes(self, client: ContextDev) -> None:
        monitor = client.monitors.list_changes(
            monitor_id="mon_123",
        )
        assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_changes_with_all_params(self, client: ContextDev) -> None:
        monitor = client.monitors.list_changes(
            monitor_id="mon_123",
            cursor="cursor",
            limit=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_changes(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.list_changes(
            monitor_id="mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_changes(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.list_changes(
            monitor_id="mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_changes(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitors.with_raw_response.list_changes(
                monitor_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs(self, client: ContextDev) -> None:
        monitor = client.monitors.list_runs(
            monitor_id="mon_123",
        )
        assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs_with_all_params(self, client: ContextDev) -> None:
        monitor = client.monitors.list_runs(
            monitor_id="mon_123",
            cursor="cursor",
            limit=1,
            status="queued",
        )
        assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_runs(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.list_runs(
            monitor_id="mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_runs(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.list_runs(
            monitor_id="mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_runs(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitors.with_raw_response.list_runs(
                monitor_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_change(self, client: ContextDev) -> None:
        monitor = client.monitors.retrieve_change(
            "chg_123",
        )
        assert_matches_type(MonitorRetrieveChangeResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_change(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.retrieve_change(
            "chg_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorRetrieveChangeResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_change(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.retrieve_change(
            "chg_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorRetrieveChangeResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_change(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `change_id` but received ''"):
            client.monitors.with_raw_response.retrieve_change(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: ContextDev) -> None:
        monitor = client.monitors.run(
            "mon_123",
        )
        assert_matches_type(MonitorRunResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: ContextDev) -> None:
        response = client.monitors.with_raw_response.run(
            "mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorRunResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: ContextDev) -> None:
        with client.monitors.with_streaming_response.run(
            "mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorRunResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_run(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitors.with_raw_response.run(
                "",
            )


class TestAsyncMonitors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
            },
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
                "normalize_whitespace": True,
            },
            mode="web",
            tags=["pricing", "competitor"],
            webhook={
                "url": "https://example.com/webhook",
                "events": ["change.detected", "run.completed"],
            },
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.create(
            change_detection={"type": "exact"},
            name="Acme pricing page",
            schedule={
                "frequency": 6,
                "type": "interval",
                "unit": "hours",
            },
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.retrieve(
            "mon_123",
        )
        assert_matches_type(MonitorRetrieveResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.retrieve(
            "mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorRetrieveResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.retrieve(
            "mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorRetrieveResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.update(
            monitor_id="mon_123",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.update(
            monitor_id="mon_123",
            change_detection={"type": "exact"},
            name="Acme pricing monitor",
            schedule={
                "frequency": 1,
                "type": "interval",
                "unit": "hours",
            },
            status="active",
            tags=["pricing", "competitor"],
            target={
                "type": "page",
                "url": "https://acme.com/pricing",
                "normalize_whitespace": True,
            },
            webhook={
                "url": "https://example.com/webhook",
                "events": ["change.detected", "run.completed"],
            },
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.update(
            monitor_id="mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.update(
            monitor_id="mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitors.with_raw_response.update(
                monitor_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list()
        assert_matches_type(MonitorListResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list(
            change_detection_type="exact",
            cursor="cursor",
            limit=1,
            q="q",
            search_by=["name"],
            search_type="exact",
            status="active",
            tag="tag",
            tags=["string"],
            target_type="page",
        )
        assert_matches_type(MonitorListResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorListResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorListResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.delete(
            "mon_123",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.delete(
            "mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.delete(
            "mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_account_changes(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_account_changes()
        assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_account_changes_with_all_params(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_account_changes(
            change_detection_type="exact",
            cursor="cursor",
            limit=1,
            monitor_id="monitor_id",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
            target_type="page",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_account_changes(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.list_account_changes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_account_changes(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.list_account_changes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorListAccountChangesResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_account_runs(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_account_runs()
        assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_account_runs_with_all_params(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_account_runs(
            cursor="cursor",
            limit=1,
            status="queued",
        )
        assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_account_runs(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.list_account_runs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_account_runs(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.list_account_runs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorListAccountRunsResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_changes(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_changes(
            monitor_id="mon_123",
        )
        assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_changes_with_all_params(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_changes(
            monitor_id="mon_123",
            cursor="cursor",
            limit=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_changes(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.list_changes(
            monitor_id="mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_changes(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.list_changes(
            monitor_id="mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorListChangesResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_changes(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitors.with_raw_response.list_changes(
                monitor_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_runs(
            monitor_id="mon_123",
        )
        assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs_with_all_params(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.list_runs(
            monitor_id="mon_123",
            cursor="cursor",
            limit=1,
            status="queued",
        )
        assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_runs(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.list_runs(
            monitor_id="mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_runs(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.list_runs(
            monitor_id="mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorListRunsResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_runs(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitors.with_raw_response.list_runs(
                monitor_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_change(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.retrieve_change(
            "chg_123",
        )
        assert_matches_type(MonitorRetrieveChangeResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_change(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.retrieve_change(
            "chg_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorRetrieveChangeResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_change(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.retrieve_change(
            "chg_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorRetrieveChangeResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_change(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `change_id` but received ''"):
            await async_client.monitors.with_raw_response.retrieve_change(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncContextDev) -> None:
        monitor = await async_client.monitors.run(
            "mon_123",
        )
        assert_matches_type(MonitorRunResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncContextDev) -> None:
        response = await async_client.monitors.with_raw_response.run(
            "mon_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorRunResponse, monitor, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncContextDev) -> None:
        async with async_client.monitors.with_streaming_response.run(
            "mon_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorRunResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitors.with_raw_response.run(
                "",
            )
