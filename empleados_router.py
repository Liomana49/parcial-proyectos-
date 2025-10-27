from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from database import get_session
from crud import (
    crear_empleado, listar_empleados, obtener_empleado, actualizar_empleado, eliminar_empleado
)
from schemas import EmpleadoCreate, EmpleadoRead, EmpleadoUpdate

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.post("/", response_model=EmpleadoRead)
def crear_nuevo_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_session)):
    return crear_empleado(db, empleado)

@router.get("/", response_model=List[EmpleadoRead])
def listar_todos_empleados(db: Session = Depends(get_session)):
    return listar_empleados(db)

@router.get("/{empleado_id}", response_model=EmpleadoRead)
def obtener_empleado_por_id(empleado_id: int, db: Session = Depends(get_session)):
    return obtener_empleado(db, empleado_id)

@router.put("/{empleado_id}", response_model=EmpleadoRead)
def actualizar_empleado_por_id(empleado_id: int, empleado: EmpleadoUpdate, db: Session = Depends(get_session)):
    return actualizar_empleado(db, empleado_id, empleado)

@router.delete("/{empleado_id}")
def eliminar_empleado_por_id(empleado_id: int, db: Session = Depends(get_session)):
    return eliminar_empleado(db, empleado_id)
