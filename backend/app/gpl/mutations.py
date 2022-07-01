import strawberry
from typing import Optional

from fastapi.exceptions import HTTPException
from sqlalchemy import select, and_

from app.config import get_session
from app.utils import IsAuthenticated, signJWT
from app import models, schemas


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def login(self, id: str, password: str) -> schemas.AuthData:
        async with get_session() as s:
            info = None

            sql = select(models.Users).where(
                and_(models.Users.id == id, models.Users.password == password))

            user = (await s.execute(sql)).scalars().first()

            if user is not None:
                print(user.id)
                info = schemas.AuthData.marshal(signJWT(user.id))
            else:
                raise HTTPException("없는 유저입니다.")
                # return NotExistUser()
        return info

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def add_code(self, C_ID: str, C_PARENT_ID: Optional[str], C_NAME: Optional[str], C_ENG_NAME: Optional[str], C_DESCRIPTION: Optional[str]) -> schemas.CodeM:
        async with get_session() as s:
            code = None

            sql = select(models.CodeM).where(
                and_(models.CodeM.C_ID == C_ID, models.CodeM.C_PARENT_ID == C_PARENT_ID))
            code = (await s.execute(sql)).scalars().first()

            if code is None:
                raise HTTPException("중복 유저입니다.")

            insert_code = models.CodeM(C_ID=C_ID, C_PARENT_ID=C_PARENT_ID,
                                       C_NAME=C_NAME, C_ENG_NAME=C_ENG_NAME, C_DESCRIPTION=C_DESCRIPTION)
            s.add(insert_code)
            await s.commit()
        return insert_code

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def add_code_problem(self, CP_CATEGORY_CD: str, CP_TITLE: str, CP_LEVEL_CD: str, CP_CONTENT: Optional[str], CP_TAG: Optional[str]) -> schemas.CodeProblem:
        async with get_session() as s:
            code_problem = models.CodeProblem(
                CP_CATEGORY_CD=CP_CATEGORY_CD, CP_TITLE=CP_TITLE, CP_LEVEL_CD=CP_LEVEL_CD, CP_CONTENT=CP_CONTENT, CP_TAG=CP_TAG)
            s.add(code_problem)
            await s.commit()
        return code_problem
