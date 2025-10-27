from sqlmodel import SQLModel, Session, create_engine

# =========================================================
# CONFIGURACIÓN BASE DE DATOS LOCAL (sincrónica)
# =========================================================

# Ruta del archivo de base de datos SQLite local
DATABASE_URL = "sqlite:///./database.db"

# Crear engine (sin async)
# connect_args evita errores de thread en SQLite
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})


# =========================================================
# CREAR TABLAS
# =========================================================
def create_db_and_tables():
    """Crea las tablas definidas en los modelos."""
    from models import Empleado, Proyecto, Asignacion  # importa aquí para evitar ciclos
    SQLModel.metadata.create_all(engine)


# =========================================================
# SESIÓN DE BASE DE DATOS
# =========================================================
def get_session():
    """Dependency de FastAPI para usar la sesión."""
    with Session(engine) as session:
        yield session


