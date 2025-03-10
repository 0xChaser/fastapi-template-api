from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from project_template.settings import settings

postgresql_url = settings.database_uri.unicode_string()

engine = create_async_engine(postgresql_url, echo=True, future=True)
AsyncSessionFactory = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session


        