from fastapi import FastAPI
from pydantic import BaseModel

books = [
  {
    "id": 1,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "published_date": "1988-04-15"
  },
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published_date": "1960-07-11"
  },
  {
    "id": 3,
    "title": "1984",
    "author": "George Orwell",
    "published_date": "1949-06-08"
  },
  {
    "id": 4,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "published_date": "1813-01-28"
  },
  {
    "id": 5,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10"
  },
  {
    "id": 6,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "published_date": "1937-09-21"
  },
  {
    "id": 7,
    "title": "Atomic Habits",
    "author": "James Clear",
    "published_date": "2018-10-16"
  },
  {
    "id": 8,
    "title": "Rich Dad Poor Dad",
    "author": "Robert T. Kiyosaki",
    "published_date": "1997-04-01"
  },
  {
    "id": 9,
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "published_date": "1997-06-26"
  },
  {
    "id": 10,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "published_date": "1951-07-16"
  }
]


app = FastAPI()


class Book(BaseModel):
    id: int
    title:str
    author:str
    published_date:str

@app.get("/books")
def get_books():
    return books

@

@app.post("/books")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)