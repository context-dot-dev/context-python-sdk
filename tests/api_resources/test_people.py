# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import PersonEnrichResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeople:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enrich(self, client: ContextDev) -> None:
        person = client.people.enrich()
        assert_matches_type(PersonEnrichResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enrich_with_all_params(self, client: ContextDev) -> None:
        person = client.people.enrich(
            company={
                "domain": "analyticalengines.example",
                "name": "Analytical Engines",
            },
            education=[
                {
                    "degree": "x",
                    "field_of_study": "x",
                    "graduation_year": 1900,
                    "institution": {
                        "domain": "x",
                        "name": "x",
                    },
                }
            ],
            email="dev@stainless.com",
            location={
                "city": "x",
                "country": "x",
                "region": "x",
            },
            name={
                "first": "Ada",
                "last": "Lovelace",
            },
            social_urls=["https://www.linkedin.com/in/ada-lovelace/"],
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
        )
        assert_matches_type(PersonEnrichResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enrich(self, client: ContextDev) -> None:
        response = client.people.with_raw_response.enrich()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonEnrichResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enrich(self, client: ContextDev) -> None:
        with client.people.with_streaming_response.enrich() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonEnrichResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPeople:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enrich(self, async_client: AsyncContextDev) -> None:
        person = await async_client.people.enrich()
        assert_matches_type(PersonEnrichResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enrich_with_all_params(self, async_client: AsyncContextDev) -> None:
        person = await async_client.people.enrich(
            company={
                "domain": "analyticalengines.example",
                "name": "Analytical Engines",
            },
            education=[
                {
                    "degree": "x",
                    "field_of_study": "x",
                    "graduation_year": 1900,
                    "institution": {
                        "domain": "x",
                        "name": "x",
                    },
                }
            ],
            email="dev@stainless.com",
            location={
                "city": "x",
                "country": "x",
                "region": "x",
            },
            name={
                "first": "Ada",
                "last": "Lovelace",
            },
            social_urls=["https://www.linkedin.com/in/ada-lovelace/"],
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
        )
        assert_matches_type(PersonEnrichResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enrich(self, async_client: AsyncContextDev) -> None:
        response = await async_client.people.with_raw_response.enrich()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonEnrichResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enrich(self, async_client: AsyncContextDev) -> None:
        async with async_client.people.with_streaming_response.enrich() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonEnrichResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True
