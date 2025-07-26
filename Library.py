# library_management
import csv

available_books = ["harry potter", "1984", "to kill a mockingbird"]
borrowed_books = {}

def load_books():
    with open('books.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)
    print("Books loaded from CSV:")

def save_books(books):
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'availability', 'borrowed_by'])
        writer.writeheader()
        writer.writerows(books)
    print("Books saved to CSV.")

def view_available_books():
    if len(available_books) == 0:
        print("There are no available books. Please come again another time!")
    else:
        print("Available books:")
        for book in available_books:
            print(book)

def borrow_books():
    if len(available_books) == 0:
        print("There are no available books. Please come again another time!")
        return
    borrower_name = input("What is your name? ")
    print("Available books:", available_books)
    book = input("What book do you want to borrow? ")
    if book in available_books:
        borrowed_books.setdefault(borrower_name, [])
        borrowed_books[borrower_name].append(book)
        available_books.remove(book)
        print("The book has been borrowed.")
    else:
        print("We do not have that book.")

def view_borrowed_books():
    name = input("What is your name? ")
    if name in borrowed_books and borrowed_books[name]:
        print(f"These are the books you have borrowed, {name}:")
        for book in borrowed_books[name]:
            print(book)
    else:
        print("You have not borrowed any books.")

def return_books():
    name = input("What is your name? ")
    if name not in borrowed_books or not borrowed_books[name]:
        print("You have not borrowed any books.")
        return
    print(f"These are the books you have borrowed, {name}:")
    for book in borrowed_books[name]:
        print(book)
    book_remove = input("What book would you like to return? ")
    if book_remove in borrowed_books[name]:
        borrowed_books[name].remove(book_remove)
        available_books.append(book_remove)
        print("Your book has been returned.")
        # Remove the user from borrowed_books if they have no books left
        if not borrowed_books[name]:
            del borrowed_books[name]
    else:
        print("You did not borrow that book.")

def main():
    x = 0
    while x != 5:
        print("--------Library Menu--------")
        print("1 : View Available Books")
        print("2 : Borrow a Book")
        print("3 : View Borrowed Books")
        print("4 : Return a Book")
        print("5 : Exit Library Menu")
        try:
            x = int(input("Enter 1,2,3,4 or 5 : "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if x == 1:
            view_available_books()
        elif x == 2:
            borrow_books()
        elif x == 3:
            view_borrowed_books()
        elif x == 4:
            return_books()
        elif x == 5:
            print("Thanks for Coming! See you soon!")
        else:
            print("Please Choose a valid option.")

#main()

data = [
    {"title": "harry potter", "availability": True, "borrowed_by": ""},
    {"title": "1984", "availability": True, "borrowed_by": ""},
    {"title": "to kill a mockingbird", "availability": True, "borrowed_by": ""}
]

save_books(data)

loaded_books = load_books()
print("Loaded books:", loaded_books)

