from typing import Optional, List
from sqlmodel import SQLModel, Field
from pydantic import field_validator


# =========================
# SHARED / UTIL
# =========================
class Message(SQLModel):
    detail: str


# =========================
# EMPLEADO SCHEMAS
# =========================
class EmpleadoBase(SQLModel):
    nombre: str = Field(min_length=3, max_length=120)
    especialidad: str = Field(min_length=3, max_length=120)
    salario: float = Field(gt=0, description="Salario mensual > 0")
    estado: bool = Field(default=True)

    @field_validator("nombre", "especialidad")
    @classmethod
    def strip_text(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("no puede estar vacío")
        return v


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=3, max_length=120)
    especialidad: Optional[str] = Field(default=None, min_length=3, max_length=120)
    salario: Optional[float] = Field(default=None, gt=0)
    estado: Optional[bool] = None

    @field_validator("nombre", "especialidad")
    @classmethod
    def strip_opt_text(cls, v: Optional[str]) -> Optional[str]:
        return v.strip() if isinstance(v, str) else v


class EmpleadoRead(EmpleadoBase):
    id: int


class EmpleadoMini(SQLModel):
    id: int
    nombre: str
    especialidad: str
    estado: bool


# =========================
# PROYECTO SCHEMAS
# =========================
class ProyectoBase(SQLModel):
    nombre: str = Field(min_length=3, max_length=150)
    descripcion: str = Field(min_length=3, max_length=500)
    presupuesto: float = Field(gt=0, description="Presupuesto > 0")
    estado: bool = Field(default=True)

    @field_validator("nombre", "descripcion")
    @classmethod
    def strip_text(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("no puede estar vacío")
        return v


class ProyectoCreate(ProyectoBase):
    gerente_id: Optional[int] = Field(default=None, ge=1)


class ProyectoUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=3, max_length=150)
    descripcion: Optional[str] = Field(default=None, min_length=3, max_length=500)
    presupuesto: Optional[float] = Field(default=None, gt=0)
    estado: Optional[bool] = None
    gerente_id: Optional[int] = Field(default=None, ge=1)

    @field_validator("nombre", "descripcion")
    @classmethod
    def strip_opt_text(cls, v: Optional[str]) -> Optional[str]:
        return v.strip() if isinstance(v, str) else v


class ProyectoRead(ProyectoBase):
    id: int
    gerente_id: Optional[int] = None


class ProyectoMini(SQLModel):
    id: int
    nombre: str
    estado: bool


# =========================
# ASIGNACIÓN SCHEMAS (N:M)
# =========================
class AsignacionBase(SQLModel):
    empleado_id: int = Field(ge=1)
    proyecto_id: int = Field(ge=1)


class AsignacionCreate(AsignacionBase):
    pass


class AsignacionRead(AsignacionBase):
    id: int


# =========================
# RESPUESTAS ANIDADAS
# =========================
class EmpleadoWithProyectos(EmpleadoRead):
    proyectos: List[ProyectoMini] = []


class ProyectoWithGerenteYEmpleados(ProyectoRead):
    gerente: Optional[EmpleadoMini] = None
    empleados: List[EmpleadoMini] = []


class AsignacionExpanded(SQLModel):
    id: int
    empleado: EmpleadoMini
    proyecto: ProyectoMini


# =========================
# FILTROS (para GET con query params)
# =========================
class EmpleadoFilter(SQLModel):
    especialidad: Optional[str] = None
    estado: Optional[bool] = None
    salario_min: Optional[float] = Field(default=None, ge=0)
    salario_max: Optional[float] = Field(default=None, ge=0)


class ProyectoFilter(SQLModel):
    estado: Optional[bool] = None
    presupuesto_min: Optional[float] = Field(default=None, ge=0)
    presupuesto_max: Optional[float] = Field(default=None, ge=0)
    gerente_id: Optional[int] = Field(default=None, ge=1)


