# library_management
books= []
available_books = ["harry potter", "1984","to kill a mockingbird" ]
borrowed_books = {}
def view_available_books():
    for book in available_books:
        print(book)
    if len(available_books) == 0:
        print("There are no available books.Please come again another time!")

def borrow_books():
    x = input("What is your name? ")
    print(available_books)
    y = input("What book do you want to borrow? ")
    z = 0
    books.append(y)
    for book in available_books:
        if book == y:
            borrowed_books.update({x : books})
            z = 1
            print("The book has been borrowed")
            print(borrowed_books)
            available_books.remove(book)
            print(available_books)
    if z == 0:
        print("We do not have that book")   

def view_borrowed_books():
    name = input("What is your name? ")
    print(f"These are the books you have borrowed {borrowed_books[name]}")

def return_books():
    name = input("What is your name?")
    print(f"")

print("--------Library Menu--------")
print("1 : View Available Books")
print("2 : Borrow a Book")
print("3 : View Borrowed Books")
print("4 : Return a Book")
print("5 : Exit Library Menu")

x = int(input("Enter 1,2,3,4 or 5 : "))
while x !=5:
    if x == 1:
        view_available_books()
        x = int("Enter 1,2,3,4 or 5 : ")
    elif x == 2:
        borrow_books()
        x = int(input("Enter 1,2,3,4 or 5 : "))
    elif x == 3:
        view_borrowed_books()
        x = int(input("Enter 1,2,3,4 or 5 : "))
    elif x == 4:
        return_books()
        x = int(input("Enter 1,2,3,4 or 5 : "))
    else:
        print("Please Choose a valid option")
        x = int(input("Enter 1,2,3,4 or 5 : "))
print("Thanks for Coming ! See you soon !")
