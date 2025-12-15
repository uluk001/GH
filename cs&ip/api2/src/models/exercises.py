from typing import Optional, List
from datetime import datetime, timezone as datetime_timezone
from beanie import Document
from pydantic import Field

from src.utils.enums import ExerciseCategory, MuscleGroup, DifficultyLevel


class Exercise(Document):
    name: str = Field(index=True)
    description: str = ""

    category: ExerciseCategory
    muscle_groups: List[MuscleGroup] = Field(default_factory=list)
    difficulty_level: DifficultyLevel

    equipment_needed: List[str] = Field(default_factory=list)
    instructions: str = ""
    video_url: Optional[str] = None

    calories_per_minute: Optional[float] = None

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(datetime_timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(datetime_timezone.utc)
    )

    class Settings:
        name = "exercises"
