# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import NewsSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: ContextDev) -> None:
        news = client.news.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
        )
        assert_matches_type(NewsSearchResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: ContextDev) -> None:
        news = client.news.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
            cursor="cursor",
            filter_by={
                "article_language": ["ar"],
                "article_type": ["editorial"],
                "date": {
                    "from": 0,
                    "to": 0,
                },
                "source_country": ["ae"],
                "source_domain": ["x"],
            },
            limit=1,
            sort_by={"type": "relevance"},
            tags=["production", "team-alpha"],
        )
        assert_matches_type(NewsSearchResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: ContextDev) -> None:
        response = client.news.with_raw_response.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(NewsSearchResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: ContextDev) -> None:
        with client.news.with_streaming_response.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(NewsSearchResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncContextDev) -> None:
        news = await async_client.news.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
        )
        assert_matches_type(NewsSearchResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncContextDev) -> None:
        news = await async_client.news.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
            cursor="cursor",
            filter_by={
                "article_language": ["ar"],
                "article_type": ["editorial"],
                "date": {
                    "from": 0,
                    "to": 0,
                },
                "source_country": ["ae"],
                "source_domain": ["x"],
            },
            limit=1,
            sort_by={"type": "relevance"},
            tags=["production", "team-alpha"],
        )
        assert_matches_type(NewsSearchResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncContextDev) -> None:
        response = await async_client.news.with_raw_response.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(NewsSearchResponse, news, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncContextDev) -> None:
        async with async_client.news.with_streaming_response.search(
            search_by={
                "entity": {
                    "name": "xx",
                    "type": "name",
                },
                "type": "entity",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(NewsSearchResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True
