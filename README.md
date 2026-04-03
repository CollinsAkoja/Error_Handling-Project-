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

## Author

**Collins Akoja**

## Development Challenges and Solutions

During the development of this API error handling system, several challenges were encountered and overcome:

1. **Module Import Issues in Tests**: Initially, pytest couldn't find the custom modules during testing. This was resolved by adding proper packaging metadata in `setup.py` and using editable installs (`pip install -e .`) to ensure the package is correctly installed in development mode.

2. **Ensuring Framework Consistency**: Maintaining consistent error handling behavior between Flask and FastAPI required careful design of the exception classes and response formatting. This was achieved by creating a unified `ApiError` base class with standardized attributes and a common `format_error_response` function that works across both frameworks.

3. **Middleware Integration**: Integrating error handlers as middleware for both Flask and FastAPI involved understanding their respective exception handling mechanisms. Flask uses error handler decorators, while FastAPI uses exception handlers. The solution was to create framework-specific registration functions that abstract these differences.

4. **Logging Integration**: Ensuring that logging works seamlessly with the error handling required designing a flexible logger interface that can be injected into the handlers. This allows for different logging configurations in production environments.

These challenges were overcome through iterative testing, research into framework-specific APIs, and modular design principles that separated concerns effectively.
