from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from project_template.db import get_session
from project_template.schemas.test import (
    TestIn,
    TestOut,
    TestPatch
)
from project_template.schemas.page import Page
from project_template.services.test import TestService

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/", response_model=Page[TestOut])
async def list_test(
    offset:int=0,
    limit:int=10,
    session:AsyncSession = Depends(get_session)
):
    """
    Get all test:
    
    Return : 
    
    TestOut : Test with all it's attributes (id, name, age, comment) 
    
    """
    return await TestService.get_all_test(session=session, offset=offset, limit=limit)

@router.get("/{id}", response_model=TestOut)
async def get_test(id:UUID, session:AsyncSession=Depends(get_session)):
    return await TestService.get_by_id(id, session)


@router.post("/")
async def add_test(test_data:TestIn, session:AsyncSession=Depends(get_session)):
    return await TestService.add_test(test_data, session)

@router.patch("/{id}", response_model=TestOut)
async def update_test(id:UUID, test:TestPatch, session:AsyncSession=Depends(get_session)):
    return await TestService.update_by_id(id, test, session)

@router.delete("/{id}", response_model=TestOut)
async def delete_test(id:UUID,session:AsyncSession=Depends(get_session)):
    return await TestService.delete_by_id(id, session)

@router.delete("/")
async def delete_all_test(session:AsyncSession=Depends(get_session)):
    return await TestService.delete_all(session)