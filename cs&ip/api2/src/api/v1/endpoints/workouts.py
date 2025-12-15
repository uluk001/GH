from fastapi import APIRouter, HTTPException, status, Query
from beanie import PydanticObjectId

from src.models.workouts import Workout
from src.schemas.workout import (
    WorkoutCreate,
    WorkoutUpdate,
    WorkoutResponse,
    WorkoutListResponse,
)

router = APIRouter(prefix="/workouts", tags=["workouts"])


@router.post("/", response_model=WorkoutResponse, status_code=status.HTTP_201_CREATED)
async def create_workout(
    workout_data: WorkoutCreate, user_id: str = Query(..., description="User ID")
):
    workout = Workout(
        user_id=user_id,
        name=workout_data.name,
        description=workout_data.description,
        duration=workout_data.duration,
        difficulty_level=workout_data.difficulty_level,
        workout_type=workout_data.workout_type,
        is_template=workout_data.is_template,
    )

    await workout.insert()

    return WorkoutResponse(
        id=str(workout.id),
        user_id=workout.user_id,
        name=workout.name,
        description=workout.description,
        duration=workout.duration,
        difficulty_level=workout.difficulty_level,
        workout_type=workout.workout_type,
        is_template=workout.is_template,
        created_at=workout.created_at,
    )


@router.get("/", response_model=WorkoutListResponse)
async def get_workouts(
    user_id: str = Query(None, description="Filter by user ID"),
    is_template: bool = Query(None, description="Filter by template status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
):
    query = {}

    if user_id:
        query["user_id"] = user_id

    if is_template is not None:
        query["is_template"] = is_template

    workouts = await Workout.find(query).skip(skip).limit(limit).to_list()
    total = await Workout.find(query).count()

    workout_responses = [
        WorkoutResponse(
            id=str(workout.id),
            user_id=workout.user_id,
            name=workout.name,
            description=workout.description,
            duration=workout.duration,
            difficulty_level=workout.difficulty_level,
            workout_type=workout.workout_type,
            is_template=workout.is_template,
            created_at=workout.created_at,
        )
        for workout in workouts
    ]

    return WorkoutListResponse(
        workouts=workout_responses, total=total, page=skip // limit + 1, page_size=limit
    )


@router.get("/{workout_id}", response_model=WorkoutResponse)
async def get_workout(workout_id: str):
    try:
        workout = await Workout.get(PydanticObjectId(workout_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid workout ID format"
        )

    if not workout:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found"
        )

    return WorkoutResponse(
        id=str(workout.id),
        user_id=workout.user_id,
        name=workout.name,
        description=workout.description,
        duration=workout.duration,
        difficulty_level=workout.difficulty_level,
        workout_type=workout.workout_type,
        is_template=workout.is_template,
        created_at=workout.created_at,
    )


@router.patch("/{workout_id}", response_model=WorkoutResponse)
async def update_workout(workout_id: str, workout_data: WorkoutUpdate):
    try:
        workout = await Workout.get(PydanticObjectId(workout_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid workout ID format"
        )

    if not workout:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found"
        )

    update_data = workout_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(workout, field, value)

    await workout.save()

    return WorkoutResponse(
        id=str(workout.id),
        user_id=workout.user_id,
        name=workout.name,
        description=workout.description,
        duration=workout.duration,
        difficulty_level=workout.difficulty_level,
        workout_type=workout.workout_type,
        is_template=workout.is_template,
        created_at=workout.created_at,
    )


@router.delete("/{workout_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workout(workout_id: str):
    try:
        workout = await Workout.get(PydanticObjectId(workout_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid workout ID format"
        )

    if not workout:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found"
        )

    await workout.delete()
    return None
