from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from database import get_session
from crud import (
    crear_proyecto, listar_proyectos, obtener_proyecto, actualizar_proyecto, eliminar_proyecto,
    listar_proyectos_eliminados
)
from schemas import ProyectoCreate, ProyectoRead, ProyectoUpdate

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])

@router.post("/", response_model=ProyectoRead)
def crear_nuevo_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_session)):
    return crear_proyecto(db, proyecto)

@router.get("/", response_model=List[ProyectoRead])
def listar_todos_proyectos(db: Session = Depends(get_session)):
    return listar_proyectos(db)

@router.get("/{proyecto_id}", response_model=ProyectoRead)
def obtener_proyecto_por_id(proyecto_id: int, db: Session = Depends(get_session)):
    return obtener_proyecto(db, proyecto_id)

@router.put("/{proyecto_id}", response_model=ProyectoRead)
def actualizar_proyecto_por_id(proyecto_id: int, proyecto: ProyectoUpdate, db: Session = Depends(get_session)):
    return actualizar_proyecto(db, proyecto_id, proyecto)

@router.delete("/{proyecto_id}")
def eliminar_proyecto_por_id(proyecto_id: int, db: Session = Depends(get_session)):
    return eliminar_proyecto(db, proyecto_id)

@router.get("/eliminados", response_model=List[ProyectoRead])
def listar_proyectos_eliminados_endpoint(db: Session = Depends(get_session)):
    return listar_proyectos_eliminados(db)
