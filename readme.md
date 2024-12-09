# Install Deps
  pip install -r requirements.txt

# Start server
  sanic --debug web.server:app
  open http://localhost:8000/read-api for graphql introspection

# Freeze requirements
  pip install pipreqs
  pipreqs .

# Initializing Migrations (only once when the project is created)
  aerich init --location database/tortoiseimpl/migrations -t config.TORTOISE_ORM
  python database/tortoiseimpl/init.py
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


# Guia de desarrollador
    Utiliza gitcommit para realizar commits basado en el estandar de commit de conventionalcommits
    mas informacion en: https://www.conventionalcommits.org/en/v1.0.0/#summary

# Calcular version actual
    semantic-release version

## PROXIMAS ACTIVIDADES

[ X ] Crear modelos
[ X ] Ejecutar migraciones
[ X ] Crear repositorios

[ X ] Diseñar casos de uso
[ X ] Implementar casos de uso

[ 40% ] Diseñar queries
[ 40% ] Implementar queries
[ 20% ] Diseñar mutaciones
[ 20% ] Implementar mutaciones
[] Paginacion
[] Filtrado de informacion
[] Autenticacion
[] Esquema de permisos

[ X ] Refactorizacion Strawberry graphQL
[ X ] Docs, add conventional commit usage

[ ] Diseñar pruebas
[ ] Implementar pruebas

[ ] Implementar loggin del SQL


## CLEAN CACHE
    find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
