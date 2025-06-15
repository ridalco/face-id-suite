from fastapi import FastAPI
from app.api.v1 import routes as v1_routes   # ← importa el router principal

app = FastAPI(title="Face-ID Suite", version="0.1.0")

app.include_router(v1_routes.router, prefix="/api/v1")   # ← monta aquí

@app.get("/api/v1/ping", tags=["utils"])
async def ping():
    return {"status": "pong 🏓"}

# ─── Creación de tablas al arranque ───────────────────────────
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

