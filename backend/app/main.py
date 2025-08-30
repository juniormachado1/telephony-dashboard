from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router

app = FastAPI(
    title="Telephony Dashboard API",
    description="API para gerenciar usuários e dados de telefonia.",
    version="0.1.0"
)

origins = [
    "http://localhost",
    "http://localhost:3000", # Frontend React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
def read_root():
    return {"status": "API is running!"}