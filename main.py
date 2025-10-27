from fastapi import FastAPI, Depends
from sqlmodel import Session
from typing import List

from database import create_db_and_tables, get_session
from crud import (
    crear_empleado, listar_empleados, obtener_empleado, actualizar_empleado, eliminar_empleado,
    crear_proyecto, listar_proyectos, obtener_proyecto, actualizar_proyecto, eliminar_proyecto,
    asignar_empleado_a_proyecto, listar_asignaciones, eliminar_asignacion
)
from schemas import (
    EmpleadoCreate, EmpleadoRead, EmpleadoUpdate,
    ProyectoCreate, ProyectoRead, ProyectoUpdate,
    AsignacionCreate, AsignacionRead
)


# =========================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =========================================================
app = FastAPI(
    title="Sistema de Gestión de Proyectos",
    description="API para gestionar empleados, proyectos y sus asignaciones",
    version="1.0.0"
)


# =========================================================
# EVENTO DE INICIO
# =========================================================
@app.on_event("startup")
def on_startup():
    """Crea las tablas al iniciar el servidor."""
    create_db_and_tables()


# =========================================================
# ENDPOINTS EMPLEADOS
# =========================================================
@app.post("/empleados/", response_model=EmpleadoRead)
def crear_nuevo_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_session)):
    return crear_empleado(db, empleado)


@app.get("/empleados/", response_model=List[EmpleadoRead])
def listar_todos_empleados(db: Session = Depends(get_session)):
    return listar_empleados(db)


@app.get("/empleados/{empleado_id}", response_model=EmpleadoRead)
def obtener_empleado_por_id(empleado_id: int, db: Session = Depends(get_session)):
    return obtener_empleado(db, empleado_id)


@app.put("/empleados/{empleado_id}", response_model=EmpleadoRead)
def actualizar_empleado_por_id(empleado_id: int, empleado: EmpleadoUpdate, db: Session = Depends(get_session)):
    return actualizar_empleado(db, empleado_id, empleado)


@app.delete("/empleados/{empleado_id}")
def eliminar_empleado_por_id(empleado_id: int, db: Session = Depends(get_session)):
    return eliminar_empleado(db, empleado_id)


# =========================================================
# ENDPOINTS PROYECTOS
# =========================================================
@app.post("/proyectos/", response_model=ProyectoRead)
def crear_nuevo_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_session)):
    return crear_proyecto(db, proyecto)


@app.get("/proyectos/", response_model=List[ProyectoRead])
def listar_todos_proyectos(db: Session = Depends(get_session)):
    return listar_proyectos(db)


@app.get("/proyectos/{proyecto_id}", response_model=ProyectoRead)
def obtener_proyecto_por_id(proyecto_id: int, db: Session = Depends(get_session)):
    return obtener_proyecto(db, proyecto_id)


@app.put("/proyectos/{proyecto_id}", response_model=ProyectoRead)
def actualizar_proyecto_por_id(proyecto_id: int, proyecto: ProyectoUpdate, db: Session = Depends(get_session)):
    return actualizar_proyecto(db, proyecto_id, proyecto)


@app.delete("/proyectos/{proyecto_id}")
def eliminar_proyecto_por_id(proyecto_id: int, db: Session = Depends(get_session)):
    return eliminar_proyecto(db, proyecto_id)


# =========================================================
# ENDPOINTS ASIGNACIONES (N:M)
# =========================================================
@app.post("/asignaciones/", response_model=AsignacionRead)
def asignar_empleado(proyecto: AsignacionCreate, db: Session = Depends(get_session)):
    return asignar_empleado_a_proyecto(db, proyecto)


@app.get("/asignaciones/", response_model=List[AsignacionRead])
def listar_todas_asignaciones(db: Session = Depends(get_session)):
    return listar_asignaciones(db)


@app.delete("/asignaciones/{asignacion_id}")
def eliminar_asignacion_por_id(asignacion_id: int, db: Session = Depends(get_session)):
    return eliminar_asignacion(db, asignacion_id)


# =========================================================
# ENDPOINT RAÍZ
# =========================================================
@app.get("/")
def inicio():
    return {"mensaje": "🚀 API Sistema de Gestión de Proyectos funcionando correctamente"}

