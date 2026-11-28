# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ParseHandleParams", "Pdf"]


class ParseHandleParams(TypedDict, total=False):
    client: str
    """Client identifier for usage attribution."""

    extension: Literal[
        "warc",
        "warc.gz",
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
    """
    File type hint, such as `pdf`, `docx`, `xlsx`, `pptx`, `html`, `json`, `csv`,
    `md`, `py`, `rtf`, `jpg`, `png`, `txt`, `warc`, or `warc.gz`. Use it when the
    `Content-Type` header is missing or generic.
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown."""

    include_numbered_pages: Annotated[bool, PropertyInfo(alias="includeNumberedPages")]
    """
    Start each PDF page in the Markdown with a `<!-- page N -->` line, where `N` is
    the original 1-based page number.
    """

    ocr: bool
    """
    Read text from images and scanned PDF pages with OCR, within the `pdf` page
    range. Adds 1 credit per page read.
    """

    pdf: Pdf
    """PDF page range as a JSON object, such as `{"start": 2, "end": 5}`."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten inline base64 image data."""

    tags: SequenceNotStr[str]
    """Comma-separated labels for this request, such as `production,team-alpha`.

    Filter usage and request logs by them.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Keep only the main content, without navigation, headers, footers, or sidebars.

    Applies to HTML-like inputs.
    """

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Pdf(TypedDict, total=False):
    """PDF page range as a JSON object, such as `{"start": 2, "end": 5}`."""

    end: int
    """Last page to parse. Defaults to the last page. Must be at least `start`."""

    start: int
    """First page to parse, starting at 1."""
