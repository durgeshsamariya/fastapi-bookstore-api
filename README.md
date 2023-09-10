# Bookstore API using FastAPI

The Bookstore API is a robust and high-performance API built using FastAPI. It allows users to browse, search, and purchase books. The API includes features like adding reviews, managing a shopping cart, and processing orders.

## Features

- Browse and search for books by title, author, or genre
- User authentication and authorization
- Adding, updating, and deleting reviews for books
- Managing a shopping cart with add, update, and remove functionalities
- Processing orders, calculating totals, and generating invoices

## Technologies Used

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python
- SQLAlchemy: A powerful and popular Object-Relational Mapping (ORM) library for database operations
- SQLite: A lightweight and serverless database used for storing book, user, and order data

## Project Structure

The project follows a structured organization to maintain code readability and maintainability. Here's the project structure:
```
fastapi-bookstore-api/
    ├── main.py
    ├── models.py
    ├── database.py
    ├── authentication.py
    ├── docs/
    ├── tests/
    └── requirements.txt
```

- `main.py` : This file will contain your FastAPI application code, including API routing and logic.
- `models.py` : Define Pydantic models for data structures to ensure data consistency and validation.
- `database.py` : Set up your database connection and define database models for storing book information.
- `authentication.py` : Handle user authentication and authorization.
- `docs/` : Store documentation and project-related notes.
- `tests/` : Create a test suite to ensure the reliability and correctness of your API.
- `requirements.txt` : List your project's dependencies for easy installation.


## Getting Started

1. Clone the repository: git clone <repository_url>
2. Create a virtual environment: `python3 -m venv env`
3. Activate the virtual environment:
  - For Unix/Linux: `source env/bin/activate`
  - For Windows: `.\env\Scripts\activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Run the API server: `uvicorn main:app --reload`
6. Visit http://localhost:8000/docs to access the interactive API documentation (Swagger UI).

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.


