from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from src.utils.enums import DifficultyLevel, WorkoutType


class WorkoutBase(BaseModel):
    name: str
    description: str = ""
    duration: int = Field(gt=0, description="Duration in minutes")
    difficulty_level: DifficultyLevel
    workout_type: WorkoutType
    is_template: bool = False


class WorkoutCreate(WorkoutBase):
    pass


class WorkoutUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[int] = Field(None, gt=0, description="Duration in minutes")
    difficulty_level: Optional[DifficultyLevel] = None
    workout_type: Optional[WorkoutType] = None
    is_template: Optional[bool] = None


class WorkoutResponse(WorkoutBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class WorkoutListResponse(BaseModel):
    workouts: list[WorkoutResponse]
    total: int
    page: int
    page_size: int
