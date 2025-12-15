from typing import Optional
from datetime import datetime
from beanie import Document, Indexed
from pydantic import Field


class WorkoutSession(Document):
    user_id: Indexed(str)
    workout_id: Indexed(str)

    start_time: datetime
    end_time: Optional[datetime] = None
    actual_duration: Optional[int] = None

    calories_burned: Optional[float] = None

    notes: str = ""
    rating: Optional[int] = Field(None, ge=1, le=5)

    completed: bool = False

    class Settings:
        name = "workout_sessions"
