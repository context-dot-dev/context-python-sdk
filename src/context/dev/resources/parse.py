# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

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
        base_url: str | Omit = omit,
        extension: str | Omit = omit,
        filename: str | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        ocr: bool | Omit = omit,
        pdf_end: int | Omit = omit,
        pdf_start: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
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
        into LLM-usable Markdown.

        Args:
          base_url: Optional HTTP(S) source document URL used to resolve relative links and image
              references. Relative references remain relative when omitted.

          extension: Optional file extension hint, such as pdf, docx, xlsx, pptx, html, json, csv,
              md, py, rtf, jpg, png, or txt.

          filename: Optional filename hint used to infer the extension when extension is omitted.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          ocr: When true for PDF inputs, detect and OCR images embedded in the selected pages,
              inserting recognized text at each image's position in page reading order while
              preserving the PDF text layer. pdfStart/pdfEnd limit the inclusive page range.
              This is separate from automatic scanned-PDF OCR fallback.

          pdf_end: Last 1-based PDF page to parse. When omitted, parsing ends at the last page.
              Must be greater than or equal to pdfStart when both are provided.

          pdf_start: First 1-based PDF page to parse. When omitted, parsing starts at the first page.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

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
                        "base_url": base_url,
                        "extension": extension,
                        "filename": filename,
                        "include_images": include_images,
                        "include_links": include_links,
                        "ocr": ocr,
                        "pdf_end": pdf_end,
                        "pdf_start": pdf_start,
                        "shorten_base64_images": shorten_base64_images,
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
        base_url: str | Omit = omit,
        extension: str | Omit = omit,
        filename: str | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        ocr: bool | Omit = omit,
        pdf_end: int | Omit = omit,
        pdf_start: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
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
        into LLM-usable Markdown.

        Args:
          base_url: Optional HTTP(S) source document URL used to resolve relative links and image
              references. Relative references remain relative when omitted.

          extension: Optional file extension hint, such as pdf, docx, xlsx, pptx, html, json, csv,
              md, py, rtf, jpg, png, or txt.

          filename: Optional filename hint used to infer the extension when extension is omitted.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          ocr: When true for PDF inputs, detect and OCR images embedded in the selected pages,
              inserting recognized text at each image's position in page reading order while
              preserving the PDF text layer. pdfStart/pdfEnd limit the inclusive page range.
              This is separate from automatic scanned-PDF OCR fallback.

          pdf_end: Last 1-based PDF page to parse. When omitted, parsing ends at the last page.
              Must be greater than or equal to pdfStart when both are provided.

          pdf_start: First 1-based PDF page to parse. When omitted, parsing starts at the first page.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

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
                        "base_url": base_url,
                        "extension": extension,
                        "filename": filename,
                        "include_images": include_images,
                        "include_links": include_links,
                        "ocr": ocr,
                        "pdf_end": pdf_end,
                        "pdf_start": pdf_start,
                        "shorten_base64_images": shorten_base64_images,
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
