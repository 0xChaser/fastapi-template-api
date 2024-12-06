from logging.config import fileConfig

from project_template.models import *
from project_template.models.base import Base
from project_template.settings import settings

from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

from alembic import context


config = context.config

target_metadata = Base.metadata

def run_migrations(connection):
    context.configure(
        connection=connection,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
        target_metadata=target_metadata,
        include_schemas=False,
        version_table_schema=target_metadata.schema, 
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine    
    and associate a connection with the context.

    """
    connectable = create_async_engine(settings.database_uri.unicode_string(), future=True)

    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations)


asyncio.run(run_migrations_online())