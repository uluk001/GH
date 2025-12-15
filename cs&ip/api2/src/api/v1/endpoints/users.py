from typing import List
from fastapi import APIRouter, HTTPException, status, Query
from beanie import PydanticObjectId

from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    existing_user = await User.find_one(User.email == user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )

    existing_username = await User.find_one(User.username == user_data.username)
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists",
        )

    user = User(
        email=user_data.email,
        hashed_password=user_data.password,
        name=user_data.name,
        surname=user_data.surname,
        username=user_data.username,
        age=user_data.age,
        weight=user_data.weight,
        height=user_data.height,
        gender=user_data.gender,
        fitness_level=user_data.fitness_level,
        goals=user_data.goals,
    )

    await user.insert()

    return UserResponse(
        id=str(user.id),
        email=user.email,
        name=user.name,
        surname=user.surname,
        username=user.username,
        age=user.age,
        weight=user.weight,
        height=user.height,
        gender=user.gender,
        fitness_level=user.fitness_level,
        goals=user.goals,
        tariff=user.tariff,
        is_active=user.is_active,
        is_verified=user.is_verified,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    users = await User.find_all().skip(skip).limit(limit).to_list()

    return [
        UserResponse(
            id=str(user.id),
            email=user.email,
            name=user.name,
            surname=user.surname,
            username=user.username,
            age=user.age,
            weight=user.weight,
            height=user.height,
            gender=user.gender,
            fitness_level=user.fitness_level,
            goals=user.goals,
            tariff=user.tariff,
            is_active=user.is_active,
            is_verified=user.is_verified,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
        for user in users
    ]


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    try:
        user = await User.get(PydanticObjectId(user_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return UserResponse(
        id=str(user.id),
        email=user.email,
        name=user.name,
        surname=user.surname,
        username=user.username,
        age=user.age,
        weight=user.weight,
        height=user.height,
        gender=user.gender,
        fitness_level=user.fitness_level,
        goals=user.goals,
        tariff=user.tariff,
        is_active=user.is_active,
        is_verified=user.is_verified,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_data: UserUpdate):
    try:
        user = await User.get(PydanticObjectId(user_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    update_data = user_data.model_dump(exclude_unset=True)

    if "username" in update_data and update_data["username"] != user.username:
        existing = await User.find_one(User.username == update_data["username"])
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken"
            )

    for field, value in update_data.items():
        setattr(user, field, value)

    from datetime import datetime, timezone

    user.updated_at = datetime.now(timezone.utc)

    await user.save()

    return UserResponse(
        id=str(user.id),
        email=user.email,
        name=user.name,
        surname=user.surname,
        username=user.username,
        age=user.age,
        weight=user.weight,
        height=user.height,
        gender=user.gender,
        fitness_level=user.fitness_level,
        goals=user.goals,
        tariff=user.tariff,
        is_active=user.is_active,
        is_verified=user.is_verified,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    try:
        user = await User.get(PydanticObjectId(user_id))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID format"
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    await user.delete()
    return None
