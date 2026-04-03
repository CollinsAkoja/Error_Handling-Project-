from flask import Flask, jsonify
from api_error_handling import register_flask_error_handlers, setup_logger, BadRequestError, NotFoundError

logger = setup_logger("flask_api")
app = Flask(__name__)
register_flask_error_handlers(app, logger=logger, include_trace=False)

@app.route("/api/items/<item_id>")
def get_item(item_id):
    if item_id == "0":
        raise BadRequestError("item_id cannot be 0", details={"integrity": "invalid_id"})
    if item_id != "42":
        raise NotFoundError("Item not found", details={"item_id": item_id})
    return jsonify({"id": 42, "name": "The Answer"})

@app.route("/api/boom")
def boom():
    raise Exception("unexpected failure")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
