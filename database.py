# database.py

from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    # 👇 Importa aquí dentro (no al inicio)
    from models import Empleado, Proyecto, Asignacion
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


