# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WebScrapeResponse",
    "Bytes",
    "BytesData",
    "CacheMetadata",
    "Highlights",
    "HTML",
    "Images",
    "ImagesData",
    "Json",
    "Markdown",
    "Metadata",
    "MetadataAlternate",
    "MetadataHeading",
    "Parsed",
    "Product",
    "ProductData",
    "ProductDataProduct",
    "ProductDataProductVariant",
    "Profile",
    "Screenshot",
    "KeyMetadata",
]


class BytesData(BaseModel):
    base64: str
    """Response body as base64, after HTTP decompression. Up to 50 MiB decoded."""

    content_type: str = FieldInfo(alias="contentType")
    """`Content-Type` of the response."""


class Bytes(BaseModel):
    """The original HTTP response body, unchanged by waits, actions, and filters."""

    data: Optional[BytesData] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class CacheMetadata(BaseModel):
    """Cache status of this response."""

    age_ms: int
    """Age of the cached data, in milliseconds. `0` for `miss` and `zdr`."""

    status: Literal["hit", "miss", "zdr"]
    """
    `hit` when served from cache, `miss` when fetched fresh, `zdr` when zero data
    retention bypassed the cache.
    """


class Highlights(BaseModel):
    """Relevant Markdown excerpts in page order.

    `[Heading]` adds context; `…` marks omitted text.
    """

    data: Optional[List[str]] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class HTML(BaseModel):
    """Rendered HTML of the page, after content filters."""

    data: Optional[str] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class ImagesData(BaseModel):
    alt: Optional[str] = None
    """Alt text. `null` when the image has none."""

    url: str
    """Image URL, or a data URI for inline images."""

    classification: Optional[
        Literal["photography", "illustration", "logo", "wordmark", "icon", "pattern", "graphic", "other"]
    ] = None
    """What the image shows, such as a photo, logo, or icon.

    Requires `classification` enrichment.
    """

    file_url: Optional[str] = FieldInfo(alias="fileUrl", default=None)
    """Hosted copy of the image, valid for 24 hours after capture.

    Requires `file` enrichment; not returned with ZDR.
    """

    height: Optional[int] = None
    """Image height in pixels. Requires `dimensions` enrichment."""

    width: Optional[int] = None
    """Image width in pixels. Requires `dimensions` enrichment."""


class Images(BaseModel):
    """Images found on the page, after content filters. `[]` when there are none."""

    data: Optional[List[ImagesData]] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class Json(BaseModel):
    """Object matching `jsonParams.schema`."""

    data: Optional[Dict[str, object]] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    is_truncated: Optional[Literal[True]] = FieldInfo(alias="isTruncated", default=None)
    """
    `true` when the page was too long to read in full, so values that appear only in
    the unread part may be missing.
    """

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class Markdown(BaseModel):
    """Page content as Markdown, after content filters."""

    data: Optional[str] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class MetadataAlternate(BaseModel):
    href: str
    """Absolute URL of the alternate version."""

    hreflang: Optional[str] = None
    """Language or locale of the alternate version, when present."""

    title: Optional[str] = None
    """Title of the alternate version, when present."""

    type: Optional[str] = None
    """MIME type of the alternate version, when present."""


class MetadataHeading(BaseModel):
    level: int
    """Heading level, from 1 (`h1`) to 6 (`h6`)."""

    text: str
    """Heading text with whitespace collapsed, truncated to 1000 characters."""


class Metadata(BaseModel):
    """Page metadata. Fields are omitted when not found."""

    additional_meta: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="additionalMeta", default=None)
    """Other non-social meta tags that don't have their own field."""

    alternates: Optional[List[MetadataAlternate]] = None
    """Alternate links from `link rel="alternate"` tags, as absolute URLs."""

    author: Optional[str] = None
    """Author, when present."""

    canonical_url: Optional[str] = FieldInfo(alias="canonicalUrl", default=None)
    """Absolute canonical URL, when present."""

    description: Optional[str] = None
    """Best available description, from standard, Open Graph, or Twitter meta tags."""

    favicon: Optional[str] = None
    """Absolute favicon URL, when present."""

    headings: Optional[List[MetadataHeading]] = None
    """
    Headings (`h1` to `h6`) in document order, from the full page before any
    filtering. Up to 500. Omitted when the page has none.
    """

    image: Optional[str] = None
    """Main preview image URL, from Open Graph, Twitter, or image meta tags."""

    json_ld: Optional[List[Dict[str, object]]] = FieldInfo(alias="jsonLd", default=None)
    """JSON-LD structured data blocks parsed from the page."""

    keywords: Optional[List[str]] = None
    """Keywords from the page's `keywords` meta tag."""

    language: Optional[str] = None
    """Page language, from the `html` `lang` attribute or language meta tags."""

    modified_time: Optional[str] = FieldInfo(alias="modifiedTime", default=None)
    """Last-modified date or timestamp from page metadata, when present."""

    open_graph: Optional[Dict[str, Union[str, List[str]]]] = FieldInfo(alias="openGraph", default=None)
    """Open Graph tags, with the `og:` prefix removed and keys in camelCase."""

    published_time: Optional[str] = FieldInfo(alias="publishedTime", default=None)
    """Publish date or timestamp from page metadata, when present."""

    robots: Optional[str] = None
    """`robots` meta directive, when present."""

    site_name: Optional[str] = FieldInfo(alias="siteName", default=None)
    """Site or app name from page metadata."""

    title: Optional[str] = None
    """Best available page title."""

    twitter: Optional[Dict[str, Union[str, List[str]]]] = None
    """Twitter card tags, with the `twitter:` prefix removed and keys in camelCase."""


class Parsed(BaseModel):
    """Fields extracted by `parseParams`.

    Custom rules return each field after content filters, with `null` when nothing matches (`[]` for `list` rules). Prebuilt parsers return the record or lists described under `parseParams.parser`.
    """

    data: Optional[Dict[str, object]] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    type: Literal[
        "custom",
        "google-maps",
        "google-maps-reviews",
        "google-play",
        "google-play-reviews",
        "app-store",
        "app-store-reviews",
        "g2-reviews",
        "instagram-profile",
        "instagram-post",
        "instagram-feed",
        "tiktok-profile",
        "tiktok-video",
        "tiktok-feed",
        "tiktok-comments",
        "tiktok-followers",
        "tiktok-following",
        "tiktok-user-search",
        "reddit-post",
        "reddit-search",
        "reddit-subreddit",
        "reddit-user",
        "yelp-search",
        "yelp-reviews",
        "tripadvisor-reviews",
        "car-rental-availability",
        "car-rental-locations",
        "emails",
        "phone-numbers",
        "links",
    ]
    """
    Prebuilt parser that ran, or `custom` for custom rules or when `parse` was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class ProductDataProductVariant(BaseModel):
    attributes: Dict[str, str]
    """
    Attributes that define this variant, such as color, size, material, or pattern,
    as stated on the page.
    """

    images: List[str]
    """Image URLs the source attaches to this variant."""

    sku: Optional[str] = None
    """SKU of this variant. `null` when the source does not state one."""

    url: Optional[str] = None
    """URL of this variant or offer, when the source provides one.

    Several variants can share a URL.
    """

    availability: Optional[
        Literal[
            "in_stock", "out_of_stock", "limited_availability", "preorder", "backorder", "made_to_order", "discontinued"
        ]
    ] = None
    """Stock or ordering availability of this variant."""

    currency: Optional[str] = None
    """Currency code of `price`, such as `USD` or `EUR`, when stated."""

    price: Optional[float] = None
    """Price of this variant, when the source states one per variant."""


class ProductDataProduct(BaseModel):
    """The extracted product. `null` when the page is not a product detail page."""

    availability: Optional[
        Literal[
            "in_stock", "out_of_stock", "limited_availability", "preorder", "backorder", "made_to_order", "discontinued"
        ]
    ] = None
    """Stock or ordering availability."""

    brand: Optional[str] = None
    """Brand or vendor."""

    category: Optional[str] = None
    """Product category."""

    currency: Optional[str] = None
    """ISO 4217 currency code of `price`."""

    description: Optional[str] = None
    """Product description."""

    dimensions: List[str]
    """Product dimensions as shown on the page."""

    features: List[str]
    """Key features and specifications."""

    images: List[str]
    """Product image URLs, main image first."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """Main product image URL."""

    name: str
    """Product name."""

    price: Optional[float] = None
    """Current price."""

    regular_price: Optional[float] = FieldInfo(alias="regularPrice", default=None)
    """List price before any discount."""

    sku: Optional[str] = None
    """Product identifier such as a SKU or model number."""

    tags: List[str]
    """Product tags."""

    target_audience: List[str] = FieldInfo(alias="targetAudience")
    """Intended audience."""

    variants: List[ProductDataProductVariant]
    """Product variants, such as colors or sizes, with their attributes and images.

    `[]` when none are found. May not include every variant the store offers.
    """


class ProductData(BaseModel):
    is_product_page: bool = FieldInfo(alias="isProductPage")
    """Whether the page is a product detail page."""

    product: Optional[ProductDataProduct] = None
    """The extracted product. `null` when the page is not a product detail page."""


class Product(BaseModel):
    """Product details found on the page."""

    data: Optional[ProductData] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class Profile(BaseModel):
    """Browser profile used for this scrape. `null` when no profile was requested."""

    id: str
    """ID of the browser profile.

    After creating a profile, save it and pass it as
    `sharedParams.profile.profileId` with `type: "existing"`.
    """


class Screenshot(BaseModel):
    """Screenshot as a base64 image data URL."""

    data: Optional[str] = None

    requested: bool
    """Whether you requested this output in `formats`."""

    success: Optional[bool] = None
    """
    `true` when the output succeeded, `false` when it failed, `null` when it was not
    requested.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present only when `success` is `false`."""

    message: Optional[str] = None
    """Human-readable explanation of the error and how to resolve it."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class WebScrapeResponse(BaseModel):
    bytes: Bytes
    """The original HTTP response body, unchanged by waits, actions, and filters."""

    cache_metadata: CacheMetadata
    """Cache status of this response."""

    highlights: Highlights
    """Relevant Markdown excerpts in page order.

    `[Heading]` adds context; `…` marks omitted text.
    """

    html: HTML
    """Rendered HTML of the page, after content filters."""

    images: Images
    """Images found on the page, after content filters. `[]` when there are none."""

    json_: Json = FieldInfo(alias="json")
    """Object matching `jsonParams.schema`."""

    markdown: Markdown
    """Page content as Markdown, after content filters."""

    metadata: Metadata
    """Page metadata. Fields are omitted when not found."""

    parsed: Parsed
    """Fields extracted by `parseParams`.

    Custom rules return each field after content filters, with `null` when nothing
    matches (`[]` for `list` rules). Prebuilt parsers return the record or lists
    described under `parseParams.parser`.
    """

    product: Product
    """Product details found on the page."""

    profile: Optional[Profile] = None
    """Browser profile used for this scrape. `null` when no profile was requested."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    screenshot: Screenshot
    """Screenshot as a base64 image data URL."""

    url: str
    """Final URL after redirects and browser actions."""

    is_partial: Optional[Literal[True]] = FieldInfo(alias="isPartial", default=None)
    """
    `true` when at least one requested output succeeded but others failed or are
    incomplete. Absent otherwise.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
