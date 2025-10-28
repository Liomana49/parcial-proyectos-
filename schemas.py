from typing import List
from sqlmodel import SQLModel
from models import EstadoEmpleado, EstadoProyecto


class EmpleadoCreate(SQLModel):
    nombre: str
    especialidad: str
    salario: float
    estado: EstadoEmpleado | None = None

class EmpleadoUpdate(SQLModel):
    nombre: str | None = None
    especialidad: str | None = None
    salario: float | None = None
    estado: EstadoEmpleado | None = None

class EmpleadoRead(SQLModel):
    id: int
    nombre: str
    especialidad: str
    salario: float
    estado: EstadoEmpleado

class EmpleadoWithProyectos(EmpleadoRead):
    proyectos_ids: List[int] = []
    proyectos_gerenciados_ids: List[int] = []


class ProyectoCreate(SQLModel):
    nombre: str
    descripcion: str
    presupuesto: float
    estado: EstadoProyecto | None = None
    gerente_id: int | None = None

class ProyectoUpdate(SQLModel):
    nombre: str | None = None
    descripcion: str | None = None
    presupuesto: float | None = None
    estado: EstadoProyecto | None = None
    gerente_id: int | None = None

class ProyectoRead(SQLModel):
    id: int
    nombre: str
    descripcion: str
    presupuesto: float
    estado: EstadoProyecto
    gerente_id: int | None

class ProyectoWithEmpleados(ProyectoRead):
    empleados_ids: List[int] = []

class AsignacionCreate(SQLModel):
    empleado_id: int
    proyecto_id: int

class AsignacionRead(SQLModel):
    id: int
    empleado_id: int
    proyecto_id: int

