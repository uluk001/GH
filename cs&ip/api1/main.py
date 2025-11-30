import fastapi
import uvicorn

from models.books import Book, Books, CreateBook


app = fastapi.FastAPI()

books = [
    {"title": "1984", "author": "George Orwell", "id": 1},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "id": 2},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "id": 3},
]


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return Book(**book)
    return fastapi.HTTPException(status_code=404, detail="Book not found")


@app.get("/books")
async def get_books():
    print("Hi")
    return Books(books=books).books


@app.patch("/books/{book_id}")
async def update_book(book_id: int, book: CreateBook):
    for idx, existing_book in enumerate(books):
        if existing_book['id'] == book_id:
            updated_book = book.model_dump()
            updated_book['id'] = book_id
            books[idx] = updated_book
            return Book(**updated_book)
    return fastapi.HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}")
async def replace_book(book_id: int, book: CreateBook):
    for idx, existing_book in enumerate(books):
        if existing_book['id'] == book_id:
            replaced_book = book.model_dump()
            replaced_book['id'] = book_id
            books[idx] = replaced_book
            return Book(**replaced_book)
    return fastapi.HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for idx, existing_book in enumerate(books):
        if existing_book['id'] == book_id:
            del books[idx]
            return {"detail": "Book deleted"}
    return fastapi.HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
async def create_books(book: CreateBook):
    new_book = book.model_dump()
    new_book['id'] = books[-1]['id'] + 1 if books else 1
    books.append(new_book)
    return Book(**new_book)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
