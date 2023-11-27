import uvicorn
from fastapi import FastAPI
from routers import travel

app = FastAPI(
    title="Should I go there?",
    docs_url="/api/docs"
)

app.include_router(prefix="/api/v1", router=travel.router)

@app.get("/")
async def root() -> None:
    """
    Root endpoint.
    """
    return {"message": "Connection Successful"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
