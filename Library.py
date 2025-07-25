# library_management
books= []
x = 0
available_books = ["harry potter", "1984","to kill a mockingbird" ]
borrowed_books = {}

def view_available_books():
    for book in available_books:
        print(book)
    if len(available_books) == 0:
        print("There are no available books.Please come again another time!")

def borrow_books():
    if len(available_books) == 0:
        print("There are no available books.Please come again another time!") 
    x = input("What is your name? ")
    print(available_books)
    y = input("What book do you want to borrow? ")
    z = 0
    if y in available_books:
        if len(borrowed_books.keys()) > 0:
            if x in borrowed_books.keys():
                books = []
                books.append(borrowed_books[x])
                books.append(y)
                borrowed_books.update({x : books})               
            else:
                books = []
                books.append(y)
                print(books)
                borrowed_books[x] = books
        else:
            books = []
            books.append(y)
            print(books)
            borrowed_books[x] = books
        z = 1
        print("The book has been borrowed")
        available_books.remove(y)
    if z == 0:
        print("We do not have that book")   

def view_borrowed_books():
    name = input("What is your name? ")
    print(f"These are the books you have borrowed {name} :")
    for book in borrowed_books[name]:
        print(book)

def return_books():
    name = input("What is your name? ")
    print(f"Hello {name } !")
    if name in borrowed_books.keys():
        print(f"These are the books you have borrowed {name} :")
        for book in borrowed_books[name]:
            books = []
            books.append(book)
            print(book)
    else:
        print("You have not borrowed any books")
        return
    book_remove = input("What book would you like to return")
    if book_remove in books:
        print("Your book has been removed")
        book.remove(book_remove)
        borrowed_books.update({name : books})
        available_books.append(book_remove)

while x !=5:
    print("--------Library Menu--------")
    print("1 : View Available Books")
    print("2 : Borrow a Book")
    print("3 : View Borrowed Books")
    print("4 : Return a Book")
    print("5 : Exit Library Menu")
    x = int(input("Enter 1,2,3,4 or 5 : "))
    if x == 1:
        view_available_books()
    elif x == 2:
        borrow_books()
    elif x == 3:
        view_borrowed_books()
    elif x == 4:
        return_books()
    else:
        print("Please Choose a valid option")

print("Thanks for Coming ! See you soon !")