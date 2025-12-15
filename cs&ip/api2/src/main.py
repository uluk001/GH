import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

from src.models.user import User
from src.models.exercises import Exercise
from src.models.workouts import Workout
from src.models.workout_exercises import WorkoutExercise
from src.models.workout_sessions import WorkoutSession
from src.models.progress import Progress
from src.api.v1.endpoints import users, workouts

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "workouts_db")


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(MONGODB_URL)
    database = client[DATABASE_NAME]

    await init_beanie(
        database=database,
        document_models=[
            User,
            Exercise,
            Workout,
            WorkoutExercise,
            WorkoutSession,
            Progress,
        ],
    )
    print(f"Connected to MongoDB: {DATABASE_NAME}")

    yield

    client.close()
    print("Disconnected from MongoDB")


app = FastAPI(
    title="Workouts API",
    description="API for managing workouts and exercises",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(users.router, prefix="/api/v1")
app.include_router(workouts.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to Workouts API"}
