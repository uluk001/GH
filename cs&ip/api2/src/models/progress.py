from datetime import date as date_type
from beanie import Document, Indexed
from pydantic import Field


class Progress(Document):
    user_id: Indexed(str)
    exercise_id: Indexed(str)

    date: date_type = Field(default_factory=date_type.today)

    weight: float
    reps: int
    sets: int

    personal_record: bool = False

    class Settings:
        name = "progress"
