from fastapi import APIRouter

from project_template.api.v1.test import router as TestRouter


__all__ = (
    TestRouter,
)


router = APIRouter()


for api_router in __all__:
    router.include_router(api_router)