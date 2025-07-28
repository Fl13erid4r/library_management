# library_management

import csv

def load_books():
    with open('books.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        books = list(reader)
    return books

def save_books(books):
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'availability', 'borrowed_by' ,'author',"published_year",'genre'])
        writer.writeheader()
        # Convert non-string fields to strings before writing
        for book in books:
            book_copy = book.copy()
            book_copy['availability'] = str(book_copy['availability'])
            book_copy['published_year'] = str(book_copy['published_year'])
            writer.writerow(book_copy)

data = [
    {'title': 'harry potter', 'availability': True, 'borrowed_by': '', 'author': 'J.K.Rowling', 'published_year': 1997, 'genre': 'Fantasy'},
    {'title': '1984', 'availability': False, 'borrowed_by': 'Rutwik', 'author': 'George Orwell', 'published_year': 1949, 'genre': 'Dystopian'},
    {'title': 'to kill a mockingbird', 'availability': True, 'borrowed_by': '', 'author': 'Harper Lee', 'published_year': 1960, 'genre': 'Thriller'},
]
#save_books(data)

def view_available_books(books):
    available = [book['title'] for book in books if str(book['availability']).lower() == 'true']
    if not available:
        print("There are no available books. Please come again another time!")
    else:
        print("Available books:")
        for book in available:
            print(book)

def borrow_books(books):
    available = [book for book in books if book['availability'] == 'True' or book['availability'] == True]
    if not available:
        print("There are no available books. Please come again another time!")
        return
    borrower_name = input("What is your name? ")
    print("Available books:", [book['title'] for book in available])
    book_title = input("What book do you want to borrow? ")
    for book in books:
        if book['title'].lower() == book_title.lower() and (book['availability'] == 'True' or book['availability'] == True):
            book['availability'] = False
            book['borrowed_by'] = borrower_name
            print("The book has been borrowed.")
            save_books(books)
            return

def view_borrowed_books(books):
    name = input("What is your name? ")
    borrowed = [book['title'] for book in books if book['borrowed_by'].lower() == name.lower()]
    if borrowed:
        print(f"These are the books you have borrowed, {name}:")
        for book in borrowed:
            print(book)
    else:
        print("You have not borrowed any books.")

def return_books(books):
    name = input("What is your name? ")
    borrowed = [book for book in books if book['borrowed_by'].lower() == name.lower()]
    if not borrowed:
        print("You have not borrowed any books.")
        return
    print(f"These are the books you have borrowed, {name}:")
    for book in borrowed:
        print(book['title'])
    book_remove = input("What book would you like to return? ")
    for book in borrowed:
        if book['title'].lower() == book_remove.lower():
            book['availability'] = True
            book['borrowed_by'] = ""
            print("Your book has been returned.")
            save_books(books)
            return
    print("You did not borrow that book.")

def donate_books(books):
    title = input("What is the title of the book you want to donate? ")
    author = input("Who is the author of the book? ")
    published_year = input("What year was the book published? ")
    genre = input("What is the genre of the book? ")
    new_book = {
        'title': title,
        'availability': True,
        'borrowed_by': '',
        'author': author,
        'published_year': published_year,
        'genre': genre
    }
    books.append(new_book)
    save_books(books)
    print(f"Thank you for donating {title}!")

def view_book_info(books):
    title = input("Enter the title of the book you want to view: ")
    for book in books:
        if book['title'].lower() == title.lower():
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Published Year: {book['published_year']}")
            print(f"Genre: {book['genre']}")
            print(f"Availability: {'Available' if book['availability'] == 'True' or book['availability'] == True else 'Not Available'}")
            return
    print("Book not found.")

def main():
    books = load_books()
    x = 0
    while x != 7:
        print("--------Library Menu--------")
        print("1 : View Available Books")
        print("2 : Borrow a Book")
        print("3 : View Borrowed Books")
        print("4 : Return a Book")
        print("5 : Donate a Book")
        print("6 : View Book Information")
        print("7 : Exit Library Menu")
        try:
            x = int(input("Enter 1,2,3,4,5,6 or 7 : "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if x == 1:
            view_available_books(books)
        elif x == 2:
            borrow_books(books)
        elif x == 3:
            view_borrowed_books(books)
        elif x == 4:
            return_books(books)
        elif x == 5:
            donate_books(books)
        elif x == 6:
            view_book_info(books)
        elif x == 7:    
            print("Thanks for Coming! See you soon!")
            break
        else:
            print("Please Choose a valid option.")

main()