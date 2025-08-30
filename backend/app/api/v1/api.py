from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, calls, metrics

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(calls.router, prefix="/calls", tags=["Calls"])
api_router.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
