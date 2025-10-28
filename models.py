# models.py
from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

# Tipos para estado
EstadoEmpleado = bool
EstadoProyecto = bool

# ================= EMPLEADO =================
class EmpleadoBase(SQLModel):
    nombre: str
    especialidad: str
    salario: float
    estado: bool = True
    deleted_at: Optional[datetime] = None

class Empleado(EmpleadoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    proyectos_asignados: List["Asignacion"] = Relationship(back_populates="empleado")
    proyectos_gerenciados: List["Proyecto"] = Relationship(back_populates="gerente")

# ================= PROYECTO =================
class ProyectoBase(SQLModel):
    nombre: str
    descripcion: str
    presupuesto: float
    estado: bool = True
    deleted_at: Optional[datetime] = None

class Proyecto(ProyectoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    gerente_id: Optional[int] = Field(default=None, foreign_key="empleado.id")
    gerente: Optional["Empleado"] = Relationship(back_populates="proyectos_gerenciados")
    empleados_asignados: List["Asignacion"] = Relationship(back_populates="proyecto")

# ================= ASIGNACION (N:M) =================
class AsignacionBase(SQLModel):
    empleado_id: int = Field(foreign_key="empleado.id")
    proyecto_id: int = Field(foreign_key="proyecto.id")
    deleted_at: Optional[datetime] = None

class Asignacion(AsignacionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    empleado: Optional["Empleado"] = Relationship(back_populates="proyectos_asignados")
    proyecto: Optional["Proyecto"] = Relationship(back_populates="empleados_asignados")
