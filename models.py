from typing import Optional, List
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

# Estados
class EstadoEmpleado(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

class EstadoProyecto(str, Enum):
    planeado = "planeado"
    en_progreso = "en_progreso"
    pausado = "pausado"
    finalizado = "finalizado"

# Link N:M
class AsignacionEmpleadoProyecto(SQLModel, table=True):
    __tablename__ = "asignaciones"
    empleado_id: int = Field(foreign_key="empleados.id", primary_key=True)
    proyecto_id: int = Field(foreign_key="proyectos.id", primary_key=True)

# Empleado
class EmpleadoBase(SQLModel):
    nombre: str = Field(min_length=2, max_length=120)
    especialidad: str = Field(min_length=2, max_length=120)
    salario: float = Field(gt=0)
    estado: EstadoEmpleado = Field(default=EstadoEmpleado.activo)

class Empleado(EmpleadoBase, table=True):
    __tablename__ = "empleados"
    id: Optional[int] = Field(default=None, primary_key=True)

    proyectos: List["Proyecto"] = Relationship(
        back_populates="empleados",
        link_model=AsignacionEmpleadoProyecto,
    )
    proyectos_gerenciados: List["Proyecto"] = Relationship(
        back_populates="gerente"
    )

# Proyecto
class ProyectoBase(SQLModel):
    nombre: str = Field(index=True, min_length=2, max_length=120)
    descripcion: str = Field(min_length=2, max_length=500)
    presupuesto: float = Field(gt=0)
    estado: EstadoProyecto = Field(default=EstadoProyecto.planeado)

class Proyecto(ProyectoBase, table=True):
    __tablename__ = "proyectos"
    id: Optional[int] = Field(default=None, primary_key=True)

    gerente_id: int | None = Field(default=None, foreign_key="empleados.id")
    gerente: Optional[Empleado] = Relationship(back_populates="proyectos_gerenciados")

    empleados: List[Empleado] = Relationship(
        back_populates="empleados",
        link_model=AsignacionEmpleadoProyecto,
    )

