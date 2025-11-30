from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str


class Books(BaseModel):
    books: list[Book]


class CreateBook(BaseModel):
    title: str
    author: str
    id: Optional[int] = None
