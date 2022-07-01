import strawberry
import datetime
from typing import Optional, Dict

from strawberry.schema.types.base_scalars import DateTime

from . import models


@strawberry.type
class AuthData:
    user_id: strawberry.ID
    token: Optional[str] = None
    token_expiration: Optional[float] = 0

    @classmethod
    def marshal(cls, model: Dict) -> "AuthData":
        return cls(user_id=strawberry.ID(model["user_id"]), token=model["token"], token_expiration=model["token_expiration"])


@strawberry.experimental.pydantic.type(models.CodeM, fields=['C_ID', 'C_PARENT_ID', 'C_NAME', 'C_ENG_NAME', 'C_DESCRIPTION'])
class CodeM:
    pass


@strawberry.experimental.pydantic.type(models.CodeProblem, fields=['CP_SEQ', 'CP_CATEGORY_CD', 'CP_TITLE', 'CP_LEVEL_CD', 'CP_CONTENT', 'CP_TAG', 'CP_LAPTIME'])
class CodeProblem:
    pass
