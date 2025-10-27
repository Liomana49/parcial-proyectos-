from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from database import get_session
from crud import asignar_empleado_a_proyecto, listar_asignaciones, eliminar_asignacion
from schemas import AsignacionCreate, AsignacionRead

router = APIRouter(prefix="/asignaciones", tags=["Asignaciones"])

@router.post("/", response_model=AsignacionRead)
def asignar_empleado(proyecto: AsignacionCreate, db: Session = Depends(get_session)):
    return asignar_empleado_a_proyecto(db, proyecto)

@router.get("/", response_model=List[AsignacionRead])
def listar_todas_asignaciones(db: Session = Depends(get_session)):
    return listar_asignaciones(db)

@router.delete("/{asignacion_id}")
def eliminar_asignacion_por_id(asignacion_id: int, db: Session = Depends(get_session)):
    return eliminar_asignacion(db, asignacion_id)
