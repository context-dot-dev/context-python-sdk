# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WebScrapeParams",
    "Formats",
    "HighlightsParams",
    "ImageParams",
    "JsonParams",
    "MarkdownParams",
    "ParseParams",
    "ParseParamsCustomParser",
    "ParseParamsCustomParserRules",
    "ParseParamsCustomParserRulesUnionMember1",
    "ParseParamsPrebuiltParser",
    "ProductParams",
    "ScreenshotParams",
    "ScreenshotParamsArea",
    "ScreenshotParamsAreaElement",
    "ScreenshotParamsAreaRectangle",
    "SharedParams",
    "SharedParamsAction",
    "SharedParamsActionPerform",
    "SharedParamsActionScroll",
    "SharedParamsActionWait",
    "SharedParamsActionWaitFor",
    "SharedParamsParsers",
    "SharedParamsParsersPdf",
    "SharedParamsProfile",
    "SharedParamsProfileExisting",
    "SharedParamsProfileNew",
    "SharedParamsViewport",
    "TimeoutOpts",
]


class WebScrapeParams(TypedDict, total=False):
    formats: Required[Formats]
    """Outputs to return. Set at least one to `true`."""

    url: Required[str]
    """Public HTTP or HTTPS URL to scrape."""

    highlights_params: Annotated[HighlightsParams, PropertyInfo(alias="highlightsParams")]
    """Query for the `highlights` output.

    Required when `formats.highlights` is `true`, and allowed only then.
    """

    image_params: Annotated[ImageParams, PropertyInfo(alias="imageParams")]
    """Options for the `images` output. Requires `formats.images: true`."""

    json_params: Annotated[JsonParams, PropertyInfo(alias="jsonParams")]
    """Schema and instructions for the `json` output.

    Required when `formats.json` is `true`, and allowed only then.
    """

    markdown_params: Annotated[MarkdownParams, PropertyInfo(alias="markdownParams")]
    """Options for the `markdown` output. Requires `formats.markdown: true`."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached result, in milliseconds.

    `0` always fetches fresh. Defaults to 3 days (259200000 ms). Maximum: 1 year
    (31536000000 ms).
    """

    parse_params: Annotated[ParseParams, PropertyInfo(alias="parseParams")]
    """Custom rules or a prebuilt parser for the `parsed` output.

    Required when `formats.parse` is `true`, and allowed only then.
    """

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    product_params: Annotated[ProductParams, PropertyInfo(alias="productParams")]
    """Options for the `product` output. Requires `formats.product: true`."""

    screenshot_params: Annotated[ScreenshotParams, PropertyInfo(alias="screenshotParams")]
    """Options for the `screenshot` output. Requires `formats.screenshot: true`."""

    shared_params: Annotated[SharedParams, PropertyInfo(alias="sharedParams")]
    """Browser and content settings shared by all outputs."""

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Formats(TypedDict, total=False):
    """Outputs to return. Set at least one to `true`."""

    bytes: bool
    """Return the original HTTP response body."""

    highlights: bool
    """Return Markdown excerpts relevant to `highlightsParams.query`."""

    html: bool
    """Return the rendered HTML."""

    images: bool
    """Return the images found on the page."""

    json: bool
    """
    Return an object matching `jsonParams.schema`, extracted from the page text and
    embedded data such as JSON-LD, meta tags, and framework state.
    """

    markdown: bool
    """Return the page content, or a video transcript, as Markdown."""

    parse: bool
    """Return fields extracted with custom rules or a prebuilt parser, as `parsed`."""

    product: bool
    """Return product details such as name, price, and availability."""

    screenshot: bool
    """Return a screenshot of the page."""


class HighlightsParams(TypedDict, total=False):
    """Query for the `highlights` output.

    Required when `formats.highlights` is `true`, and allowed only then.
    """

    query: Required[str]
    """Question or topic to find relevant passages for."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of the returned passages, in characters."""


class ImageParams(TypedDict, total=False):
    """Options for the `images` output. Requires `formats.images: true`."""

    dedupe: Literal["none", "visual"]
    """Set to `visual` to drop visually duplicate images, keeping the largest copy."""

    enrich: List[Literal["dimensions", "classification", "file"]]
    """
    Extra data to add to each image: `dimensions` adds `width` and `height`,
    `classification` adds `classification`, and `file` adds a hosted `fileUrl`.
    """


class JsonParams(TypedDict, total=False):
    """Schema and instructions for the `json` output.

    Required when `formats.json` is `true`, and allowed only then.
    """

    schema: Required[Dict[str, object]]
    """JSON Schema for the object to extract, not an example object.

    Must describe a top-level object, up to 50 KB. Make fields optional or nullable
    when the page may not state them.
    """

    instructions: str
    """Extra guidance, such as which facts to prefer or how to read a field."""


class MarkdownParams(TypedDict, total=False):
    """Options for the `markdown` output. Requires `formats.markdown: true`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown (`html-conversion` only)."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown (`html-conversion` only)."""

    inline_images: Annotated[Literal["placeholder", "preserve"], PropertyInfo(alias="inlineImages")]
    """
    How to write base64 images when `includeImages` is `true`: `placeholder`
    shortens the data, `preserve` keeps it in full (`html-conversion` only).
    """

    source_preference: Annotated[
        List[Literal["html-conversion", "markdown-direct"]], PropertyInfo(alias="sourcePreference")
    ]
    """
    Markdown sources in order of preference: `html-conversion` converts the page
    HTML, `markdown-direct` uses Markdown the site publishes.
    """


class ParseParamsCustomParserRulesUnionMember1(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to match within the current page or parent rule."""

    output: Union[Literal["text", "html"], str, object]
    """
    What to return: `text`, `html`, an attribute such as `@href`, or nested field
    rules. Defaults to `text`.
    """

    type: Literal["item", "list"]
    """Return the first match with `item` or all matches with `list`."""


ParseParamsCustomParserRules: TypeAlias = Union[str, ParseParamsCustomParserRulesUnionMember1]


class ParseParamsCustomParser(TypedDict, total=False):
    rules: Required[Dict[str, ParseParamsCustomParserRules]]
    """
    Output field names mapped to a CSS selector (such as `h1` or `a@href`) or a rule
    object. Up to 100 fields, nested up to 5 levels.
    """

    type: Literal["custom"]
    """Extract fields with custom CSS rules. The default when `type` is omitted."""


class ParseParamsPrebuiltParser(TypedDict, total=False):
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
    ]
    """Prebuilt parser to run.

    Each one accepts specific URLs and returns its result in `parsed.data`.
    `emails`, `phone-numbers`, and `links` read the rendered page and respect
    content filters; the others read their source directly, independently of content
    filters and other outputs.

    - `google-maps`: Google Maps place, search, and internal data URLs. Returns
      businesses in `data.results`; a search URL returns up to 200 places. Results
      use the country set in the URL, or the US when none is set, and come back with
      English labels.
    - `google-maps-reviews`: Google Maps place, search, and `?cid=` URLs, plus
      `search.google.com/local/reviews` URLs, so the `google_maps_url` and
      `google_reviews_url` fields of `google-maps` results work as input. Returns
      the reviews of the place in `data.reviews` (`rating`, `date`, `isoDate`,
      `snippet`, `translatedSnippet`, `likes`, `user`, `media`, `response`, `link`,
      `id`, `language`, guided ratings in `details`, and `user.isLocalGuide`), plus
      the place `featureId`, `cid`, and `sort` in `data`. `sort` and `limit` set the
      order and count; `oldest` is exact. An unknown place returns no reviews.
    - `google-play`: Play Store app details URLs
      (`play.google.com/store/apps/details?id=…`). Returns one app in `data`:
      details, developer contact, ratings, price, permissions, data safety, the
      storefront country the record describes, and `is_available` (whether the app
      is offered there). Ratings are counted per storefront, so `rating`,
      `rating_count`, and `rating_histogram` are `null` where nobody rated the app.
      The language and storefront country set in the URL apply (default English and
      the US); without a storefront country, an app not offered in the US is read
      from the country of its developer.
    - `google-play-reviews`: Same URLs as `google-play`. Returns up to the 200
      newest reviews in the language set in the URL, with developer replies, in
      `data.reviews`; an app with fewer such reviews returns them all.
    - `app-store`: App Store app URLs (`apps.apple.com/us/app/…/id…`). Returns one
      app in `data`: details, developer, ratings, price, version, and screenshots.
      The country in the path sets the storefront (default `us`).
    - `app-store-reviews`: Same URLs as `app-store`. Returns up to the 500 newest
      reviews in `data.reviews`.
    - `g2-reviews`: G2 product URLs (`g2.com/products/…`), following renamed
      products. Returns the 25 most recently published reviews in `data.reviews`
      (rating, title, likes, dislikes, `problems_solved`, reviewer role, company
      size, and industry), plus `data.product`. Keeps star-rating filters from the
      URL (`filters[nps_score][]=1` to `5`) and ignores other filters, sort orders,
      and pages.
    - `instagram-profile`: Public profile URLs (`instagram.com/{username}`). Returns
      one profile in `data`: bio, links, follower and post counts, category,
      business address, `similar_accounts`, and `latest_posts` (up to the 12 posts
      at the top of the profile, newest first). Instagram lists pinned posts first,
      so posts with `is_pinned: true` can be older. When Instagram shows only a
      rounded post count (such as 32K), `post_count` is that rounded number and
      `is_post_count_rounded` is `true`.
    - `instagram-post`: Post and reel URLs (`/p/…`, `/reel/…`). Returns one post in
      `data`: caption, hashtags, mentions, like, comment, and view counts
      (`like_count` and `view_count` are `null` when the owner hides them), media
      URLs, tagged users, collaborators, location, and about the top 14 comments in
      `data.comments`.
    - `instagram-feed`: Hashtag and keyword URLs (`/explore/tags/…`, `/popular/…`)
      return the top posts; location URLs (`/explore/locations/{id}/…`) return
      recent posts. Posts are in `data.posts`; keyword posts carry only the
      shortcode, owner, thumbnail, and views, plus the caption when Instagram shows
      it. All three Instagram parsers read public data without signing in, so
      private accounts return no posts and follower lists are unavailable.
    - `tiktok-profile`: Public profile URLs (`tiktok.com/@{username}`). Returns one
      profile in `data`: nickname, bio, bio link, follower, following, like, and
      video counts, verified, private, and business flags, and business category.
      Does not list videos.
    - `tiktok-video`: Video and photo post URLs (`/@{username}/video/{id}`,
      `/@{username}/photo/{id}`). Returns one post in `data`: caption, hashtags,
      mentions, author, view, like, comment, share, save, and repost counts,
      duration, thumbnail, a `video_url` that downloads without cookies,
      `image_urls` for photo posts, music, location, and ad, paid-partnership, and
      AI-generated flags.
    - `tiktok-feed`: Returns videos in the `tiktok-video` shape in `data.videos`:
      the latest 15 from a profile URL, the top 30 from a hashtag URL
      (`/tag/{name}`), or the top 12 from a search URL (`/search?q={query}`).
    - `tiktok-comments`: Video and photo post URLs. Returns the first 20 comments in
      `data.comments`: text, `posted_at`, like and reply counts, whether the author
      liked it, and the commenter.
    - `tiktok-followers`, `tiktok-following`: Profile URLs. Return up to 30 accounts
      in `data.users`, in the `tiktok-profile` shape.
    - `tiktok-user-search`: User search URLs (`/search/user?q={query}`). Returns the
      top 10 accounts in `data.users`: `id`, `username`, `nickname`, `biography`,
      `avatar_url`, `sec_uid`, `follower_count`, `like_count`, and `is_verified`.
      The TikTok parsers accept `tiktok.com`, `www.tiktok.com`, and `m.tiktok.com`
      URLs, not short links (`vm.tiktok.com`, `vt.tiktok.com`, `tiktok.com/t/…`).
    - `reddit-post`: Post URLs (`reddit.com/r/{subreddit}/comments/{id}`,
      `reddit.com/comments/{id}`, `redd.it/{id}`). Returns the post in `data.post`:
      title, body as Markdown, type (`text`, `link`, `image`, `gallery`, or
      `video`), `link_url`, subreddit, author, flairs, score, `upvote_ratio`,
      comment and crosspost counts, NSFW, spoiler, locked, stickied, and archived
      flags, images (every gallery image in order), and video (an MP4 `url` plus an
      `hls_url` that carries the audio). `data.comments` holds the comment tree;
      each comment has `id`, `author`, `body` (Markdown), `score`, `posted_at`,
      `depth`, `parent_id`, `url`, `is_submitter`, `is_deleted`, and its `replies`.
      `limit` caps the total number of comments (default 100), filled shallowest
      first so whole conversations are kept, and `data.has_more_comments` says
      whether the thread has more. The `sort` in the URL (`best`, `top`, `new`,
      `controversial`, `old`, `qa`) orders the comments.
    - `reddit-search`: Search URLs (`reddit.com/search?q={query}`, or
      `reddit.com/r/{subreddit}/search?q={query}` to search one subreddit). With
      `type=link` or no `type`, returns posts in the `reddit-post` shape in
      `data.posts`, ordered by the `sort` in the URL (`relevance`, `hot`, `top`,
      `new`, `comments`) within its `t` time range (`hour`, `day`, `week`, `month`,
      `year`, `all`). `type=sr` returns communities in `data.communities` (name,
      title, description, sidebar, `subscriber_count`, `created_at`, type, NSFW and
      quarantine flags, language, category, icon and banner URLs, and allowed post
      types). `type=user` returns accounts in `data.users` (username,
      `display_name`, bio, `created_at`, post and comment karma, avatar and banner
      URLs, and verified, employee, moderator, premium, and NSFW flags). `limit`
      caps the number of results (default 100), in the order Reddit returns them,
      and `data.has_more` says whether Reddit has more.
    - `reddit-subreddit`: Subreddit URLs (`reddit.com/r/{subreddit}`, optionally
      followed by `/hot`, `/new`, `/top`, `/rising`, or `/controversial`, with `t`
      setting the time range of `top` and `controversial`, default `day`). Returns
      `data.subreddit` in the community shape of `reddit-search`, `data.rules`
      (`name`, `description`, `applies_to`, `violation_reason`, `created_at`), and
      `data.posts` in the `reddit-post` shape, ordered like the tab (default `hot`)
      with stickied posts flagged. `r/all` and `r/popular` return posts with `null`
      `subreddit` and `rules`. `limit` caps the posts (default 100) and
      `data.has_more` says whether Reddit has more. Private and quarantined
      subreddits return `WEBSITE_ACCESS_ERROR`.
    - `reddit-user`: Profile URLs (`reddit.com/user/{username}` or
      `reddit.com/u/{username}`, optionally followed by `/overview`, `/submitted`,
      or `/comments`, with `sort` set to `new`, `hot`, `top`, or `controversial` and
      `t` setting the time range of `top` and `controversial`, default `all`).
      Returns `data.user` (`id`, `username`, `display_name`, bio, `created_at`,
      total, post, comment, awardee, and awarder karma, avatar and banner URLs, and
      verified, suspended, employee, moderator, premium, and NSFW flags),
      `data.trophies` (`name`, `description`, `icon_url`, `granted_at`, `url`),
      `data.moderated_communities` (`name`, `title`, `url`, `subscriber_count`,
      `icon_url`, `is_nsfw`), `data.posts` in the `reddit-post` shape, and
      `data.comments`, each with `id`, `author`, `body` (Markdown), `score`,
      `posted_at`, `edited_at`, `url`, `subreddit`, `parent_id` (`null` for a
      top-level comment), `is_submitter`, `is_stickied`, `distinguished`,
      `award_count`, and the post it was left on (`id`, `title`, `url`, `author`,
      `is_nsfw`). The overview tab returns both posts and comments; `submitted`
      returns `null` comments and `comments` returns `null` posts. `limit` caps
      posts and comments together (default 100) and `data.has_more` says whether
      Reddit has more. Users who hide their activity return empty lists, and
      suspended accounts return their profile with `null` posts and comments.
    - `yelp-search`: Yelp search URLs with `find_desc` and `find_loc`; `start` sets
      the result offset. Returns up to 20 ranked organic businesses in
      `data.businesses`, with `total` and `pagination`.
    - `yelp-reviews`: Yelp business URLs (`yelp.com/biz/{alias}`); optional `start`
      sets the offset. Returns up to 20 of the latest public reviews, always newest
      first, in `data.reviews`, with business details and `pagination.next_offset`.
      Each review has rating, full text, `updated_at`, and author (`id` from the
      reviewer profile URL, `url` linking to that profile, `name`, `location`, and
      `review_count`); owner replies and photos are not included. Unsupported sort
      and review filters are rejected; tracking parameters are ignored.
    - `tripadvisor-reviews`: Tripadvisor hotel, restaurant, and attraction review
      URLs (`tripadvisor.com/Hotel_Review-g{geo}-d{id}-Reviews-….html`, on any
      Tripadvisor country domain); `-or{N}-` in the path sets the offset. Returns 20
      reviews in `data.reviews` in the order Tripadvisor shows them, with
      `data.location` (`id`, `name`, `type`, `url`, `review_count`) and
      `pagination.next_offset`. Each review has `id`, `url`, `title`, full text,
      `rating`, `language`, `published_at`, `visit_month`, `helpful_votes`,
      `subratings`, `photo_urls`, `owner_response` (`text`, `published_at`,
      `author_name`), and `author` (`id`, `username`, `name`, `url`,
      `contribution_count`). An unknown location returns no reviews.
    - `car-rental-availability`: avis.com and budget.com vehicle-availability search
      URLs. Returns every vehicle with pay-now and pay-later prices in
      `data.vehicles`.
    - `car-rental-locations`: avis.com and budget.com `/locations?keyword=` URLs.
      Returns rental branches with codes, addresses, coordinates, and hours in
      `data.locations`.
    - `emails`: Any page. Returns its email addresses in `data.emails`
      (`[{ email }]`), read from `mailto:` links, Cloudflare-protected addresses,
      and visible text.
    - `phone-numbers`: Any page. Returns its valid phone numbers in E.164 format in
      `data.phone_numbers` (`[{ phone }]`), read from `tel:` links and visible text.
      Numbers without a country code are read for the country of the site TLD (US by
      default).
    - `links`: Any page. Returns its unique HTTP and HTTPS links as absolute URLs in
      `data.links` (`[{ url, text }]`). `text` falls back to `aria-label` or image
      alt text and is `null` when a link has none.
    """

    type: Required[Literal["prebuilt"]]
    """Use a prebuilt parser instead of custom rules."""

    limit: int
    """
    Maximum number of reviews (`google-maps-reviews`, default 100), comments
    (`reddit-post`, default 100), or results (`reddit-search`, `reddit-subreddit`,
    and `reddit-user`, default 100) to return. Only these parsers accept it.
    """

    sort: Literal["newest", "oldest", "relevant", "highest", "lowest"]
    """Order of `data.reviews` for `google-maps-reviews`.

    `newest`, `relevant`, `highest`, and `lowest` use the same orders as Google
    Maps; `oldest` returns the earliest reviews first.
    """


ParseParams: TypeAlias = Union[ParseParamsCustomParser, ParseParamsPrebuiltParser]


class ProductParams(TypedDict, total=False):
    """Options for the `product` output. Requires `formats.product: true`."""

    dedupe_images: Annotated[bool, PropertyInfo(alias="dedupeImages")]
    """Drop visually duplicate product images, keeping the largest copy."""

    use_ai_fallback: Annotated[bool, PropertyInfo(alias="useAIFallback")]
    """Ignored. The AI fallback runs automatically."""


class ScreenshotParamsAreaElement(TypedDict, total=False):
    selector: Required[str]
    """CSS selector matching exactly one visible element."""


class ScreenshotParamsAreaRectangle(TypedDict, total=False):
    """Rectangle to capture, in pixels from the document origin."""

    height: Required[int]
    """Height of the capture in pixels."""

    width: Required[int]
    """Width of the capture in pixels."""

    x: Required[int]
    """Left edge of the capture, in pixels from the document origin."""

    y: Required[int]
    """Top edge of the capture, in pixels from the document origin."""


ScreenshotParamsArea: TypeAlias = Union[
    Literal["viewport", "fullPage"], ScreenshotParamsAreaElement, ScreenshotParamsAreaRectangle
]


class ScreenshotParams(TypedDict, total=False):
    """Options for the `screenshot` output. Requires `formats.screenshot: true`."""

    area: ScreenshotParamsArea
    """What to capture: `viewport`, `fullPage`, one element, or a rectangle.

    Up to 40 megapixels.
    """

    format: Literal["png", "jpeg", "webp"]
    """Image format for the screenshot."""


class SharedParamsActionPerform(TypedDict, total=False):
    action: Required[str]
    """One browser instruction, such as clicking a button or entering text."""

    type: Required[Literal["perform"]]
    """Follow a plain-language instruction."""


class SharedParamsActionScroll(TypedDict, total=False):
    type: Required[Literal["scroll"]]
    """Scroll the page or a container."""

    amount: Union[int, Literal["viewport", "max"]]
    """
    Distance per scroll step: a number of pixels, one `viewport`, or `max` to reach
    the end.
    """

    direction: Literal["down", "up", "left", "right"]
    """Direction to scroll."""

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]
    """Maximum number of scroll steps for this action."""

    selector: str
    """CSS selector of the container to scroll. Omit to scroll the page."""


class SharedParamsActionWait(TypedDict, total=False):
    milliseconds: Required[int]
    """How long to pause before the next action, in milliseconds."""

    type: Required[Literal["wait"]]
    """Pause for a fixed time."""


class SharedParamsActionWaitFor(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to wait for before continuing."""

    type: Required[Literal["waitFor"]]
    """Wait for an element matching `selector`."""


SharedParamsAction: TypeAlias = Union[
    SharedParamsActionPerform, SharedParamsActionScroll, SharedParamsActionWait, SharedParamsActionWaitFor
]


class SharedParamsParsersPdf(TypedDict, total=False):
    """Page range, OCR, and page markers for PDFs."""

    end_page: Annotated[int, PropertyInfo(alias="endPage")]
    """Last page to parse. Defaults to the last page. Must be at least `startPage`."""

    include_numbered_pages: Annotated[bool, PropertyInfo(alias="includeNumberedPages")]
    """
    Start each PDF page in the Markdown with a `<!-- page N -->` line, where `N` is
    the original 1-based page number. These responses are never served from cache.
    """

    ocr: Literal["off", "auto"]
    """Set to `auto` to read scanned pages with OCR. Adds 1 credit per page read."""

    start_page: Annotated[int, PropertyInfo(alias="startPage")]
    """First page to parse, starting at 1."""


class SharedParamsParsers(TypedDict, total=False):
    """Options for parsing documents such as PDFs."""

    pdf: SharedParamsParsersPdf
    """Page range, OCR, and page markers for PDFs."""


class SharedParamsProfileExisting(TypedDict, total=False):
    profile_id: Required[Annotated[str, PropertyInfo(alias="profileId")]]
    """ID of the browser profile, from `profile.id` in an earlier scrape response."""

    type: Required[Literal["existing"]]
    """Reuse a saved browser profile."""


class SharedParamsProfileNew(TypedDict, total=False):
    identifier: Required[str]
    """Username or email address for the website."""

    password: Required[str]
    """Password for the website. Used to sign in and never stored."""

    type: Required[Literal["new"]]
    """Sign in and save a new browser profile."""

    description: str
    """Label for the profile, shown by `GET /org/browser/profiles`."""


SharedParamsProfile: TypeAlias = Union[SharedParamsProfileExisting, SharedParamsProfileNew]


class SharedParamsViewport(TypedDict, total=False):
    """Browser viewport in pixels.

    Defaults to 1920 × 1080. If you pass `viewport`, a missing `width` defaults to 1440 and a missing `height` to 900.
    """

    height: int
    """Browser viewport height in pixels."""

    width: int
    """Browser viewport width in pixels."""


class SharedParams(TypedDict, total=False):
    """Browser and content settings shared by all outputs."""

    actions: Iterable[SharedParamsAction]
    """Browser steps to run in order before capture.

    Requires a paid plan. Skips the cache.
    """

    country: str
    """Country to fetch from, as an ISO 3166-1 alpha-2 code such as `US`.

    Case-insensitive.
    """

    dismiss_cookies: Annotated[bool, PropertyInfo(alias="dismissCookies")]
    """Accept cookie banners before actions and capture."""

    dismiss_popups: Annotated[bool, PropertyInfo(alias="dismissPopups")]
    """Close other popups before actions and capture."""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors. Overrides `includeSelectors`."""

    headers: Dict[str, str]
    """HTTP headers to send to the target site. Requests with headers skip the cache."""

    include_frames: Annotated[Union[bool, Literal["auto"]], PropertyInfo(alias="includeFrames")]
    """Which iframes to inline in HTML and text outputs.

    Screenshots always show visible frames. `auto` inlines only iframes that hold
    page content, such as same-site documents, framesets, job boards, forms, and
    embedded documents, and skips ads and widgets. `true` inlines every iframe;
    `false` inlines none.
    """

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors."""

    main_content_only: Annotated[bool, PropertyInfo(alias="mainContentOnly")]
    """Keep only the main content, without navigation, headers, footers, or sidebars.

    Does not affect `screenshot`, `bytes`, or `product`.
    """

    parsers: SharedParamsParsers
    """Options for parsing documents such as PDFs."""

    profile: SharedParamsProfile
    """Scrape as a signed-in user.

    Create a profile with `type: "new"` and your credentials, then reuse it with
    `type: "existing"`. Requires a paid plan and an HTTPS URL. Profiles keep their
    session between requests, skip the cache, and cannot be combined with ZDR,
    custom headers, `formats.bytes`, or prebuilt parsers other than `emails`,
    `phone-numbers`, and `links`.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before capture.

    Defaults to `true` when `formats.screenshot` is `true`.
    """

    theme: Literal["light", "dark"]
    """Emulate a light or dark color scheme."""

    viewport: SharedParamsViewport
    """Browser viewport in pixels.

    Defaults to 1920 × 1080. If you pass `viewport`, a missing `width` defaults to
    1440 and a missing `height` to 900.
    """

    wait_for: Annotated[Union[int, str], PropertyInfo(alias="waitFor")]
    """Time to wait after actions, in milliseconds, or a CSS selector to wait for.

    Defaults to 500 ms, or 2000 ms when `includeFrames` is `true` or the URL ends in
    `.xml`.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial. `return-partial` requires at least 5000 ms. On `POST /web/scrape`, an
    output that is not ready in time fails with `REQUEST_TIMEOUT` inside a 200
    response under either behavior; 408 means the whole request could not respond by
    the deadline.
    """
