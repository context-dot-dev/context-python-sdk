# Parse

Types:

```python
from context.dev.types import ParseHandleResponse
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/context/dev/resources/parse.py">handle</a>(body, \*\*<a href="src/context/dev/types/parse_handle_params.py">params</a>) -> <a href="./src/context/dev/types/parse_handle_response.py">ParseHandleResponse</a></code>

# Web

Types:

```python
from context.dev.types import (
    WebAnswersResponse,
    WebExtractCompetitorsResponse,
    WebExtractStyleguideResponse,
    WebMapURLsResponse,
    WebScrapeResponse,
    WebScreenshotResponse,
    WebSearchResponse,
    WebWebCrawlMdResponse,
)
```

Methods:

- <code title="post /web/answers">client.web.<a href="./src/context/dev/resources/web.py">answers</a>(\*\*<a href="src/context/dev/types/web_answers_params.py">params</a>) -> <a href="./src/context/dev/types/web_answers_response.py">WebAnswersResponse</a></code>
- <code title="get /web/competitors">client.web.<a href="./src/context/dev/resources/web.py">extract_competitors</a>(\*\*<a href="src/context/dev/types/web_extract_competitors_params.py">params</a>) -> <a href="./src/context/dev/types/web_extract_competitors_response.py">WebExtractCompetitorsResponse</a></code>
- <code title="get /web/styleguide">client.web.<a href="./src/context/dev/resources/web.py">extract_styleguide</a>(\*\*<a href="src/context/dev/types/web_extract_styleguide_params.py">params</a>) -> <a href="./src/context/dev/types/web_extract_styleguide_response.py">WebExtractStyleguideResponse</a></code>
- <code title="get /web/urls">client.web.<a href="./src/context/dev/resources/web.py">map_urls</a>(\*\*<a href="src/context/dev/types/web_map_urls_params.py">params</a>) -> <a href="./src/context/dev/types/web_map_urls_response.py">WebMapURLsResponse</a></code>
- <code title="post /web/scrape">client.web.<a href="./src/context/dev/resources/web.py">scrape</a>(\*\*<a href="src/context/dev/types/web_scrape_params.py">params</a>) -> <a href="./src/context/dev/types/web_scrape_response.py">WebScrapeResponse</a></code>
- <code title="get /web/screenshot">client.web.<a href="./src/context/dev/resources/web.py">screenshot</a>(\*\*<a href="src/context/dev/types/web_screenshot_params.py">params</a>) -> <a href="./src/context/dev/types/web_screenshot_response.py">WebScreenshotResponse</a></code>
- <code title="post /web/search">client.web.<a href="./src/context/dev/resources/web.py">search</a>(\*\*<a href="src/context/dev/types/web_search_params.py">params</a>) -> <a href="./src/context/dev/types/web_search_response.py">WebSearchResponse</a></code>
- <code title="post /web/crawl">client.web.<a href="./src/context/dev/resources/web.py">web_crawl_md</a>(\*\*<a href="src/context/dev/types/web_web_crawl_md_params.py">params</a>) -> <a href="./src/context/dev/types/web_web_crawl_md_response.py">WebWebCrawlMdResponse</a></code>

# Brand

Types:

```python
from context.dev.types import BrandRetrieveResponse, BrandSearchResponse
```

Methods:

- <code title="post /brand/retrieve">client.brand.<a href="./src/context/dev/resources/brand.py">retrieve</a>(\*\*<a href="src/context/dev/types/brand_retrieve_params.py">params</a>) -> <a href="./src/context/dev/types/brand_retrieve_response.py">BrandRetrieveResponse</a></code>
- <code title="get /brand/search">client.brand.<a href="./src/context/dev/resources/brand.py">search</a>(\*\*<a href="src/context/dev/types/brand_search_params.py">params</a>) -> <a href="./src/context/dev/types/brand_search_response.py">BrandSearchResponse</a></code>

# Industry

Types:

```python
from context.dev.types import IndustryRetrieveNaicsResponse, IndustryRetrieveSicResponse
```

Methods:

- <code title="get /web/naics">client.industry.<a href="./src/context/dev/resources/industry.py">retrieve_naics</a>(\*\*<a href="src/context/dev/types/industry_retrieve_naics_params.py">params</a>) -> <a href="./src/context/dev/types/industry_retrieve_naics_response.py">IndustryRetrieveNaicsResponse</a></code>
- <code title="get /web/sic">client.industry.<a href="./src/context/dev/resources/industry.py">retrieve_sic</a>(\*\*<a href="src/context/dev/types/industry_retrieve_sic_params.py">params</a>) -> <a href="./src/context/dev/types/industry_retrieve_sic_response.py">IndustryRetrieveSicResponse</a></code>

# Utility

Types:

```python
from context.dev.types import UtilityPrefetchResponse
```

Methods:

- <code title="post /utility/prefetch">client.utility.<a href="./src/context/dev/resources/utility.py">prefetch</a>(\*\*<a href="src/context/dev/types/utility_prefetch_params.py">params</a>) -> <a href="./src/context/dev/types/utility_prefetch_response.py">UtilityPrefetchResponse</a></code>

# Monitors

Types:

```python
from context.dev.types import (
    WebhookDelivery,
    MonitorCreateResponse,
    MonitorRetrieveResponse,
    MonitorUpdateResponse,
    MonitorListResponse,
    MonitorDeleteResponse,
    MonitorGetCreditUsageResponse,
    MonitorGetLimitsResponse,
    MonitorListAccountChangesResponse,
    MonitorListAccountRunsResponse,
    MonitorListChangesResponse,
    MonitorListRunsResponse,
    MonitorRetrieveChangeResponse,
    MonitorRetrieveRunResponse,
    MonitorRotateWebhookSecretResponse,
    MonitorRunResponse,
)
```

Methods:

- <code title="post /monitors">client.monitors.<a href="./src/context/dev/resources/monitors.py">create</a>(\*\*<a href="src/context/dev/types/monitor_create_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_create_response.py">MonitorCreateResponse</a></code>
- <code title="get /monitors/{monitor_id}">client.monitors.<a href="./src/context/dev/resources/monitors.py">retrieve</a>(monitor_id) -> <a href="./src/context/dev/types/monitor_retrieve_response.py">MonitorRetrieveResponse</a></code>
- <code title="patch /monitors/{monitor_id}">client.monitors.<a href="./src/context/dev/resources/monitors.py">update</a>(monitor_id, \*\*<a href="src/context/dev/types/monitor_update_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_update_response.py">MonitorUpdateResponse</a></code>
- <code title="get /monitors">client.monitors.<a href="./src/context/dev/resources/monitors.py">list</a>(\*\*<a href="src/context/dev/types/monitor_list_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_list_response.py">MonitorListResponse</a></code>
- <code title="delete /monitors/{monitor_id}">client.monitors.<a href="./src/context/dev/resources/monitors.py">delete</a>(monitor_id) -> <a href="./src/context/dev/types/monitor_delete_response.py">MonitorDeleteResponse</a></code>
- <code title="get /monitors/credit-usage">client.monitors.<a href="./src/context/dev/resources/monitors.py">get_credit_usage</a>(\*\*<a href="src/context/dev/types/monitor_get_credit_usage_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_get_credit_usage_response.py">MonitorGetCreditUsageResponse</a></code>
- <code title="get /monitors/limits">client.monitors.<a href="./src/context/dev/resources/monitors.py">get_limits</a>() -> <a href="./src/context/dev/types/monitor_get_limits_response.py">MonitorGetLimitsResponse</a></code>
- <code title="get /monitors/changes">client.monitors.<a href="./src/context/dev/resources/monitors.py">list_account_changes</a>(\*\*<a href="src/context/dev/types/monitor_list_account_changes_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_list_account_changes_response.py">MonitorListAccountChangesResponse</a></code>
- <code title="get /monitors/runs">client.monitors.<a href="./src/context/dev/resources/monitors.py">list_account_runs</a>(\*\*<a href="src/context/dev/types/monitor_list_account_runs_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_list_account_runs_response.py">MonitorListAccountRunsResponse</a></code>
- <code title="get /monitors/{monitor_id}/changes">client.monitors.<a href="./src/context/dev/resources/monitors.py">list_changes</a>(monitor_id, \*\*<a href="src/context/dev/types/monitor_list_changes_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_list_changes_response.py">MonitorListChangesResponse</a></code>
- <code title="get /monitors/{monitor_id}/runs">client.monitors.<a href="./src/context/dev/resources/monitors.py">list_runs</a>(monitor_id, \*\*<a href="src/context/dev/types/monitor_list_runs_params.py">params</a>) -> <a href="./src/context/dev/types/monitor_list_runs_response.py">MonitorListRunsResponse</a></code>
- <code title="get /monitors/changes/{change_id}">client.monitors.<a href="./src/context/dev/resources/monitors.py">retrieve_change</a>(change_id) -> <a href="./src/context/dev/types/monitor_retrieve_change_response.py">MonitorRetrieveChangeResponse</a></code>
- <code title="get /monitors/{monitor_id}/runs/{run_id}">client.monitors.<a href="./src/context/dev/resources/monitors.py">retrieve_run</a>(run_id, \*, monitor_id) -> <a href="./src/context/dev/types/monitor_retrieve_run_response.py">MonitorRetrieveRunResponse</a></code>
- <code title="post /monitors/{monitor_id}/webhook/rotate-secret">client.monitors.<a href="./src/context/dev/resources/monitors.py">rotate_webhook_secret</a>(monitor_id) -> <a href="./src/context/dev/types/monitor_rotate_webhook_secret_response.py">MonitorRotateWebhookSecretResponse</a></code>
- <code title="post /monitors/{monitor_id}/run">client.monitors.<a href="./src/context/dev/resources/monitors.py">run</a>(monitor_id) -> <a href="./src/context/dev/types/monitor_run_response.py">MonitorRunResponse</a></code>

# Batch

Types:

```python
from context.dev.types import (
    PageErrorCount,
    Failure,
    CrawlControls,
    Intake,
    BatchRetrieveResponse,
    BatchListResponse,
    BatchDeleteResponse,
    BatchCancelResponse,
    BatchGetResultsResponse,
    BatchSubmitResponse,
)
```

Methods:

- <code title="get /batch/{batch_id}">client.batch.<a href="./src/context/dev/resources/batch.py">retrieve</a>(batch_id) -> <a href="./src/context/dev/types/batch_retrieve_response.py">BatchRetrieveResponse</a></code>
- <code title="get /batch/list">client.batch.<a href="./src/context/dev/resources/batch.py">list</a>(\*\*<a href="src/context/dev/types/batch_list_params.py">params</a>) -> <a href="./src/context/dev/types/batch_list_response.py">BatchListResponse</a></code>
- <code title="delete /batch/{batch_id}">client.batch.<a href="./src/context/dev/resources/batch.py">delete</a>(batch_id) -> <a href="./src/context/dev/types/batch_delete_response.py">BatchDeleteResponse</a></code>
- <code title="post /batch/{batch_id}/cancel">client.batch.<a href="./src/context/dev/resources/batch.py">cancel</a>(batch_id) -> <a href="./src/context/dev/types/batch_cancel_response.py">BatchCancelResponse</a></code>
- <code title="get /batch/{batch_id}/results">client.batch.<a href="./src/context/dev/resources/batch.py">get_results</a>(batch_id, \*\*<a href="src/context/dev/types/batch_get_results_params.py">params</a>) -> <a href="./src/context/dev/types/batch_get_results_response.py">BatchGetResultsResponse</a></code>
- <code title="post /batch/submit">client.batch.<a href="./src/context/dev/resources/batch.py">submit</a>(\*\*<a href="src/context/dev/types/batch_submit_params.py">params</a>) -> <a href="./src/context/dev/types/batch_submit_response.py">BatchSubmitResponse</a></code>

# Webhooks

Types:

```python
from context.dev.types import RetryConfig
```

## Deliveries

Types:

```python
from context.dev.types.webhooks import (
    Attempt,
    Delivery,
    DeliverySummary,
    DeliveryRetrieveResponse,
    DeliveryListResponse,
    DeliveryListAttemptsResponse,
    DeliveryRetryResponse,
)
```

Methods:

- <code title="get /webhooks/deliveries/{delivery_id}">client.webhooks.deliveries.<a href="./src/context/dev/resources/webhooks/deliveries.py">retrieve</a>(delivery_id, \*\*<a href="src/context/dev/types/webhooks/delivery_retrieve_params.py">params</a>) -> <a href="./src/context/dev/types/webhooks/delivery_retrieve_response.py">DeliveryRetrieveResponse</a></code>
- <code title="post /webhooks/deliveries">client.webhooks.deliveries.<a href="./src/context/dev/resources/webhooks/deliveries.py">list</a>(\*\*<a href="src/context/dev/types/webhooks/delivery_list_params.py">params</a>) -> <a href="./src/context/dev/types/webhooks/delivery_list_response.py">DeliveryListResponse</a></code>
- <code title="get /webhooks/deliveries/{delivery_id}/attempts">client.webhooks.deliveries.<a href="./src/context/dev/resources/webhooks/deliveries.py">list_attempts</a>(delivery_id, \*\*<a href="src/context/dev/types/webhooks/delivery_list_attempts_params.py">params</a>) -> <a href="./src/context/dev/types/webhooks/delivery_list_attempts_response.py">DeliveryListAttemptsResponse</a></code>
- <code title="post /webhooks/deliveries/{delivery_id}/retry">client.webhooks.deliveries.<a href="./src/context/dev/resources/webhooks/deliveries.py">retry</a>(delivery_id, \*\*<a href="src/context/dev/types/webhooks/delivery_retry_params.py">params</a>) -> <a href="./src/context/dev/types/webhooks/delivery_retry_response.py">DeliveryRetryResponse</a></code>

# People

Types:

```python
from context.dev.types import PersonEnrichResponse
```

Methods:

- <code title="post /people/enrich">client.people.<a href="./src/context/dev/resources/people.py">enrich</a>(\*\*<a href="src/context/dev/types/person_enrich_params.py">params</a>) -> <a href="./src/context/dev/types/person_enrich_response.py">PersonEnrichResponse</a></code>

# News

Types:

```python
from context.dev.types import NewsSearchResponse
```

Methods:

- <code title="post /news/search">client.news.<a href="./src/context/dev/resources/news.py">search</a>(\*\*<a href="src/context/dev/types/news_search_params.py">params</a>) -> <a href="./src/context/dev/types/news_search_response.py">NewsSearchResponse</a></code>

# Logs

Types:

```python
from context.dev.types import LogRetrieveResponse, LogListResponse
```

Methods:

- <code title="get /org/logs/{request_id}">client.logs.<a href="./src/context/dev/resources/logs.py">retrieve</a>(request_id) -> <a href="./src/context/dev/types/log_retrieve_response.py">LogRetrieveResponse</a></code>
- <code title="get /org/logs">client.logs.<a href="./src/context/dev/resources/logs.py">list</a>(\*\*<a href="src/context/dev/types/log_list_params.py">params</a>) -> <a href="./src/context/dev/types/log_list_response.py">LogListResponse</a></code>

# Feedback

Types:

```python
from context.dev.types import FeedbackSubmitResponse
```

Methods:

- <code title="post /feedback">client.feedback.<a href="./src/context/dev/resources/feedback.py">submit</a>(\*\*<a href="src/context/dev/types/feedback_submit_params.py">params</a>) -> <a href="./src/context/dev/types/feedback_submit_response.py">FeedbackSubmitResponse</a></code>
