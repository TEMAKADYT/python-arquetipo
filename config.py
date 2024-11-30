TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "timezone": {
        "use_tz": True,
    },
    "apps": {
        "models": {
            "models": ["infraestructure.models", "aerich.models"],  # Incluye los modelos de Aerich
            "default_connection": "default",
        },
    },
}