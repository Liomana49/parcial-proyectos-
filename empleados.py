from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from ..models import Empleado

async def crear(db: AsyncSession, empleado: Empleado) -> Empleado:
    db.add(empleado)
    await db.commit()
    await db.refresh(empleado)
    return empleado

async def listar(db: AsyncSession) -> List[Empleado]:
    res = await db.execute(select(Empleado).order_by(Empleado.id))
    return res.scalars().all()

async def obtener(db: AsyncSession, empleado_id: int) -> Empleado | None:
    return await db.get(Empleado, empleado_id)

async def actualizar(db: AsyncSession, empleado: Empleado, data: dict) -> Empleado:
    for k, v in data.items():
        if v is not None:
            setattr(empleado, k, v)
    await db.commit()
    await db.refresh(empleado)
    return empleado

async def eliminar(db: AsyncSession, empleado: Empleado) -> None:
    await db.delete(empleado)
    await db.commit()
