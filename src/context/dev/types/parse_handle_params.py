# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ParseHandleParams", "Pdf"]


class ParseHandleParams(TypedDict, total=False):
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
    """Optional file extension hint.

    Case-insensitive; a leading dot is accepted (e.g. ".pdf").
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in Markdown output"""

    ocr: bool
    """Gates all OCR.

    When true, PDFs get embedded-image OCR (recognized text inserted at each image's
    position in page reading order, preserving the text layer; pdf.start/pdf.end
    limit the page range), scanned PDFs with no text layer get full-document OCR,
    and raster images get their visible text transcribed. When false, no OCR runs:
    scanned PDFs may yield no content and images return only format/dimension
    metadata. Calls where OCR actually runs cost 5 credits instead of 1.
    """

    pdf: Pdf
    """PDF page-range controls.

    Use start/end to limit parsing (and OCR when ocr=true) to an inclusive 1-based
    page range.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Extract only the main content from HTML-like inputs"""


class Pdf(TypedDict, total=False):
    """PDF page-range controls.

    Use start/end to limit parsing (and OCR when ocr=true) to an inclusive 1-based page range.
    """

    end: int
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    start when both are provided.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """
