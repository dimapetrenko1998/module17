import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Подготовка путей для импорта модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

# Интерпретация файла конфигурации Alembic.
fileConfig(context.config.config_file_name)

# Импорт моделей
from app.backend.db import Base
from app.models import User, Task


target_metadata = Base.metadata


def run_migrations_offline():
    """Выполнить миграции в 'offline' режиме."""
    url = context.config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Выполнить миграции в 'online' режиме."""
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
