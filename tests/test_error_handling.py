import pytest
from api_error_handling import BadRequestError, NotFoundError, format_error_response, format_generic_error_response


def test_bad_request_error_properties():
    err = BadRequestError("bad request", details={"field": "x"})
    body = err.to_dict()
    assert err.status_code == 400
    assert body["error"]["code"] == "bad_request"
    assert body["error"]["message"] == "bad request"
    assert body["error"]["details"] == {"field": "x"}


def test_format_error_response_content():
    err = NotFoundError("nope")
    payload = format_error_response(err, request_path="/api/items/1")
    assert payload["status"] == 404
    assert payload["path"] == "/api/items/1"
    assert payload["error"]["code"] == "not_found"


def test_format_generic_error_response_from_standard_exception():
    exc = ValueError("boom")
    payload = format_generic_error_response(exc, request_path="/api/test")
    assert payload["status"] == 500
    assert payload["error"]["code"] == "api_error"
    assert "boom" in payload["error"]["message"]


if __name__ == "__main__":
    pytest.main(["-q"])
