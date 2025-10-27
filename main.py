
from fastapi import FastAPI
from .database import init_db

app = FastAPI(
    title="Sistema de Gestión de Proyectos (base)",
    version="0.1.0",
    description="Base local sin routers: modelos, schemas, database y CRUD."
)

@app.get("/")
def root():
    return {"ok": True, "msg": "Servidor FastAPI funcionando 🚀"}

@app.on_event("startup")
async def on_startup():
    await init_db()
