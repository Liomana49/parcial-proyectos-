from fastapi import FastAPI

from database import create_db_and_tables
from empleados_router import router as empleados_router
from proyectos_router import router as proyectos_router
from asignaciones_router import router as asignaciones_router



app = FastAPI(
    title="Sistema de Gestión de Proyectos",
    description="API para gestionar empleados, proyectos y sus asignaciones",
    version="1.0.0"
)


app.include_router(empleados_router)
app.include_router(proyectos_router)
app.include_router(asignaciones_router)



@app.on_event("startup")
def on_startup():
    """Crea las tablas al iniciar el servidor."""
    create_db_and_tables()



@app.get("/")
def inicio():
    return {"mensaje": "🚀 API Sistema de Gestión de Proyectos funcionando correctamente"}

