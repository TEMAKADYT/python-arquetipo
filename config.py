TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],  # Incluye los modelos de Aerich
            "default_connection": "default",
        },
    },
}
