from datetime import datetime, timezone as datetime_timezone
from beanie import Document, Indexed
from pydantic import Field

from src.utils.enums import DifficultyLevel, WorkoutType


class Workout(Document):
    user_id: Indexed(str)

    name: str
    description: str = ""

    duration: int
    difficulty_level: DifficultyLevel
    workout_type: WorkoutType

    is_template: bool = False

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(datetime_timezone.utc)
    )

    class Settings:
        name = "workouts"
