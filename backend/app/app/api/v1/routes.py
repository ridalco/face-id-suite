from fastapi import APIRouter
from app.api.v1.endpoints import auth        # ← importa tu sub-router

router = APIRouter()
router.include_router(auth.router, tags=["auth"])
