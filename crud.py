from typing import List, Optional
from fastapi import HTTPException, status
from sqlmodel import Session, select
from models import Empleado, Proyecto, Asignacion
from schemas import (
    EmpleadoCreate, EmpleadoUpdate,
    ProyectoCreate, ProyectoUpdate,
    AsignacionCreate
)


# =========================================================
# CRUD EMPLEADOS
# =========================================================
def crear_empleado(db: Session, empleado: EmpleadoCreate) -> Empleado:
    nuevo = Empleado.from_orm(empleado)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_empleados(db: Session) -> List[Empleado]:
    empleados = db.exec(select(Empleado)).all()
    return empleados


def obtener_empleado(db: Session, empleado_id: int) -> Empleado:
    empleado = db.get(Empleado, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado


def actualizar_empleado(db: Session, empleado_id: int, datos: EmpleadoUpdate) -> Empleado:
    empleado = db.get(Empleado, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    datos_actualizados = datos.dict(exclude_unset=True)
    for key, value in datos_actualizados.items():
        setattr(empleado, key, value)

    db.add(empleado)
    db.commit()
    db.refresh(empleado)
    return empleado


def eliminar_empleado(db: Session, empleado_id: int):
    empleado = db.get(Empleado, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    # Previene borrar gerente asignado a proyectos
    proyectos_gerenciados = db.exec(select(Proyecto).where(Proyecto.gerente_id == empleado_id)).all()
    if proyectos_gerenciados:
        raise HTTPException(status_code=400, detail="No se puede eliminar un empleado que es gerente de proyectos")

    db.delete(empleado)
    db.commit()
    return {"detail": "Empleado eliminado correctamente"}


# =========================================================
# CRUD PROYECTOS
# =========================================================
def crear_proyecto(db: Session, proyecto: ProyectoCreate) -> Proyecto:
    nuevo = Proyecto.from_orm(proyecto)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_proyectos(db: Session) -> List[Proyecto]:
    proyectos = db.exec(select(Proyecto)).all()
    return proyectos


def obtener_proyecto(db: Session, proyecto_id: int) -> Proyecto:
    proyecto = db.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


def actualizar_proyecto(db: Session, proyecto_id: int, datos: ProyectoUpdate) -> Proyecto:
    proyecto = db.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    datos_actualizados = datos.dict(exclude_unset=True)
    for key, value in datos_actualizados.items():
        setattr(proyecto, key, value)

    db.add(proyecto)
    db.commit()
    db.refresh(proyecto)
    return proyecto


def eliminar_proyecto(db: Session, proyecto_id: int):
    proyecto = db.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    # Elimina también las asignaciones asociadas
    asignaciones = db.exec(select(Asignacion).where(Asignacion.proyecto_id == proyecto_id)).all()
    for asignacion in asignaciones:
        db.delete(asignacion)

    db.delete(proyecto)
    db.commit()
    return {"detail": "Proyecto y sus asignaciones eliminados correctamente"}


# =========================================================
# CRUD ASIGNACIONES (relación N:M)
# =========================================================
def asignar_empleado_a_proyecto(db: Session, datos: AsignacionCreate) -> Asignacion:
    empleado = db.get(Empleado, datos.empleado_id)
    proyecto = db.get(Proyecto, datos.proyecto_id)

    if not empleado or not proyecto:
        raise HTTPException(status_code=404, detail="Empleado o proyecto no encontrado")

    # Verificar si ya está asignado
    existe = db.exec(
        select(Asignacion)
        .where(Asignacion.empleado_id == datos.empleado_id)
        .where(Asignacion.proyecto_id == datos.proyecto_id)
    ).first()

    if existe:
        raise HTTPException(status_code=400, detail="El empleado ya está asignado a este proyecto")

    nueva = Asignacion.from_orm(datos)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def listar_asignaciones(db: Session) -> List[Asignacion]:
    return db.exec(select(Asignacion)).all()


def eliminar_asignacion(db: Session, asignacion_id: int):
    asignacion = db.get(Asignacion, asignacion_id)
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    db.delete(asignacion)
    db.commit()
    return {"detail": "Asignación eliminada correctamente"}
