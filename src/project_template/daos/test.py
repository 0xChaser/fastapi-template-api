from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project_template.daos.base import BaseDao
from project_template.exceptions.test import TestLinkedToAnotherObject
from project_template.models.test import Test

class TestDao(BaseDao):

    def __init__(self, session:AsyncSession):
        super().__init__(session)

    async def create(self, test_data: dict) -> Test:
        _test = Test(**test_data)
        self.session.add(_test)
        await self.session.commit()
        await self.session.refresh(_test)
        return _test
    
    async def get_by_id(self, test_id: UUID) -> Test | None:
        statement = select(Test).where(Test.id == test_id)
        return await self.session.scalar(statement=statement)

    async def get_all(self, offset:int, limit:int) -> list[Test]:
        statement = select(Test).offset(offset).limit(limit)
        result = await self.session.execute(statement=statement)
        return result.scalars().all()
    
    async def delete_all(self) -> None:
        await self.session.execute(delete(Test))
        await self.session.commit()

    async def delete_by_id(self, test_id:UUID) -> None:
        _test = await self.get_by_id(test_id=test_id)
        try:
            statement = delete(Test).where(Test.id == test_id)
            await self.session.execute(statement=statement)
            await self.session.commit()
        except IntegrityError:
            raise TestLinkedToAnotherObject
        return _test
    
    async def count(self) -> int:
        statement = select(func.count()).select_from(Test)
        result = await self.session.execute(statement=statement)
        return result.scalar_one()