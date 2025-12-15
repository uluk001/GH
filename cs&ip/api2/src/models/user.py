from datetime import datetime, timezone as datetime_timezone
from typing import Optional, List
from beanie import Document
from fastapi_users_db_beanie import BeanieBaseUser
from pydantic import Field

from src.utils.enums import TarriffType, Gender, FitnessLevel, FitnessGoal


class User(BeanieBaseUser, Document):
    name: str = ""
    surname: str = ""
    username: str = Field(unique=True, index=True)
    tariff: TarriffType = TarriffType.BASIC

    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    gender: Optional[Gender] = None

    fitness_level: FitnessLevel = FitnessLevel.BEGINNER
    goals: List[FitnessGoal] = Field(default_factory=list)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(datetime_timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(datetime_timezone.utc)
    )
