from fastapi import FastAPI
from Library import save_books,load_books,view_available_books,borrow_books,view_borrowed_books,return_books,donate_books,view_book_info
import uvicorn
import csv



app = FastAPI()

@app.get("/view-available")
def view_borrowed_books(name: str):
    books = load_books()
    return [book['title'] for book in books if book['borrowed_by'].lower() == name.lower()]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=8000)   
