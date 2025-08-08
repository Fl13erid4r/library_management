from sqlalchemy import create_engine, Column, Integer, Boolean, String, JSON
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:password@localhost:5432/library"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    availablity = Column(Boolean, default=True)
    published = Column(Integer)
    genre = Column(String)
    borrowed_by = Column(JSON, default=list)
    copies = Column(Integer, index=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "published": self.published,
            "genre": self.genre,
            "borrowed_by": self.borrowed_by,
            "availablity": self.availablity,
            "copies": self.copies
        }

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    gmail = Column(String, index=True)
    password = Column(String, index=True)
    books_currently_borrowed = Column(Integer, default=0)
    total_loans = Column(Integer, default=0)
    books_being_borrowed = Column(JSON, default=list)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "gmail": self.gmail,
            "password": self.password,
            "number_of_books_currently_borrowed": self.books_currently_borrowed,
            "number_of_total_loans": self.total_loans,
            "books_being_borrowed": self.books_being_borrowed
        }

Base.metadata.create_all(bind=engine)

def enter():
    choice = input("Enter 1 to log in or 2 to sign up: ")
    if choice == "1":
        return log_in()
    elif choice == "2":
        return sign_up()
    else:
        print("Invalid input")
        return None

def log_in():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    db = SessionLocal()
    user = db.query(User).filter(User.name == name).first()
    if user:
        if user.password == password:
            print(f"\nWelcome {name} to the Library")
            return name
        else:
            print("Incorrect password")
            return None
    else:
        print("User not found")
        return None

def sign_up():
    name = input("Enter your name: ")
    gmail = input("Enter your gmail: ")
    password = input("Enter your password: ")
    db = SessionLocal()
    user = db.query(User).filter(User.name == name).first()
    if user:
        print("User already exists")
        return None
    else:
        user = User(Name=name, Gmail=gmail, Password=password)
        db.add(user)
        db.commit()
        print("User created successfully")
        return name

def available_books():
    db = SessionLocal()
    books = db.query(Book).filter(Book.availablity == True).all()
    if books:
        for book in books:
            print(book.to_dict())
    else:
        print("No available books")

def borrow_book(username):
    book_title = input("Enter the book title: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book_title).first()
    if book:
        if book.availablity:
            book.copies -= 1
            if book.copies == 0:
                book.availablity = False
            borrowed_by = book.borrowed_by or []
            borrowed_by.append(username)
            book.borrowed_by = borrowed_by
            db.commit()

            user = db.query(User).filter(User.Name == username).first()
            if user:
                user.books_being_borrowed += 1
                books_being_borrowed = user.books_being_borrowed or []
                books_being_borrowed.append(book.title)
                user.books_being_borrowed = books_being_borrowed
                user.total_loans += 1
                db.commit()
                print("Book borrowed successfully")
            else:
                print("User not found")
        else:
            print("Book not available")
    else:
        print("Book not found")

def return_book(username):
    book_title = input("Enter the book title: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book_title).first()
    if book:
        borrowed_by = book.borrowed_by or []
        if username in borrowed_by:
            borrowed_by.remove(username)
            book.borrowed_by = borrowed_by
            book.copies += 1
            if book.copies > 0:
                book.availablity = True
            db.commit()

            user = db.query(User).filter(User.Name == username).first()
            if user:
                user.books_currently_borrowed -= 1
                books_being_borrowed = user.books_being_borrowed or []
                if book.title in books_being_borrowed:
                    books_being_borrowed.remove(book.title)
                user.books_being_borrowed = books_being_borrowed
                db.commit()
                print("Book returned successfully")
            else:
                print("User not found")
        else:
            print("You did not borrow this book")
    else:
        print("Book not found")

def view_loans(username):
    db = SessionLocal()
    user = db.query(User).filter(User.name == username).first()
    if user:
        books = user.books_being_borrowed or []
        if books:
            print("Your borrowed books:")
            for book in books:
                print(f"- {book}")
        else:
            print("You have no borrowed books")
    else:
        print("User not found")

def donate_book():
    book_title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    published = int(input("Enter the published year: "))
    genre = input("Enter the genre: ")
    copies = int(input("Enter the number of copies: "))
    db = SessionLocal()
    book = Book(title=book_title, author=author, published=published, genre=genre, copies=copies)
    db.add(book)
    db.commit()
    print("Book donated successfully")

def book_info():
    book_title = input("Enter the book title: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book_title).first()
    if book:
        print(book.to_dict())
    else:
        print("Book not found")

def user_info(username):
    db = SessionLocal()
    user = db.query(User).filter(User.name == username).first()
    if user:
        print(user.to_dict())
    else:
        print("User not found")

def change_details(username):
    db = SessionLocal()
    user = db.query(User).filter(User.name == username).first()
    if user:
        password = input("Enter your original password: ")
        if user.Password == password:
            new_name = input("Enter your new name: ")
            new_gmail = input("Enter your new gmail: ")
            new_password = input("Enter your new password: ")
            user.name = new_name
            user.gmail = new_gmail
            user.password = new_password
            db.commit()
            print("User details changed successfully")
        else:
            print("Incorrect password")
    else:
        print("User not found")

def add_new_book():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    published = int(input("Enter the published year: "))
    genre = input("Enter the genre: ")
    copies = int(input("Enter the number of copies: "))
    db = SessionLocal()
    book = Book(title=title, author=author, published=published, genre=genre, copies=copies)
    db.add(book)
    db.commit()
    print("Book added successfully")

def update_book():
    book_title = input("Enter the book title to update: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book_title).first()
    if book:
        new_title = input("Enter the new book title: ")
        new_author = input("Enter the new author name: ")
        new_published = int(input("Enter the new published year: "))
        new_genre = input("Enter the new genre: ")
        new_copies = int(input("Enter the new number of copies: "))
        book.title = new_title
        book.author = new_author
        book.published = new_published
        book.genre = new_genre
        book.copies = new_copies
        book.availablity = new_copies > 0
        db.commit()
        print("Book updated successfully")
    else:
        print("Book not found")

def delete_book():
    book_title = input("Enter the book title to delete: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book_title).first()
    if book:
        db.delete(book)
        db.commit()
        print("Book deleted successfully")
    else:
        print("Book not found")