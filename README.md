# Sistema de Gestión de Proyectos

¡Hola! Mi nombre es Laura Isabella Omaña Berrio mi codigo es 67001249 y este es mi parcial para la asignatura de desarrollo de software. Este proyecto es una API donde se gestionan empleados, proyectos y sus asignaciones en un sistema de gestión de proyectos.

## Descripción del Proyecto

Este proyecto implementa un sistema completo para la administración de recursos humanos y proyectos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre empleados, proyectos y las asignaciones entre ellos. Utiliza SQLModel para el mapeo objeto-relacional con una base de datos SQLite, proporcionando una interfaz sencilla y eficiente para la gestión de datos.

### Características Principales

- **Gestión de Empleados**: Crear, listar, actualizar y eliminar empleados con información como nombre, especialidad, salario y estado.
- **Gestión de Proyectos**: Administrar proyectos con detalles como nombre, descripción, presupuesto y gerente asignado.
- **Asignaciones**: Relacionar empleados con proyectos de manera N:M, permitiendo múltiples asignaciones.
- **API RESTful**: Endpoints organizados por modelo con documentación automática vía Swagger UI.
- **Base de Datos**: SQLite con SQLAlchemy para persistencia de datos.

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para construir APIs con Python.
- **SQLModel**: Librería para modelos de datos con SQLAlchemy y Pydantic.
- **SQLite**: Base de datos ligera y embebida.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.

## Instalación y Uso

1. Clona o descarga el proyecto.
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```
   fastapi dev main.py
   ```
4. Accede a la documentación de la API en `http://127.0.0.1:8000/docs`.

## Sobre Mí

Soy Laura Isabella Omaña Berrio, estudiante apasionada por el desarrollo de software y las tecnologías web. Me encanta aprender nuevas herramientas y aplicarlas en proyectos prácticos como este. Este parcial refleja mi interés en crear soluciones eficientes y escalables para problemas reales en la gestión de proyectos.
