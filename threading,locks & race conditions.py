import csv
import threading
import time

def load_books():
    with open('books.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        books = list(reader)
    return books

def save_books(books):
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'availability', 'borrowed_by'])
        writer.writeheader()
        for book in books:
            book_copy = book.copy()
            writer.writerow(book_copy)
lock = threading.Lock()

sample_books = [
    {'title': 'Harry Potter', 'availability': True, 'borrowed_by': ''},
    {'title': '1984', 'availability': True, 'borrowed_by': ''},
    {'title': 'The Hobbit', 'availability': True, 'borrowed_by': ''}
]

save_books(sample_books)


def borrow_books(books, borrower_name, book_title):
    with lock:
        available = [book for book in books if str(book['availability']).lower() == 'true']
        if not available:
            print("There are no available books. Please come again another time!")
            return
        for book in books:
            if book['title'].lower() == book_title.lower() and str(book['availability']).lower() == 'true':
                book['availability'] = False
                book['borrowed_by'] = borrower_name
                print("The book has been borrowed.")
                save_books(books)
                return
        print("Book not available or already borrowed.")

def return_books(books, borrower_name, book_title):
    with lock:
        borrowed_books = [book for book in books if book['borrowed_by'].lower() == borrower_name.lower()]
        if not borrowed_books:
            print("You have no borrowed books.")
            return
        for book in books:
            if book['title'].lower() == book_title.lower() and book['borrowed_by'].lower() == borrower_name.lower():
                book['availability'] = True
                book['borrowed_by'] = ''
                print("The book has been returned.")
                save_books(books)
                return
        print("You have not borrowed that book.")



t1 = threading.Thread(target=borrow_books, args=(load_books(),"Amy", "harry potter"))
t2 = threading.Thread(target=borrow_books, args=(load_books(),"Bob", "1984"))

t1.start()
t2.start()
t1.join()
t2.join()


