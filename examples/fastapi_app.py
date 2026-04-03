from fastapi import FastAPI
from api_error_handling import add_fastapi_exception_handlers, setup_logger, BadRequestError, NotFoundError

logger = setup_logger("fastapi_api")
app = FastAPI()
add_fastapi_exception_handlers(app, logger=logger, include_trace=False)

@app.get("/api/items/{item_id}")
async def get_item(item_id: int):
    if item_id == 0:
        raise BadRequestError("item_id cannot be 0", details={"integrity": "invalid_id"})
    if item_id != 42:
        raise NotFoundError("Item not found", details={"item_id": item_id})
    return {"id": 42, "name": "The Answer"}

@app.get("/api/boom")
async def boom():
    raise RuntimeError("unexpected failure")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
