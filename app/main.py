from fastapi import FastAPI
from core.api.base import router as router_base
from contextlib import asynccontextmanager
from core.db.database import db
import uvicorn

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    try:
        print("Starting up...")
        # await db.create_indexes()
        yield
    finally:
        print("Shutting down...")

app = FastAPI(lifespan=app_lifespan)
# app = FastAPI()


app.include_router(router_base)

@app.get('/')
async def home():
    return {"pme": "2023"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8082, reload=True)
