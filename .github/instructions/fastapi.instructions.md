---
applyTo: "src/**/api/**/*.py"
---

# FastAPI — CareerDEX Specifics

## Routing & Responses
- Versioned routes: `APIRouter(prefix="/api/v1", tags=["v1"])`
- Declare `response_model=` on every endpoint
- Pydantic models for all request/response shapes
- Custom `custom_openapi()` in main.py for schema customization

## Lifespan & Middleware
- `@asynccontextmanager` lifespan for startup/shutdown
- Middleware stack (order matters): request logging → metrics → auth → rate limit
- Uses `BaseHTTPMiddleware` — keeps cross-cutting logic out of route signatures
- 3 global exception handlers: `RequestValidationError`, `StarletteHTTPException`, catch-all `Exception`

## Key Files
- `src/careerdex/api/main.py` — App entry point
- `src/careerdex/api/routers/ml.py` — ML model serving
- `src/careerdex/api/routers/v1.py` — Data pipeline & quality endpoints
- `src/careerdex/phases/phase5_api_services.py` — CareerDEX-specific endpoints

## Port
- CareerDEX runs on port **17003**
