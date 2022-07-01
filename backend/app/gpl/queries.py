import strawberry
from typing import Optional

from sqlalchemy import select

from app.config import get_session
from app.utils import IsAuthenticated
from app import models, schemas


@strawberry.type
class Query:
    @strawberry.field(permission_classes=[IsAuthenticated])
    async def codes(self, page: Optional[int] = 1, page_size: Optional[int] = 100) -> list[schemas.CodeM]:
        async with get_session() as s:
            sql = select(models.CodeM).order_by(
                models.CodeM.C_ID).offset((page - 1) * page_size).limit(page_size)
            return (await s.execute(sql)).scalars().all()

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def code_problems(self, page: Optional[int] = 1, page_size: Optional[int] = 100) -> list[schemas.CodeProblem]:
        async with get_session() as s:
            sql = select(models.CodeProblem).order_by(
                models.CodeProblem.CP_SEQ).offset((page - 1) * page_size).limit(page_size)
            # code_problems = (await s.execute(sql)).scalars().unique().all()
            return (await s.execute(sql)).scalars().all()
