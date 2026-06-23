import os


def env(name: str, default=None):
    return os.environ.get(name, default)


class Config:
    SECRET_KEY = env("SECRET_KEY", "dev-secret-key-change-me")

    # Example:
    # postgresql+psycopg2://user:pass@localhost:5432/smart_task_db
    SQLALCHEMY_DATABASE_URI = env(
        "DATABASE_URL",
        # Default to a local Postgres instance. If you don't have Postgres
        # configured locally, set DATABASE_URL to point at your DB.
        "postgresql+psycopg2://postgres:postgres@localhost:5432/smart_task_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SOCKETIO_CORS_ALLOWED_ORIGINS = env("SOCKETIO_CORS_ALLOWED_ORIGINS", "*")

