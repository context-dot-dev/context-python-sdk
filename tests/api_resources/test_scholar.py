# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import ScholarSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScholar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: ContextDev) -> None:
        scholar = client.scholar.search(
            query="CRISPR off-target effects in human cells",
        )
        assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: ContextDev) -> None:
        scholar = client.scholar.search(
            query="CRISPR off-target effects in human cells",
            cursor="cursor",
            filter_by={
                "date": {
                    "from": 0,
                    "to": 0,
                }
            },
            limit=1,
            sort="relevance",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: ContextDev) -> None:
        response = client.scholar.with_raw_response.search(
            query="CRISPR off-target effects in human cells",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scholar = response.parse()
        assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: ContextDev) -> None:
        with client.scholar.with_streaming_response.search(
            query="CRISPR off-target effects in human cells",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scholar = response.parse()
            assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScholar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncContextDev) -> None:
        scholar = await async_client.scholar.search(
            query="CRISPR off-target effects in human cells",
        )
        assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncContextDev) -> None:
        scholar = await async_client.scholar.search(
            query="CRISPR off-target effects in human cells",
            cursor="cursor",
            filter_by={
                "date": {
                    "from": 0,
                    "to": 0,
                }
            },
            limit=1,
            sort="relevance",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncContextDev) -> None:
        response = await async_client.scholar.with_raw_response.search(
            query="CRISPR off-target effects in human cells",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scholar = await response.parse()
        assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncContextDev) -> None:
        async with async_client.scholar.with_streaming_response.search(
            query="CRISPR off-target effects in human cells",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scholar = await response.parse()
            assert_matches_type(ScholarSearchResponse, scholar, path=["response"])

        assert cast(Any, response.is_closed) is True
