# Billing API (internal)

Base URL: https://billing.internal.example/v2

## Limits

- 300 requests per minute per API token.
- Bursts above that return `429 Too Many Requests` with a `Retry-After` header (seconds).
