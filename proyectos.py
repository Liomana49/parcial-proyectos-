from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from ..models import Proyecto

async def crear(db: AsyncSession, proyecto: Proyecto) -> Proyecto:
    db.add(proyecto)
    await db.commit()
    await db.refresh(proyecto)
    return proyecto

async def listar(db: AsyncSession) -> List[Proyecto]:
    res = await db.execute(select(Proyecto).order_by(Proyecto.id))
    return res.scalars().all()

async def obtener(db: AsyncSession, proyecto_id: int) -> Proyecto | None:
    return await db.get(Proyecto, proyecto_id)

async def actualizar(db: AsyncSession, proyecto: Proyecto, data: dict) -> Proyecto:
    for k, v in data.items():
        if v is not None:
            setattr(proyecto, k, v)
    await db.commit()
    await db.refresh(proyecto)
    return proyecto

async def eliminar(db: AsyncSession, proyecto: Proyecto) -> None:
    await db.delete(proyecto)
    await db.commit()
