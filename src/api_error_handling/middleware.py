from fastapi import Request as FastAPIRequest
from fastapi.responses import JSONResponse
from flask import jsonify
from .exceptions import ApiError
from .responses import format_error_response


def register_flask_error_handlers(app, logger=None, include_trace=False):
    logger = logger or __import__("logging").getLogger(__name__)

    @app.errorhandler(ApiError)
    def handle_api_error(exc):
        logger.error("ApiError caught", exc_info=exc)
        payload = format_error_response(exc, request_path=getattr(__import__("flask").request, "path", None), include_trace=include_trace)
        response = jsonify(payload)
        response.status_code = exc.status_code
        return response

    @app.errorhandler(Exception)
    def handle_unhandled_exception(exc):
        logger.exception("Unhandled exception")
        error = ApiError("Internal server error")
        payload = format_error_response(error, request_path=getattr(__import__("flask").request, "path", None), include_trace=include_trace)
        response = jsonify(payload)
        response.status_code = 500
        return response


def add_fastapi_exception_handlers(app, logger=None, include_trace=False):
    logger = logger or __import__("logging").getLogger(__name__)

    @app.exception_handler(ApiError)
    async def api_error_handler(request: FastAPIRequest, exc: ApiError):
        logger.error("ApiError caught", exc_info=exc, extra={"path": request.url.path})
        payload = format_error_response(exc, request_path=str(request.url.path), include_trace=include_trace)
        return JSONResponse(status_code=exc.status_code, content=payload)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: FastAPIRequest, exc: Exception):
        logger.exception("Unhandled exception", exc_info=exc, extra={"path": request.url.path})
        error = ApiError("Internal server error")
        payload = format_error_response(error, request_path=str(request.url.path), include_trace=include_trace)
        return JSONResponse(status_code=500, content=payload)
