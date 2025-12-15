from typing import Optional
from beanie import Document, Indexed


class WorkoutExercise(Document):
    workout_id: Indexed(str)
    exercise_id: Indexed(str)

    sets: Optional[int] = None
    reps: Optional[int] = None
    duration_seconds: Optional[int] = None

    rest_time_seconds: int = 60

    order: int

    weight: Optional[float] = None
    distance: Optional[float] = None

    class Settings:
        name = "workout_exercises"
