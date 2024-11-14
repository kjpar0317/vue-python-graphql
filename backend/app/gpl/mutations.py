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
    async def add_code(self, c_id: str, c_parent_id: Optional[str], c_name: Optional[str], c_eng_name: Optional[str], c_description: Optional[str]) -> schemas.CodeM:
        async with get_session() as s:
            code = None

            sql = select(models.CodeM).where(
                and_(models.CodeM.C_ID == c_id, models.CodeM.C_PARENT_ID == c_parent_id))
            code = (await s.execute(sql)).scalars().first()

            if code is None:
                raise HTTPException("중복 유저입니다.")

            insert_code = models.CodeM(C_ID=c_id, C_PARENT_ID=c_parent_id,
                                       C_NAME=c_name, C_ENG_NAME=c_eng_name, C_DESCRIPTION=c_description)
            s.add(insert_code)
            await s.commit()
        return insert_code

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def add_code_problem(self, cp_category_cd: str, cp_title: str, cp_level_cd: str, cp_content: Optional[str], cp_tag: Optional[str]) -> schemas.CodeProblem:
        async with get_session() as s:
            code_problem = models.CodeProblem(
                CP_CATEGORY_CD=cp_category_cd, CP_TITLE=cp_title, CP_LEVEL_CD=cp_level_cd, CP_CONTENT=cp_content, CP_TAG=cp_tag)
            s.add(code_problem)
            await s.commit()
        return code_problem
