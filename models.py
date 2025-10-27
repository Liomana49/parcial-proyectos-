from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel


# =========================================================
# MODELO EMPLEADO
# =========================================================
class EmpleadoBase(SQLModel):
    nombre: str
    especialidad: str
    salario: float
    estado: bool = True


class Empleado(EmpleadoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relaciones
    proyectos_asignados: List["Asignacion"] = Relationship(back_populates="empleado")
    proyectos_gerenciados: List["Proyecto"] = Relationship(back_populates="gerente")


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoRead(EmpleadoBase):
    id: int


class EmpleadoUpdate(SQLModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None
    salario: Optional[float] = None
    estado: Optional[bool] = None


# =========================================================
# MODELO PROYECTO
# =========================================================
class ProyectoBase(SQLModel):
    nombre: str
    descripcion: str
    presupuesto: float
    estado: bool = True


class Proyecto(ProyectoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    gerente_id: Optional[int] = Field(default=None, foreign_key="empleado.id")

    # Relaciones
    gerente: Optional["Empleado"] = Relationship(back_populates="proyectos_gerenciados")
    empleados_asignados: List["Asignacion"] = Relationship(back_populates="proyecto")


class ProyectoCreate(ProyectoBase):
    gerente_id: Optional[int] = None


class ProyectoRead(ProyectoBase):
    id: int
    gerente_id: Optional[int]


class ProyectoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    presupuesto: Optional[float] = None
    estado: Optional[bool] = None
    gerente_id: Optional[int] = None


# =========================================================
# MODELO ASIGNACION (relación N:M)
# =========================================================
class AsignacionBase(SQLModel):
    empleado_id: int = Field(foreign_key="empleado.id")
    proyecto_id: int = Field(foreign_key="proyecto.id")


class Asignacion(AsignacionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relaciones
    empleado: Optional["Empleado"] = Relationship(back_populates="proyectos_asignados")
    proyecto: Optional["Proyecto"] = Relationship(back_populates="empleados_asignados")


class AsignacionCreate(AsignacionBase):
    pass


class AsignacionRead(AsignacionBase):
    id: int

