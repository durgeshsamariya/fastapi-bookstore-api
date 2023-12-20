from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int
    
class User(BaseModel):
    username: str
    password: str
    role: str