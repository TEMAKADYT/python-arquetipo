TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": [
                "infraestructure.models.bank_account_model",
                "infraestructure.models.transaction_model",
                "aerich.models"
            ],  # Incluye los modelos de Aerich
            "default_connection": "default",
        },
    },
    "use_tz": True,  # Use timezone-aware datetime fields
    "timezone": "UTC",  # Set timezone, e.g., "UTC" or your preferred timezone
}
