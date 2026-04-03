import datetime
import traceback
from .exceptions import ApiError


def format_error_response(error: ApiError, request_path: str = None, include_trace: bool = False):
    payload = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "status": error.status_code,
        "path": request_path,
        "error": {
            "type": error.__class__.__name__,
            "code": error.error_code,
            "message": error.message,
        },
    }

    if error.details is not None:
        payload["error"]["details"] = error.details

    if include_trace and not isinstance(error, ApiError):
        payload["debug"] = traceback.format_exc()

    return payload


def format_generic_error_response(exc: Exception, request_path: str = None, include_trace: bool = False):
    error = ApiError(str(exc) if str(exc) else "Unexpected error")
    result = format_error_response(error, request_path=request_path, include_trace=include_trace)
    if include_trace:
        result["debug"] = traceback.format_exc()
    return result
