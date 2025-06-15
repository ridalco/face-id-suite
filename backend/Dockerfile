# backend/Dockerfile  (corregido)
FROM python:3.11-slim

# ─── Ajustes básicos ───────────────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Aquí vivirá tu código
WORKDIR /app      

# ─── Dependencias de sistema + Python ──────────────────────────
COPY backend/requirements.txt ./
RUN apt-get update \
 && apt-get install -y --no-install-recommends libpq-dev \
 && pip install --upgrade pip \
 && pip install -r requirements.txt \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ─── Copiamos TODA la aplicación ───────────────────────────────
# Copia backend/app/  →  /app/app/
COPY backend/app/app/ ./app/

# ─── Arranque ──────────────────────────────────────────────────
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
