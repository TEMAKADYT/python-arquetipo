# Install Deps
  pip install -r requirements.txt

# Start server
  sanic main

# Freeze requirements
  pip install pipreqs
  pipreqs .

# Initializing Migrations (only once when the project is created)
  aerich init -t config.TORTOISE_ORM
  aerich init-db

# Create Migrations
  aerich migrate

# Run Migrations
  aerich upgrade

# Run TESTS
  pytest


Estructura del proyecto

    project/
    │
    ├── src/
    │   ├── core/              # Dominio (Entidades y Casos de uso)
    │   │   ├── entities/      # Modelos de negocio (clases puras)
    │   │   ├── use_cases/     # Casos de uso (lógica de negocio)
    │   │   └── interfaces/    # Puertos (interfaces para repositorios)
    │   │
    │   ├── infrastructure/    # Implementaciones concretas
    │   │   ├── db/            # Repositorios para la base de datos
    │   │   ├── graphql/       # Esquemas GraphQL (Strawberry)
    │   │   └── third_party/   # Conexiones externas (servicios externos)
    │   │
    │   ├── application/       # Configuración y adaptadores
    │   │   ├── schema/        # Esquema raíz de GraphQL
    │   │   └── config.py      # Configuración general (DI, settings)
    │   │
    │   └── main.py            # Punto de entrada (Sanic)
    │
    └── tests/                 # Pruebas unitarias y de integración
