"""Application entry point for the FastAPI backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

app = FastAPI(title="CubeVI API", version="0.1.0")

# CORS allows the Vite frontend on localhost:5173 to call this API in development.
# TODO: replace this development allow-list with the deployed frontend origin later.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# The router keeps URL definitions out of this startup file.
app.include_router(router, prefix="/api")

