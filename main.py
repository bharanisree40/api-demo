from fastapi import FastAPI, HTTPException
from schema import Book

app = FastAPI()

# A variable to store ONE book only (starts as None)
stored_book: Book = None

# Show the current book (GET)
@app.get("/book")
def get_book():
    if stored_book is None:
        raise HTTPException(status_code=404, detail="No book found")
    return stored_book

# Add a new book (POST)
@app.post("/text_book")
def create_book(book: Book):
    global stored_book
    if stored_book is not None:
        raise HTTPException(status_code=400, detail="A book already exists")
    stored_book = book
    return {"message": "Book created successfully"}

# Update the book (PUT)
@app.put("/text_book")
def update_book(book: Book):
    global stored_book
    if stored_book is None:
        raise HTTPException(status_code=404, detail="No book to update")
    stored_book = book
    return {"message": "Book updated successfully"}

# Delete the book (DELETE)
@app.delete("/text_book")
def delete_book():
    global stored_book
    if stored_book is None:
        raise HTTPException(status_code=404, detail="No book to delete")
    stored_book = None
    return {"message": "Book deleted successfully"}
