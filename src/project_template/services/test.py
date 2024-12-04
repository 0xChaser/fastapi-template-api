from uuid import UUID

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from project_template.daos import test
from project_template.exceptions.test import TestNotFound
from project_template.schemas.test import TestIn, TestOut, TestPatch
from project_template.schemas.page import Page


class TestService:

    @staticmethod
    async def add_test(test_data:TestIn, session:AsyncSession):
        new_test = await test.TestDao(session).create(test_data.model_dump())
        logger.info(f"New test created successfully: {new_test}")
        return new_test
    
    @staticmethod
    async def get_all_test(offset:int, limit:int, session:AsyncSession) -> Page[TestOut]:
        all_test = await test.TestDao(session).get_all(offset=offset, limit=limit)
        return Page(
            total = await test.TestDao(session).count(),
            items=[TestOut.model_validate(_test) for _test in all_test],
            offset=offset,
            limit=limit,
        )
    
    @staticmethod
    async def get_by_id(test_id:UUID, session:AsyncSession) -> TestOut | None :
        _test = await test.TestDao(session).get_by_id(test_id)
        if not _test:
            raise TestNotFound
        return _test
    
    @staticmethod
    async def update_by_id(test_id: UUID, test_patch:TestPatch, session:AsyncSession) -> TestPatch:
        _test = await test.TestDao(session).get_by_id(test_id)
        if not _test:
            raise TestNotFound
        for key,value in test_patch.model_dump(exclude_unset=True).items():
            setattr(_test, key, value)
        await session.commit()
        return _test
    
    @staticmethod
    async def delete_by_id(test_id:UUID, session:AsyncSession) -> None:
        _test = await test.TestDao(session).delete_by_id(test_id)
        if not _test:
            raise TestNotFound
        return _test
    
    @staticmethod
    async def delete_all(session:AsyncSession) -> None:
        await test.TestDao(session).delete_all()
        return []