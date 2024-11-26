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
