import typing


class ApiError(Exception):
    """Base structured API error."""

    status_code = 500
    error_code = "api_error"

    def __init__(self, message: str = "Internal server error", *, error_code: typing.Optional[str] = None, status_code: typing.Optional[int] = None, details: typing.Optional[typing.Any] = None):
        self.message = message
        self.details = details
        if status_code is not None:
            self.status_code = status_code
        if error_code is not None:
            self.error_code = error_code

        super().__init__(message)

    def to_dict(self):
        obj = {
            "error": {
                "type": self.__class__.__name__,
                "code": self.error_code,
                "message": self.message,
            }
        }
        if self.details is not None:
            obj["error"]["details"] = self.details
        return obj


class BadRequestError(ApiError):
    status_code = 400
    error_code = "bad_request"


class NotFoundError(ApiError):
    status_code = 404
    error_code = "not_found"


class UnauthorizedError(ApiError):
    status_code = 401
    error_code = "unauthorized"


class ForbiddenError(ApiError):
    status_code = 403
    error_code = "forbidden"


class ConflictError(ApiError):
    status_code = 409
    error_code = "conflict"


class ValidationError(ApiError):
    status_code = 422
    error_code = "validation_error"


class ServiceUnavailableError(ApiError):
    status_code = 503
    error_code = "service_unavailable"
