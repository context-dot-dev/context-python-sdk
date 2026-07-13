# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing_extensions import Literal

import httpx

from ..types import parse_handle_params
from .._files import read_file_content, async_read_file_content
from .._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    BinaryTypes,
    FileContent,
    SequenceNotStr,
    AsyncBinaryTypes,
    omit,
    not_given,
)
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
from ..types.parse_handle_response import ParseHandleResponse

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)

    def handle(
        self,
        body: FileContent | BinaryTypes,
        *,
        extension: Literal[
            "txt",
            "text",
            "md",
            "markdown",
            "html",
            "htm",
            "xhtml",
            "xml",
            "rss",
            "atom",
            "csv",
            "tsv",
            "yaml",
            "yml",
            "py",
            "java",
            "js",
            "jsx",
            "mjs",
            "cjs",
            "json",
            "jsonl",
            "ndjson",
            "php",
            "sh",
            "bash",
            "zsh",
            "fish",
            "rb",
            "ts",
            "tsx",
            "rtf",
            "srt",
            "css",
            "scss",
            "less",
            "styl",
            "sass",
            "svg",
            "pdf",
            "docx",
            "doc",
            "xlsx",
            "xlsm",
            "xlsb",
            "xltx",
            "xltm",
            "xls",
            "pptx",
            "pptm",
            "ppsx",
            "ppsm",
            "potx",
            "potm",
            "ppt",
            "pps",
            "pot",
            "jpg",
            "jpeg",
            "jpe",
            "png",
            "gif",
            "bmp",
            "tiff",
            "tif",
            "webp",
            "ppm",
            "pbm",
            "pgm",
            "pnm",
        ]
        | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        ocr: bool | Omit = omit,
        pdf: parse_handle_params.Pdf | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseHandleResponse:
        """
        Converts raw text, source code, web/data, PDF, Microsoft Office, and image bytes
        into LLM-usable Markdown. The base request costs 1 credit. When OCR runs
        (requires ocr=true), the entire call costs 5 credits; ocr=true requests where no
        OCR ends up running still cost 1 credit.

        Args:
          extension: Optional file extension hint. Case-insensitive; a leading dot is accepted (e.g.
              ".pdf").

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          ocr: Gates all OCR. When true, PDFs get embedded-image OCR (recognized text inserted
              at each image's position in page reading order, preserving the text layer;
              pdf.start/pdf.end limit the page range), scanned PDFs with no text layer get
              full-document OCR, and raster images get their visible text transcribed. When
              false, no OCR runs: scanned PDFs may yield no content and images return only
              format/dimension metadata. Calls where OCR actually runs cost 5 credits instead
              of 1.

          pdf: PDF page-range controls. Use start/end to limit parsing (and OCR when ocr=true)
              to an inclusive 1-based page range.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          use_main_content_only: Extract only the main content from HTML-like inputs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/parse",
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "extension": extension,
                        "include_images": include_images,
                        "include_links": include_links,
                        "ocr": ocr,
                        "pdf": pdf,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "use_main_content_only": use_main_content_only,
                    },
                    parse_handle_params.ParseHandleParams,
                ),
            ),
            cast_to=ParseHandleResponse,
        )


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)

    async def handle(
        self,
        body: FileContent | AsyncBinaryTypes,
        *,
        extension: Literal[
            "txt",
            "text",
            "md",
            "markdown",
            "html",
            "htm",
            "xhtml",
            "xml",
            "rss",
            "atom",
            "csv",
            "tsv",
            "yaml",
            "yml",
            "py",
            "java",
            "js",
            "jsx",
            "mjs",
            "cjs",
            "json",
            "jsonl",
            "ndjson",
            "php",
            "sh",
            "bash",
            "zsh",
            "fish",
            "rb",
            "ts",
            "tsx",
            "rtf",
            "srt",
            "css",
            "scss",
            "less",
            "styl",
            "sass",
            "svg",
            "pdf",
            "docx",
            "doc",
            "xlsx",
            "xlsm",
            "xlsb",
            "xltx",
            "xltm",
            "xls",
            "pptx",
            "pptm",
            "ppsx",
            "ppsm",
            "potx",
            "potm",
            "ppt",
            "pps",
            "pot",
            "jpg",
            "jpeg",
            "jpe",
            "png",
            "gif",
            "bmp",
            "tiff",
            "tif",
            "webp",
            "ppm",
            "pbm",
            "pgm",
            "pnm",
        ]
        | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        ocr: bool | Omit = omit,
        pdf: parse_handle_params.Pdf | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseHandleResponse:
        """
        Converts raw text, source code, web/data, PDF, Microsoft Office, and image bytes
        into LLM-usable Markdown. The base request costs 1 credit. When OCR runs
        (requires ocr=true), the entire call costs 5 credits; ocr=true requests where no
        OCR ends up running still cost 1 credit.

        Args:
          extension: Optional file extension hint. Case-insensitive; a leading dot is accepted (e.g.
              ".pdf").

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          ocr: Gates all OCR. When true, PDFs get embedded-image OCR (recognized text inserted
              at each image's position in page reading order, preserving the text layer;
              pdf.start/pdf.end limit the page range), scanned PDFs with no text layer get
              full-document OCR, and raster images get their visible text transcribed. When
              false, no OCR runs: scanned PDFs may yield no content and images return only
              format/dimension metadata. Calls where OCR actually runs cost 5 credits instead
              of 1.

          pdf: PDF page-range controls. Use start/end to limit parsing (and OCR when ocr=true)
              to an inclusive 1-based page range.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          use_main_content_only: Extract only the main content from HTML-like inputs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/parse",
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "extension": extension,
                        "include_images": include_images,
                        "include_links": include_links,
                        "ocr": ocr,
                        "pdf": pdf,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "use_main_content_only": use_main_content_only,
                    },
                    parse_handle_params.ParseHandleParams,
                ),
            ),
            cast_to=ParseHandleResponse,
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.handle = to_raw_response_wrapper(
            parse.handle,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.handle = async_to_raw_response_wrapper(
            parse.handle,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.handle = to_streamed_response_wrapper(
            parse.handle,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.handle = async_to_streamed_response_wrapper(
            parse.handle,
        )
