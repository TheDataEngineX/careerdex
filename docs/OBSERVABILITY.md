# Observability: Metrics, Logging & Tracing

Guide to monitoring, debugging, and understanding CareerDEX in production.

## Overview

CareerDEX implements observability using **Prometheus** for metrics, **OpenTelemetry** for distributed tracing, and **structlog** for structured logging — all provided by the dataenginex framework.

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  CareerDEX   │────→│  Prometheus  │────→│   Grafana    │
│  :8003       │     │  :9090       │     │   :3000      │
└──────┬───────┘     └──────────────┘     └──────────────┘
       │
       └──→ OTLP ──→ Jaeger :4317/:16686
```

## Prometheus Metrics

All metrics use the `http_` prefix:

| Metric | Type | Description |
|--------|------|-------------|
| `http_requests_total` | Counter | Total HTTP requests by method/path/status |
| `http_request_duration_seconds` | Histogram | Request latency distribution |
| `http_requests_in_progress` | Gauge | Currently active requests |

Access metrics: `GET /metrics`

## Structured Logging

- **API/middleware**: `structlog.get_logger(__name__)` with key-value pairs
- **ML/backend**: `from loguru import logger` with `logger.info("message %s", arg)`
- `X-Request-ID` propagated via `structlog.contextvars`

## Health Checks

| Endpoint | Purpose |
|----------|---------|
| `GET /health` | Liveness probe |
| `GET /ready` | Readiness probe (checks components) |
| `GET /startup` | Startup probe |

## Local Testing

```bash
# Start full observability stack
uv run poe docker-up

# Services:
# CareerDEX API:  http://localhost:8003
# Prometheus:     http://localhost:9090
# Grafana:        http://localhost:3000
# Jaeger UI:      http://localhost:16686
```

## Troubleshooting

1. **No metrics**: Check `/metrics` endpoint; verify PrometheusMetricsMiddleware is registered
1. **No traces**: Verify `OTEL_EXPORTER_OTLP_ENDPOINT` env var and Jaeger connectivity
1. **Missing request IDs**: Check RequestLoggingMiddleware is first in the middleware stack
