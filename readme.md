# Install Deps
  pip install -r requirements.txt

# Start server
  sanic --debug web.server:create_app
  open http://localhost:8000/gql for graphql introspection

# Start asgi server
  # WEB
  gunicorn web.server:create_app --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker

  # WEBSOCKET
  gunicorn web.asgi_ws:wsapp --bind 0.0.0.0:8010 --worker-class uvicorn.workers.UvicornWorker

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



# pip install 'strawberry-graphql[debug-server]'
# pip install 'tortoise-orm[aiosqlite]'
