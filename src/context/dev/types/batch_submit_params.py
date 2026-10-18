# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .retry_config_param import RetryConfigParam

__all__ = [
    "BatchSubmitParams",
    "Input",
    "InputScrape",
    "InputScrapeData",
    "InputScrapeDataFormats",
    "InputScrapeDataURL",
    "InputScrapeDataHighlightsParams",
    "InputScrapeDataImageParams",
    "InputScrapeDataJsonParams",
    "InputScrapeDataMarkdownParams",
    "InputScrapeDataParseParams",
    "InputScrapeDataParseParamsCustomParser",
    "InputScrapeDataParseParamsCustomParserRules",
    "InputScrapeDataParseParamsCustomParserRulesUnionMember1",
    "InputScrapeDataParseParamsPrebuiltParser",
    "InputScrapeDataProductParams",
    "InputScrapeDataScreenshotParams",
    "InputScrapeDataScreenshotParamsArea",
    "InputScrapeDataScreenshotParamsAreaElement",
    "InputScrapeDataScreenshotParamsAreaRectangle",
    "InputScrapeDataSharedParams",
    "InputScrapeDataSharedParamsAction",
    "InputScrapeDataSharedParamsActionPerform",
    "InputScrapeDataSharedParamsActionScroll",
    "InputScrapeDataSharedParamsActionWait",
    "InputScrapeDataSharedParamsActionWaitFor",
    "InputScrapeDataSharedParamsParsers",
    "InputScrapeDataSharedParamsParsersPdf",
    "InputScrapeDataSharedParamsProfile",
    "InputScrapeDataSharedParamsProfileExisting",
    "InputScrapeDataSharedParamsProfileNew",
    "InputScrapeDataSharedParamsViewport",
    "InputScrapeDataTimeoutOpts",
    "InputCrawl",
    "InputCrawlData",
    "InputCrawlDataFormats",
    "InputCrawlDataSource",
    "InputCrawlDataSourceStartURL",
    "InputCrawlDataSourceStartURLControls",
    "InputCrawlDataSourceSitemap",
    "InputCrawlDataSourceSitemapControls",
    "InputCrawlDataHighlightsParams",
    "InputCrawlDataImageParams",
    "InputCrawlDataJsonParams",
    "InputCrawlDataMarkdownParams",
    "InputCrawlDataParseParams",
    "InputCrawlDataParseParamsCustomParser",
    "InputCrawlDataParseParamsCustomParserRules",
    "InputCrawlDataParseParamsCustomParserRulesUnionMember1",
    "InputCrawlDataParseParamsPrebuiltParser",
    "InputCrawlDataProductParams",
    "InputCrawlDataScreenshotParams",
    "InputCrawlDataScreenshotParamsArea",
    "InputCrawlDataScreenshotParamsAreaElement",
    "InputCrawlDataScreenshotParamsAreaRectangle",
    "InputCrawlDataSharedParams",
    "InputCrawlDataSharedParamsAction",
    "InputCrawlDataSharedParamsActionPerform",
    "InputCrawlDataSharedParamsActionScroll",
    "InputCrawlDataSharedParamsActionWait",
    "InputCrawlDataSharedParamsActionWaitFor",
    "InputCrawlDataSharedParamsParsers",
    "InputCrawlDataSharedParamsParsersPdf",
    "InputCrawlDataSharedParamsProfile",
    "InputCrawlDataSharedParamsProfileExisting",
    "InputCrawlDataSharedParamsProfileNew",
    "InputCrawlDataSharedParamsViewport",
    "InputCrawlDataTimeoutOpts",
    "Webhook",
]


class BatchSubmitParams(TypedDict, total=False):
    input: Required[Input]
    """Choose a URL list or a site crawl."""

    tags: SequenceNotStr[str]
    """Tags stored on the batch. Filter the batch list by them later."""

    webhook: Webhook
    """Where to send the batch's final-status event.

    Omit `retry` for one attempt; `{}` uses the default retry schedule.
    """

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """Legacy URL notified when the batch finishes.

    Preserves one best-effort attempt. Cannot be combined with webhook.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Unique key per submission.

    Retrying with the same key and body returns the original batch; a different body
    returns `409`.
    """


class InputScrapeDataFormats(TypedDict, total=False):
    """Outputs to return. Set at least one to `true`."""

    bytes: bool
    """The original HTTP response body."""

    highlights: bool
    """Markdown excerpts relevant to `highlightsParams.query`."""

    html: bool
    """Rendered HTML."""

    images: bool
    """Images found on the page."""

    json: bool
    """An object matching `jsonParams.schema`, extracted from the page."""

    markdown: bool
    """Page content as Markdown."""

    parse: bool
    """Fields extracted with custom rules or a prebuilt parser, returned as `parsed`."""

    product: bool
    """Product details such as name, price, and availability."""

    screenshot: bool
    """A screenshot of the page."""


class InputScrapeDataURL(TypedDict, total=False):
    """A page to scrape, with optional data for matching results."""

    url: Required[str]
    """Page URL to scrape."""

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """Your ID for this page, returned with its result.

    The same URL can use different IDs.
    """

    meta: Dict[str, object]
    """Custom JSON returned unchanged with this page result."""


class InputScrapeDataHighlightsParams(TypedDict, total=False):
    """Requires `formats.highlights: true`; required when it is set."""

    query: Required[str]
    """The question or topic to find passages for."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of returned passages."""


class InputScrapeDataImageParams(TypedDict, total=False):
    """Image options. Requires formats.images: true."""

    dedupe: Literal["none", "visual"]
    """Set `visual` to drop visual duplicates, keeping the largest copy."""

    enrich: List[Literal["dimensions", "classification", "file"]]
    """Extra data per image: `dimensions`, `classification`, or a hosted `file` URL."""


class InputScrapeDataJsonParams(TypedDict, total=False):
    """Requires `formats.json: true`; required when it is set."""

    schema: Required[Dict[str, object]]
    """JSON Schema (not an example object) for a top-level object, up to 50 KB.

    Use optional or nullable fields for missing facts.
    """

    instructions: str
    """Extra guidance, such as which facts to prefer or how to read a field."""


class InputScrapeDataMarkdownParams(TypedDict, total=False):
    """Markdown options. Requires `formats.markdown`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include images in the Markdown using image syntax with URLs and alt text."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown. Set false to return link text without URLs."""

    inline_images: Annotated[Literal["placeholder", "preserve"], PropertyInfo(alias="inlineImages")]
    """How base64 images appear: `placeholder` (default) or `preserve`.

    Requires `includeImages`.
    """


class InputScrapeDataParseParamsCustomParserRulesUnionMember1(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to match within the current page or parent rule."""

    output: Union[Literal["text", "html"], str, object]
    """Return text, HTML, an attribute such as `@href`, or nested field rules.

    Defaults to text.
    """

    type: Literal["item", "list"]
    """Return the first match with `item` or all matches with `list`."""


InputScrapeDataParseParamsCustomParserRules: TypeAlias = Union[
    str, InputScrapeDataParseParamsCustomParserRulesUnionMember1
]


class InputScrapeDataParseParamsCustomParser(TypedDict, total=False):
    rules: Required[Dict[str, InputScrapeDataParseParamsCustomParserRules]]
    """Field names mapped to CSS selectors (`h1`, `a@href`) or rule objects.

    Max 100 fields, 5 levels.
    """

    type: Literal["custom"]
    """Extract fields using custom CSS rules.

    This is the default when type is omitted.
    """


class InputScrapeDataParseParamsPrebuiltParser(TypedDict, total=False):
    parser: Required[
        Literal[
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
            "emails",
            "phone-numbers",
            "links",
        ]
    ]
    """google-maps parses Google Maps business data into data.results.

    Accepts Maps place, search, and internal data URLs. Uses a US exit and English
    labels regardless of hl or Accept-Language. google-maps-reviews returns the
    reviews of a place in data.reviews, in the same shape as the Serper reviews API
    (rating, date, isoDate, snippet, translatedSnippet, likes, user, media,
    response, link, id), plus language, guided ratings in details, and
    user.isLocalGuide; data also carries the place featureId, cid, and sort. sort
    and limit pick the order and count, and oldest is exact. It accepts Maps place,
    search, and ?cid= URLs, plus search.google.com/local/reviews URLs, so the
    google_maps_url and google_reviews_url fields of google-maps results work as
    input. An unknown place returns no reviews. google-play parses a Play Store app
    into data: details, developer contact, ratings, price, permissions, and data
    safety. google-play-reviews returns the 200 newest reviews of the app, with
    developer replies, in data.reviews. Both Play parsers accept app details URLs
    (play.google.com/store/apps/details?id=…); hl and gl set the language and
    storefront, defaulting to en and us. app-store parses an App Store app into
    data: details, developer, ratings, price, version, and screenshots.
    app-store-reviews returns up to the 500 newest reviews in data.reviews. Both App
    Store parsers accept app URLs (apps.apple.com/us/app/…/id…); the country in the
    path sets the storefront, defaulting to us. g2-reviews returns the 25 most
    recently published reviews of a G2 product in data.reviews (rating, title,
    likes, dislikes, problems_solved, reviewer role, company size, and industry),
    plus data.product. It accepts G2 product URLs (g2.com/products/…), follows
    renamed products, and keeps star-rating filters from the URL
    (filters[nps_score][]=1 to 5); other filters, sort orders, and pages are
    ignored. instagram-profile parses a public profile (instagram.com/{username})
    into data: bio, links, follower and post counts, category, business address,
    similar_accounts, and latest_posts (the 12 newest). instagram-post parses a post
    or reel (/p/…, /reel/…) into data: caption, hashtags, mentions, like, comment,
    and view counts, media URLs, tagged users, collaborators, location, and the top
    ~14 comments in data.comments. instagram-feed returns the top posts for a
    hashtag or keyword (/explore/tags/…, /popular/…) or the recent posts at a
    location (/explore/locations/{id}/…) in data.posts; keyword posts carry only the
    shortcode, owner, thumbnail, and views, plus the caption when Instagram shows
    it. All three Instagram parsers read public data without logging in, so private
    accounts return no posts and follower lists are unavailable. tiktok-profile
    parses a public profile (tiktok.com/@{username}) into data: nickname, bio, bio
    link, follower, following, like, and video counts, verified, private, and
    business flags, and business category; it does not list videos. tiktok-video
    parses a video or photo post (/@{username}/video/{id} or
    /@{username}/photo/{id}) into data: caption, hashtags, mentions, author, view,
    like, comment, share, save, and repost counts, duration, thumbnail, a video_url
    that downloads without cookies, image_urls for photo posts, music, location, and
    ad, paid-partnership, and AI-generated flags. tiktok-feed returns videos in the
    tiktok-video shape as data.videos: the latest 15 from a profile URL, the top 30
    from a hashtag URL (/tag/{name}), or the top 12 from a search URL
    (/search?q={query}). tiktok-comments returns the first 20 comments of a video or
    photo post as data.comments: text, posted_at, like and reply counts, whether the
    author liked it, and the commenter. tiktok-followers and tiktok-following return
    up to 30 accounts of a profile as data.users, in the tiktok-profile shape.
    tiktok-user-search returns the top 10 accounts for a user search URL
    (/search/user?q={query}) as data.users: id, username, nickname, biography,
    avatar_url, sec_uid, follower_count, like_count, and is_verified. The TikTok
    parsers accept tiktok.com, www.tiktok.com, and m.tiktok.com URLs but not short
    links (vm.tiktok.com, vt.tiktok.com, tiktok.com/t/…). emails accepts any page
    and returns its email addresses as data.emails ([{ email }]), read from mailto
    links, Cloudflare-protected addresses, and visible text. phone-numbers accepts
    any page and returns its valid phone numbers in E.164 as data.phone_numbers ([{
    phone }]), read from tel links and visible text; numbers without a country code
    are read for the country of the site TLD, defaulting to US. links accepts any
    page and returns its unique http(s) links as data.links ([{ url, text }]), with
    absolute URLs; text falls back to aria-label or image alt and is null when a
    link has none. The emails parser reads the rendered page and respects content
    filters; the other prebuilt parsers read their data independently of DOM
    filters.
    """

    type: Required[Literal["prebuilt"]]
    """Use a prebuilt parser instead of custom rules."""

    limit: int
    """google-maps-reviews only.

    Maximum number of reviews to return. Defaults to 100; maximum 1000.
    """

    sort: Literal["newest", "oldest", "relevant", "highest", "lowest"]
    """google-maps-reviews only.

    Order of data.reviews. newest, relevant, highest, and lowest follow Google;
    oldest returns the earliest reviews first, which Google itself does not offer.
    """


InputScrapeDataParseParams: TypeAlias = Union[
    InputScrapeDataParseParamsCustomParser, InputScrapeDataParseParamsPrebuiltParser
]


class InputScrapeDataProductParams(TypedDict, total=False):
    """Product options. Requires formats.product: true."""

    dedupe_images: Annotated[bool, PropertyInfo(alias="dedupeImages")]
    """Drop visually duplicate product images, keeping the largest copy."""


class InputScrapeDataScreenshotParamsAreaElement(TypedDict, total=False):
    selector: Required[str]
    """CSS selector matching exactly one visible element."""


class InputScrapeDataScreenshotParamsAreaRectangle(TypedDict, total=False):
    """Pixels from the document origin."""

    height: Required[int]
    """Height of the capture in pixels."""

    width: Required[int]
    """Width of the capture in pixels."""

    x: Required[int]
    """Left edge of the capture, in pixels from the document origin."""

    y: Required[int]
    """Top edge of the capture, in pixels from the document origin."""


InputScrapeDataScreenshotParamsArea: TypeAlias = Union[
    Literal["viewport", "fullPage"],
    InputScrapeDataScreenshotParamsAreaElement,
    InputScrapeDataScreenshotParamsAreaRectangle,
]


class InputScrapeDataScreenshotParams(TypedDict, total=False):
    """Screenshot options. Requires formats.screenshot: true."""

    area: InputScrapeDataScreenshotParamsArea
    """What to capture: `viewport`, `fullPage`, one element, or a rectangle.

    Max 40 megapixels.
    """

    format: Literal["png", "jpeg", "webp"]
    """Image format for the screenshot."""


class InputScrapeDataSharedParamsActionPerform(TypedDict, total=False):
    action: Required[str]
    """One browser instruction, such as clicking a button or entering text."""

    type: Required[Literal["perform"]]
    """Use `perform` for a plain-language browser instruction."""


class InputScrapeDataSharedParamsActionScroll(TypedDict, total=False):
    type: Required[Literal["scroll"]]
    """Use `scroll` to move through the page or a container."""

    amount: Union[int, Literal["viewport", "max"]]
    """Distance per scroll: pixels, one `viewport`, or `max` to reach the end."""

    direction: Literal["down", "up", "left", "right"]
    """Direction to scroll."""

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]
    """Maximum number of scroll steps for this action."""

    selector: str
    """Scroll this container. Omit to scroll the page."""


class InputScrapeDataSharedParamsActionWait(TypedDict, total=False):
    milliseconds: Required[int]
    """Time to pause in milliseconds before the next action."""

    type: Required[Literal["wait"]]
    """Use `wait` to pause for a fixed duration."""


class InputScrapeDataSharedParamsActionWaitFor(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to wait for before continuing."""

    type: Required[Literal["waitFor"]]
    """Use `waitFor` to wait for a matching element."""


InputScrapeDataSharedParamsAction: TypeAlias = Union[
    InputScrapeDataSharedParamsActionPerform,
    InputScrapeDataSharedParamsActionScroll,
    InputScrapeDataSharedParamsActionWait,
    InputScrapeDataSharedParamsActionWaitFor,
]


class InputScrapeDataSharedParamsParsersPdf(TypedDict, total=False):
    """PDF page range and OCR."""

    end_page: Annotated[int, PropertyInfo(alias="endPage")]
    """Last page to parse. Must be at least `startPage`."""

    ocr: Literal["off", "auto"]
    """Set `auto` to read scanned pages with OCR."""

    start_page: Annotated[int, PropertyInfo(alias="startPage")]
    """First page to parse, starting at 1."""


class InputScrapeDataSharedParamsParsers(TypedDict, total=False):
    """Document parsing options."""

    pdf: InputScrapeDataSharedParamsParsersPdf
    """PDF page range and OCR."""


class InputScrapeDataSharedParamsProfileExisting(TypedDict, total=False):
    profile_id: Required[Annotated[str, PropertyInfo(alias="profileId")]]
    """The ID returned in profile.id by an earlier scrape."""

    type: Required[Literal["existing"]]
    """Reuse a saved browser profile."""


class InputScrapeDataSharedParamsProfileNew(TypedDict, total=False):
    identifier: Required[str]
    """Username or email for the target website."""

    password: Required[str]
    """Password used to sign in. It is never stored in the profile."""

    type: Required[Literal["new"]]
    """Sign in and create a browser profile."""

    description: str
    """Optional label shown when listing profiles with `GET /org/browser/profiles`."""


InputScrapeDataSharedParamsProfile: TypeAlias = Union[
    InputScrapeDataSharedParamsProfileExisting, InputScrapeDataSharedParamsProfileNew
]


class InputScrapeDataSharedParamsViewport(TypedDict, total=False):
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    height: int
    """Browser viewport height in pixels."""

    width: int
    """Browser viewport width in pixels."""


class InputScrapeDataSharedParams(TypedDict, total=False):
    """Browser and content settings shared by all outputs."""

    actions: Iterable[InputScrapeDataSharedParamsAction]
    """Browser steps run in order before capture.

    Requires a paid plan. Skips the cache.
    """

    country: str
    """Proxy country as a two-letter code, such as `US`. Case-insensitive."""

    dismiss_cookies: Annotated[bool, PropertyInfo(alias="dismissCookies")]
    """Accept cookie banners before actions and capture."""

    dismiss_popups: Annotated[bool, PropertyInfo(alias="dismissPopups")]
    """Close other popups before actions and capture."""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors. Overrides `includeSelectors`."""

    headers: Dict[str, str]
    """HTTP headers to send to the target site. Requests with headers skip the cache."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Include iframe content in HTML and text outputs.

    Screenshots always show visible frames.
    """

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors."""

    main_content_only: Annotated[bool, PropertyInfo(alias="mainContentOnly")]
    """Keep only the main content. Doesn't affect `screenshot`, `bytes`, or `product`."""

    parsers: InputScrapeDataSharedParamsParsers
    """Document parsing options."""

    profile: InputScrapeDataSharedParamsProfile
    """Create or reuse an authenticated browser profile.

    Requires a paid plan and an HTTPS target. Profiles persist session state, bypass
    shared caches, and cannot be combined with ZDR, custom headers, raw bytes, or
    prebuilt parsers.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before capture.

    Defaults to `true` when `screenshot` is requested.
    """

    theme: Literal["light", "dark"]
    """Emulate a light or dark color scheme."""

    viewport: InputScrapeDataSharedParamsViewport
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    wait_for: Annotated[Union[int, str], PropertyInfo(alias="waitFor")]
    """Milliseconds, or a CSS selector to wait for, after actions.

    Defaults to 500 (2000 with frames or XML).
    """


class InputScrapeDataTimeoutOpts(TypedDict, total=False):
    """
    Deadline for each page, using the same behavior and defaults as POST /web/scrape.
    """

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """


class InputScrapeData(TypedDict, total=False):
    """Use the same formats and parameters as POST /web/scrape, replacing url with urls.

    Options apply to every page.
    """

    formats: Required[InputScrapeDataFormats]
    """Outputs to return. Set at least one to `true`."""

    urls: Required[Iterable[InputScrapeDataURL]]
    """Pages to scrape. Maximum 100000."""

    highlights_params: Annotated[InputScrapeDataHighlightsParams, PropertyInfo(alias="highlightsParams")]
    """Requires `formats.highlights: true`; required when it is set."""

    image_params: Annotated[InputScrapeDataImageParams, PropertyInfo(alias="imageParams")]
    """Image options. Requires formats.images: true."""

    json_params: Annotated[InputScrapeDataJsonParams, PropertyInfo(alias="jsonParams")]
    """Requires `formats.json: true`; required when it is set."""

    markdown_params: Annotated[InputScrapeDataMarkdownParams, PropertyInfo(alias="markdownParams")]
    """Markdown options. Requires `formats.markdown`."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached output, in milliseconds.

    `0` fetches fresh. Defaults to 3 days (259200000 ms). Maximum: 1 year
    (31536000000 ms).
    """

    parse_params: Annotated[InputScrapeDataParseParams, PropertyInfo(alias="parseParams")]
    """Requires `formats.parse: true`; required when it is set."""

    product_params: Annotated[InputScrapeDataProductParams, PropertyInfo(alias="productParams")]
    """Product options. Requires formats.product: true."""

    screenshot_params: Annotated[InputScrapeDataScreenshotParams, PropertyInfo(alias="screenshotParams")]
    """Screenshot options. Requires formats.screenshot: true."""

    shared_params: Annotated[InputScrapeDataSharedParams, PropertyInfo(alias="sharedParams")]
    """Browser and content settings shared by all outputs."""

    tags: SequenceNotStr[str]
    """Labels for tracking request usage. Not retained when zdr is enabled."""

    timeout_opts: Annotated[InputScrapeDataTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """
    Deadline for each page, using the same behavior and defaults as POST
    /web/scrape.
    """

    zdr: Literal["disabled"]
    """Batches persist their results.

    Only disabled is supported; enabled returns ZDR_NOT_SUPPORTED.
    """


class InputScrape(TypedDict, total=False):
    """Scrape a list of up to 100,000 URLs."""

    data: Required[InputScrapeData]
    """Use the same formats and parameters as POST /web/scrape, replacing url with
    urls.

    Options apply to every page.
    """

    mode: Required[Literal["scrape"]]
    """Scrape the pages in `data.urls`."""


class InputCrawlDataFormats(TypedDict, total=False):
    """Outputs to return. Set at least one to `true`."""

    bytes: bool
    """The original HTTP response body."""

    highlights: bool
    """Markdown excerpts relevant to `highlightsParams.query`."""

    html: bool
    """Rendered HTML."""

    images: bool
    """Images found on the page."""

    json: bool
    """An object matching `jsonParams.schema`, extracted from the page."""

    markdown: bool
    """Page content as Markdown."""

    parse: bool
    """Fields extracted with custom rules or a prebuilt parser, returned as `parsed`."""

    product: bool
    """Product details such as name, price, and availability."""

    screenshot: bool
    """A screenshot of the page."""


class InputCrawlDataSourceStartURLControls(TypedDict, total=False):
    """Limits and filters for page discovery."""

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """Follow links to subdomains."""

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth. Source pages are depth 0. No limit when omitted."""

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """RE2 pattern for URLs to include. The `start_url` itself is always included."""


class InputCrawlDataSourceStartURL(TypedDict, total=False):
    """Discover pages by following links from one URL."""

    type: Required[Literal["start_url"]]
    """Start from one page."""

    url: Required[str]
    """Page where crawling begins. A URL without a scheme is read as https://."""

    controls: InputCrawlDataSourceStartURLControls
    """Limits and filters for page discovery."""


class InputCrawlDataSourceSitemapControls(TypedDict, total=False):
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so there is no crawl depth here.
    """

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """RE2 pattern; only sitemap URLs matching it are scraped."""


class InputCrawlDataSourceSitemap(TypedDict, total=False):
    """Scrape the pages listed in a domain's sitemap.

    Links on those pages are not followed.
    """

    domain: Required[str]
    """Domain whose sitemap lists the pages to scrape.

    A full URL is reduced to its domain.
    """

    type: Required[Literal["sitemap"]]
    """Scrape the URLs in the domain's sitemap."""

    controls: InputCrawlDataSourceSitemapControls
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so
    there is no crawl depth here.
    """


InputCrawlDataSource: TypeAlias = Union[InputCrawlDataSourceStartURL, InputCrawlDataSourceSitemap]


class InputCrawlDataHighlightsParams(TypedDict, total=False):
    """Requires `formats.highlights: true`; required when it is set."""

    query: Required[str]
    """The question or topic to find passages for."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of returned passages."""


class InputCrawlDataImageParams(TypedDict, total=False):
    """Image options. Requires formats.images: true."""

    dedupe: Literal["none", "visual"]
    """Set `visual` to drop visual duplicates, keeping the largest copy."""

    enrich: List[Literal["dimensions", "classification", "file"]]
    """Extra data per image: `dimensions`, `classification`, or a hosted `file` URL."""


class InputCrawlDataJsonParams(TypedDict, total=False):
    """Requires `formats.json: true`; required when it is set."""

    schema: Required[Dict[str, object]]
    """JSON Schema (not an example object) for a top-level object, up to 50 KB.

    Use optional or nullable fields for missing facts.
    """

    instructions: str
    """Extra guidance, such as which facts to prefer or how to read a field."""


class InputCrawlDataMarkdownParams(TypedDict, total=False):
    """Markdown options. Requires `formats.markdown`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include images in the Markdown using image syntax with URLs and alt text."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown. Set false to return link text without URLs."""

    inline_images: Annotated[Literal["placeholder", "preserve"], PropertyInfo(alias="inlineImages")]
    """How base64 images appear: `placeholder` (default) or `preserve`.

    Requires `includeImages`.
    """


class InputCrawlDataParseParamsCustomParserRulesUnionMember1(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to match within the current page or parent rule."""

    output: Union[Literal["text", "html"], str, object]
    """Return text, HTML, an attribute such as `@href`, or nested field rules.

    Defaults to text.
    """

    type: Literal["item", "list"]
    """Return the first match with `item` or all matches with `list`."""


InputCrawlDataParseParamsCustomParserRules: TypeAlias = Union[
    str, InputCrawlDataParseParamsCustomParserRulesUnionMember1
]


class InputCrawlDataParseParamsCustomParser(TypedDict, total=False):
    rules: Required[Dict[str, InputCrawlDataParseParamsCustomParserRules]]
    """Field names mapped to CSS selectors (`h1`, `a@href`) or rule objects.

    Max 100 fields, 5 levels.
    """

    type: Literal["custom"]
    """Extract fields using custom CSS rules.

    This is the default when type is omitted.
    """


class InputCrawlDataParseParamsPrebuiltParser(TypedDict, total=False):
    parser: Required[
        Literal[
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
            "emails",
            "phone-numbers",
            "links",
        ]
    ]
    """google-maps parses Google Maps business data into data.results.

    Accepts Maps place, search, and internal data URLs. Uses a US exit and English
    labels regardless of hl or Accept-Language. google-maps-reviews returns the
    reviews of a place in data.reviews, in the same shape as the Serper reviews API
    (rating, date, isoDate, snippet, translatedSnippet, likes, user, media,
    response, link, id), plus language, guided ratings in details, and
    user.isLocalGuide; data also carries the place featureId, cid, and sort. sort
    and limit pick the order and count, and oldest is exact. It accepts Maps place,
    search, and ?cid= URLs, plus search.google.com/local/reviews URLs, so the
    google_maps_url and google_reviews_url fields of google-maps results work as
    input. An unknown place returns no reviews. google-play parses a Play Store app
    into data: details, developer contact, ratings, price, permissions, and data
    safety. google-play-reviews returns the 200 newest reviews of the app, with
    developer replies, in data.reviews. Both Play parsers accept app details URLs
    (play.google.com/store/apps/details?id=…); hl and gl set the language and
    storefront, defaulting to en and us. app-store parses an App Store app into
    data: details, developer, ratings, price, version, and screenshots.
    app-store-reviews returns up to the 500 newest reviews in data.reviews. Both App
    Store parsers accept app URLs (apps.apple.com/us/app/…/id…); the country in the
    path sets the storefront, defaulting to us. g2-reviews returns the 25 most
    recently published reviews of a G2 product in data.reviews (rating, title,
    likes, dislikes, problems_solved, reviewer role, company size, and industry),
    plus data.product. It accepts G2 product URLs (g2.com/products/…), follows
    renamed products, and keeps star-rating filters from the URL
    (filters[nps_score][]=1 to 5); other filters, sort orders, and pages are
    ignored. instagram-profile parses a public profile (instagram.com/{username})
    into data: bio, links, follower and post counts, category, business address,
    similar_accounts, and latest_posts (the 12 newest). instagram-post parses a post
    or reel (/p/…, /reel/…) into data: caption, hashtags, mentions, like, comment,
    and view counts, media URLs, tagged users, collaborators, location, and the top
    ~14 comments in data.comments. instagram-feed returns the top posts for a
    hashtag or keyword (/explore/tags/…, /popular/…) or the recent posts at a
    location (/explore/locations/{id}/…) in data.posts; keyword posts carry only the
    shortcode, owner, thumbnail, and views, plus the caption when Instagram shows
    it. All three Instagram parsers read public data without logging in, so private
    accounts return no posts and follower lists are unavailable. tiktok-profile
    parses a public profile (tiktok.com/@{username}) into data: nickname, bio, bio
    link, follower, following, like, and video counts, verified, private, and
    business flags, and business category; it does not list videos. tiktok-video
    parses a video or photo post (/@{username}/video/{id} or
    /@{username}/photo/{id}) into data: caption, hashtags, mentions, author, view,
    like, comment, share, save, and repost counts, duration, thumbnail, a video_url
    that downloads without cookies, image_urls for photo posts, music, location, and
    ad, paid-partnership, and AI-generated flags. tiktok-feed returns videos in the
    tiktok-video shape as data.videos: the latest 15 from a profile URL, the top 30
    from a hashtag URL (/tag/{name}), or the top 12 from a search URL
    (/search?q={query}). tiktok-comments returns the first 20 comments of a video or
    photo post as data.comments: text, posted_at, like and reply counts, whether the
    author liked it, and the commenter. tiktok-followers and tiktok-following return
    up to 30 accounts of a profile as data.users, in the tiktok-profile shape.
    tiktok-user-search returns the top 10 accounts for a user search URL
    (/search/user?q={query}) as data.users: id, username, nickname, biography,
    avatar_url, sec_uid, follower_count, like_count, and is_verified. The TikTok
    parsers accept tiktok.com, www.tiktok.com, and m.tiktok.com URLs but not short
    links (vm.tiktok.com, vt.tiktok.com, tiktok.com/t/…). emails accepts any page
    and returns its email addresses as data.emails ([{ email }]), read from mailto
    links, Cloudflare-protected addresses, and visible text. phone-numbers accepts
    any page and returns its valid phone numbers in E.164 as data.phone_numbers ([{
    phone }]), read from tel links and visible text; numbers without a country code
    are read for the country of the site TLD, defaulting to US. links accepts any
    page and returns its unique http(s) links as data.links ([{ url, text }]), with
    absolute URLs; text falls back to aria-label or image alt and is null when a
    link has none. The emails parser reads the rendered page and respects content
    filters; the other prebuilt parsers read their data independently of DOM
    filters.
    """

    type: Required[Literal["prebuilt"]]
    """Use a prebuilt parser instead of custom rules."""

    limit: int
    """google-maps-reviews only.

    Maximum number of reviews to return. Defaults to 100; maximum 1000.
    """

    sort: Literal["newest", "oldest", "relevant", "highest", "lowest"]
    """google-maps-reviews only.

    Order of data.reviews. newest, relevant, highest, and lowest follow Google;
    oldest returns the earliest reviews first, which Google itself does not offer.
    """


InputCrawlDataParseParams: TypeAlias = Union[
    InputCrawlDataParseParamsCustomParser, InputCrawlDataParseParamsPrebuiltParser
]


class InputCrawlDataProductParams(TypedDict, total=False):
    """Product options. Requires formats.product: true."""

    dedupe_images: Annotated[bool, PropertyInfo(alias="dedupeImages")]
    """Drop visually duplicate product images, keeping the largest copy."""


class InputCrawlDataScreenshotParamsAreaElement(TypedDict, total=False):
    selector: Required[str]
    """CSS selector matching exactly one visible element."""


class InputCrawlDataScreenshotParamsAreaRectangle(TypedDict, total=False):
    """Pixels from the document origin."""

    height: Required[int]
    """Height of the capture in pixels."""

    width: Required[int]
    """Width of the capture in pixels."""

    x: Required[int]
    """Left edge of the capture, in pixels from the document origin."""

    y: Required[int]
    """Top edge of the capture, in pixels from the document origin."""


InputCrawlDataScreenshotParamsArea: TypeAlias = Union[
    Literal["viewport", "fullPage"],
    InputCrawlDataScreenshotParamsAreaElement,
    InputCrawlDataScreenshotParamsAreaRectangle,
]


class InputCrawlDataScreenshotParams(TypedDict, total=False):
    """Screenshot options. Requires formats.screenshot: true."""

    area: InputCrawlDataScreenshotParamsArea
    """What to capture: `viewport`, `fullPage`, one element, or a rectangle.

    Max 40 megapixels.
    """

    format: Literal["png", "jpeg", "webp"]
    """Image format for the screenshot."""


class InputCrawlDataSharedParamsActionPerform(TypedDict, total=False):
    action: Required[str]
    """One browser instruction, such as clicking a button or entering text."""

    type: Required[Literal["perform"]]
    """Use `perform` for a plain-language browser instruction."""


class InputCrawlDataSharedParamsActionScroll(TypedDict, total=False):
    type: Required[Literal["scroll"]]
    """Use `scroll` to move through the page or a container."""

    amount: Union[int, Literal["viewport", "max"]]
    """Distance per scroll: pixels, one `viewport`, or `max` to reach the end."""

    direction: Literal["down", "up", "left", "right"]
    """Direction to scroll."""

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]
    """Maximum number of scroll steps for this action."""

    selector: str
    """Scroll this container. Omit to scroll the page."""


class InputCrawlDataSharedParamsActionWait(TypedDict, total=False):
    milliseconds: Required[int]
    """Time to pause in milliseconds before the next action."""

    type: Required[Literal["wait"]]
    """Use `wait` to pause for a fixed duration."""


class InputCrawlDataSharedParamsActionWaitFor(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to wait for before continuing."""

    type: Required[Literal["waitFor"]]
    """Use `waitFor` to wait for a matching element."""


InputCrawlDataSharedParamsAction: TypeAlias = Union[
    InputCrawlDataSharedParamsActionPerform,
    InputCrawlDataSharedParamsActionScroll,
    InputCrawlDataSharedParamsActionWait,
    InputCrawlDataSharedParamsActionWaitFor,
]


class InputCrawlDataSharedParamsParsersPdf(TypedDict, total=False):
    """PDF page range and OCR."""

    end_page: Annotated[int, PropertyInfo(alias="endPage")]
    """Last page to parse. Must be at least `startPage`."""

    ocr: Literal["off", "auto"]
    """Set `auto` to read scanned pages with OCR."""

    start_page: Annotated[int, PropertyInfo(alias="startPage")]
    """First page to parse, starting at 1."""


class InputCrawlDataSharedParamsParsers(TypedDict, total=False):
    """Document parsing options."""

    pdf: InputCrawlDataSharedParamsParsersPdf
    """PDF page range and OCR."""


class InputCrawlDataSharedParamsProfileExisting(TypedDict, total=False):
    profile_id: Required[Annotated[str, PropertyInfo(alias="profileId")]]
    """The ID returned in profile.id by an earlier scrape."""

    type: Required[Literal["existing"]]
    """Reuse a saved browser profile."""


class InputCrawlDataSharedParamsProfileNew(TypedDict, total=False):
    identifier: Required[str]
    """Username or email for the target website."""

    password: Required[str]
    """Password used to sign in. It is never stored in the profile."""

    type: Required[Literal["new"]]
    """Sign in and create a browser profile."""

    description: str
    """Optional label shown when listing profiles with `GET /org/browser/profiles`."""


InputCrawlDataSharedParamsProfile: TypeAlias = Union[
    InputCrawlDataSharedParamsProfileExisting, InputCrawlDataSharedParamsProfileNew
]


class InputCrawlDataSharedParamsViewport(TypedDict, total=False):
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    height: int
    """Browser viewport height in pixels."""

    width: int
    """Browser viewport width in pixels."""


class InputCrawlDataSharedParams(TypedDict, total=False):
    """Browser and content settings shared by all outputs."""

    actions: Iterable[InputCrawlDataSharedParamsAction]
    """Browser steps run in order before capture.

    Requires a paid plan. Skips the cache.
    """

    country: str
    """Proxy country as a two-letter code, such as `US`. Case-insensitive."""

    dismiss_cookies: Annotated[bool, PropertyInfo(alias="dismissCookies")]
    """Accept cookie banners before actions and capture."""

    dismiss_popups: Annotated[bool, PropertyInfo(alias="dismissPopups")]
    """Close other popups before actions and capture."""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors. Overrides `includeSelectors`."""

    headers: Dict[str, str]
    """HTTP headers to send to the target site. Requests with headers skip the cache."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Include iframe content in HTML and text outputs.

    Screenshots always show visible frames.
    """

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors."""

    main_content_only: Annotated[bool, PropertyInfo(alias="mainContentOnly")]
    """Keep only the main content. Doesn't affect `screenshot`, `bytes`, or `product`."""

    parsers: InputCrawlDataSharedParamsParsers
    """Document parsing options."""

    profile: InputCrawlDataSharedParamsProfile
    """Create or reuse an authenticated browser profile.

    Requires a paid plan and an HTTPS target. Profiles persist session state, bypass
    shared caches, and cannot be combined with ZDR, custom headers, raw bytes, or
    prebuilt parsers.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before capture.

    Defaults to `true` when `screenshot` is requested.
    """

    theme: Literal["light", "dark"]
    """Emulate a light or dark color scheme."""

    viewport: InputCrawlDataSharedParamsViewport
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    wait_for: Annotated[Union[int, str], PropertyInfo(alias="waitFor")]
    """Milliseconds, or a CSS selector to wait for, after actions.

    Defaults to 500 (2000 with frames or XML).
    """


class InputCrawlDataTimeoutOpts(TypedDict, total=False):
    """
    Deadline for each page, using the same behavior and defaults as POST /web/scrape.
    """

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """


class InputCrawlData(TypedDict, total=False):
    """
    Use the same formats and parameters as POST /web/scrape, replacing url with source. Options apply to every page.
    """

    formats: Required[InputCrawlDataFormats]
    """Outputs to return. Set at least one to `true`."""

    source: Required[InputCrawlDataSource]
    """How to find pages to crawl."""

    highlights_params: Annotated[InputCrawlDataHighlightsParams, PropertyInfo(alias="highlightsParams")]
    """Requires `formats.highlights: true`; required when it is set."""

    image_params: Annotated[InputCrawlDataImageParams, PropertyInfo(alias="imageParams")]
    """Image options. Requires formats.images: true."""

    json_params: Annotated[InputCrawlDataJsonParams, PropertyInfo(alias="jsonParams")]
    """Requires `formats.json: true`; required when it is set."""

    markdown_params: Annotated[InputCrawlDataMarkdownParams, PropertyInfo(alias="markdownParams")]
    """Markdown options. Requires `formats.markdown`."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached output, in milliseconds.

    `0` fetches fresh. Defaults to 3 days (259200000 ms). Maximum: 1 year
    (31536000000 ms).
    """

    parse_params: Annotated[InputCrawlDataParseParams, PropertyInfo(alias="parseParams")]
    """Requires `formats.parse: true`; required when it is set."""

    product_params: Annotated[InputCrawlDataProductParams, PropertyInfo(alias="productParams")]
    """Product options. Requires formats.product: true."""

    screenshot_params: Annotated[InputCrawlDataScreenshotParams, PropertyInfo(alias="screenshotParams")]
    """Screenshot options. Requires formats.screenshot: true."""

    shared_params: Annotated[InputCrawlDataSharedParams, PropertyInfo(alias="sharedParams")]
    """Browser and content settings shared by all outputs."""

    tags: SequenceNotStr[str]
    """Labels for tracking request usage. Not retained when zdr is enabled."""

    timeout_opts: Annotated[InputCrawlDataTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """
    Deadline for each page, using the same behavior and defaults as POST
    /web/scrape.
    """

    zdr: Literal["disabled"]
    """Batches persist their results.

    Only disabled is supported; enabled returns ZDR_NOT_SUPPORTED.
    """


class InputCrawl(TypedDict, total=False):
    """Crawl pages starting from a URL or from a domain's sitemap."""

    data: Required[InputCrawlData]
    """
    Use the same formats and parameters as POST /web/scrape, replacing url with
    source. Options apply to every page.
    """

    mode: Required[Literal["crawl"]]
    """Discover and scrape pages from `data.source`."""


Input: TypeAlias = Union[InputScrape, InputCrawl]


class Webhook(TypedDict, total=False):
    """Where to send the batch's final-status event.

    Omit `retry` for one attempt; `{}` uses the default retry schedule.
    """

    url: Required[str]
    """
    Public HTTP(S) URL that receives batch completion, failure, or cancellation
    events.
    """

    retry: RetryConfigParam
    """Webhook retry settings. Use {} for the default schedule."""
