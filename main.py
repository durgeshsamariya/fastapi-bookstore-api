from fastapi import FastAPI, HTTPException, Depends, status
from models import Book  # Import the Book model
from auth import create_access_token, get_current_user, verify_user, create_access_token_for_user, get_user
from roles import UserRole
from models import User

# Create an instance of FastAPI
app = FastAPI()

# In-memory data store for books (replace with a database in production)
books_db = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Store API"}

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    """
    Create a new book entry.

    Parameters:
    - book (Book) : The book data to be added.

    Returns:
    - book: A response message indicating success or failure.
    """
    # FastAPI automatically validates the incoming 'book' data
    # If the data is invalid, FastAPI will return a detailed error response
    # If the data is valid, you can proceed to save it
    books_db[book.isbn] = book
    return book

@app.get("/books/{isbn}", response_model=Book)
def read_book(isbn: str):
    """
    Retrieve book details by ISBN.

    Parameters:
    - isbn (str): The ISBN of the book to retrieve.

    Returns:
    - book: The book details or a message if the book is not found.
    """
    # Fetch book data from your data store
    book_data = books_db.get(isbn)
    if book_data is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_data

@app.put("/books/{isbn}", response_model=Book)
def update_book(isbn: str, updated_book: Book):
    """
    Update book information by ISBN.

    Parameters:
    - isbn (str): The ISBN of the book to update.
    - updated_book (Book): The updated book data.

    Returns:
    - dict: A response message indicating success or failure.
    """
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[isbn] = updated_book
    return updated_book

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    """
    Delete a book by ISBN.

    Parameters:
    - isbn (str): The ISBN of the book to delete.

    Returns:
    - Book: A detail of deleted book.
    """
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = books_db.pop(isbn)
    return deleted_book

# Example protected route with role-based access control
@app.get("/admin/dashboard")
async def admin_dashboard(current_user: User = Depends(get_current_user)):
    if current_user["role"] == UserRole.admin:
        return {"message": "Welcome to the admin dashboard!"}
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="You do not have permission to access this resource.")