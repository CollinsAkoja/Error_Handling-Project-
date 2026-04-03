# API Error Handling Upgrade (Python)

A production-ready error handling architecture for Python APIs, with:

- Custom structured exceptions (`ApiError`, `BadRequestError`, `ValidationError`, `NotFoundError`, etc.)
- Consistent JSON response schema
- Flask + FastAPI middleware integration
- Logging and exception detail support
- Example apps + tests

## Features

1. Custom API exceptions with status codes and machine-friendly error codes.
2. Generic & structured error responses using `format_error_response`.
3. Flask `register_flask_error_handlers(app, logger)`.
4. FastAPI `add_fastapi_exception_handlers(app, logger)`.
5. Confidence in production usage with clean bad request / not found / uncaught fallback.

## Install

```bash
python -m pip install -r requirements.txt
```

## Run examples

Flask:

```bash
python examples/flask_app.py
```

FastAPI:

```bash
python examples/fastapi_app.py
```

Or:

```bash
uvicorn examples.fastapi_app:app --reload
```

## Quick usage

```python
from api_error_handling import BadRequestError, register_flask_error_handlers

app = Flask(__name__)
register_flask_error_handlers(app)

@app.route("/demo")
def demo():
    raise BadRequestError("Invalid payload", details={"field": "name"})
```

## Testing

```bash
pytest -q
```
