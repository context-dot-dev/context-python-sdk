# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ParseHandleParams"]


class ParseHandleParams(TypedDict, total=False):
    base_url: Annotated[str, PropertyInfo(alias="baseUrl")]
    """
    Optional HTTP(S) source document URL used to resolve relative links and image
    references. Relative references remain relative when omitted.
    """

    extension: str
    """
    Optional file extension hint, such as pdf, docx, xlsx, pptx, html, json, csv,
    md, py, rtf, jpg, png, or txt.
    """

    filename: str
    """Optional filename hint used to infer the extension when extension is omitted."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in Markdown output"""

    ocr: bool
    """
    When true for PDF inputs, detect and OCR images embedded in the selected pages,
    inserting recognized text at each image's position in page reading order while
    preserving the PDF text layer. pdfStart/pdfEnd limit the inclusive page range.
    This is separate from automatic scanned-PDF OCR fallback.
    """

    pdf_end: Annotated[int, PropertyInfo(alias="pdfEnd")]
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    pdfStart when both are provided.
    """

    pdf_start: Annotated[int, PropertyInfo(alias="pdfStart")]
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Extract only the main content from HTML-like inputs"""
