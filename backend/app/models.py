from datetime import datetime
from typing import Optional
from sqlmodel import Field

from .config import Base, SQLModel


class Users(SQLModel, table=True):
    __tablename__ = "users"
    id: str = Field(default=None, primary_key=True, index=True)
    name: Optional[str]
    password: str


class CodeM(SQLModel, table=True):
    __tablename__ = "tb_code_m"
    C_ID: Optional[str] = Field(default=None, primary_key=True, index=True)
    C_PARENT_ID: Optional[str]
    C_NAME: Optional[str]
    C_ENG_NAME: Optional[str]
    C_DESCRIPTION: Optional[str]

    # team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    # team: Optional[Team] = Relationship(back_populates="heroes")


class CodeProblem(SQLModel, table=True):
    __tablename__ = "tb_code_problem"
    CP_SEQ: Optional[int] = Field(default=None, primary_key=True, index=True)
    CP_CATEGORY_CD: str
    CP_TITLE: str
    CP_LEVEL_CD: str
    CP_CONTENT: Optional[str]
    CP_TAG: str
    CP_LAPTIME: datetime = Field(
        default_factory=datetime.utcnow(), nullable=False)
