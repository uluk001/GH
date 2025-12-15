from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

from src.utils.enums import TarriffType, Gender, FitnessLevel, FitnessGoal


class UserBase(BaseModel):
    name: str = ""
    surname: str = ""
    username: str
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    gender: Optional[Gender] = None
    fitness_level: FitnessLevel = FitnessLevel.BEGINNER
    goals: List[FitnessGoal] = Field(default_factory=list)


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    username: Optional[str] = None
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    gender: Optional[Gender] = None
    fitness_level: Optional[FitnessLevel] = None
    goals: Optional[List[FitnessGoal]] = None


class UserResponse(UserBase):
    id: str
    email: EmailStr
    tariff: TarriffType
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
