from sqlalchemy import create_engine, Column, Integer, Boolean, String, JSON
from sqlalchemy.orm import declarative_base, sessionmaker, Session
    # # "postgresql://your_user:your_password@localhost:5432/your_db"
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
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Gmail = Column(String, index=True)
    Password = Column(String, index=True)
    Books_currently_borrowed = Column(Integer, default=0)
    Total_loans = Column(Integer, default=0)
    Books_being_borrowed = Column(JSON, default=list)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "gmail": self.gmail,
            "books_currently_borrowed": self.books_currently_borrowed,
            "total_loans": self.total_loans,
            "books_being_borrowed": self.books_being_borrowed
        }

Base.metadata.create_all(bind=engine)

def enter():
    input=input("Enter 1 to log in or 2 to sign up: ")
    if input==1:
        log_in()
    elif input==2:
        sign_up()
    else:
        print("Invalid input")

def log_in():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    db = SessionLocal()
    user = db.query(User).filter(User.Name == name).first()
    if user:
        if user.Password == password:
            return{"":"Welcome to the "}
        else:
            return {"message": "incorrect password"}
    else:
        return {"message": "user not found"}

def sign_up():
    name = input("Enter your name: ")
    gmail = input("Enter your gmail: ")
    password = input("Enter your password: ")
    db = SessionLocal()
    user = db.query(User).filter(User.Name == name).first()
    if user:
        return {"message": "user already exists"}
    else:
        user = User(Name=name, Gmail=gmail, Password=password)
        db.add(user)
        db.commit()
        return {"message": "user created successfully"}

def available_books():
    db = SessionLocal()
    books = db.query(Book).filter(Book.availablity == True).all()
    return [book.to_dict() for book in books]

def borrow_book():
    book = input("Enter the book title: ")
    user = input("Enter your name: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book).first()
    if book:
        if book.availablity:
            book.copies -= 1
            if book.copies == 0:
                book.availablity = False
            book.borrowed_by.append(user)
            db.commit()
            user = db.query(User).filter(User.name == user).first()
            if user:
                user.books_currently_borrowed += 1
                user.books_being_borrowed.append(book.title)
                user.total_loans += 1
                db.commit()
            else:
                user = User(name=user, gmail="")
                db.add(user)
                db.commit()
            return {"message": "book borrowed successfully"}
        return {"message": "book not available"}
    return {"message": "book not found"}

def view_loans():
    pass
    user = input("Enter your name: ")
    db = SessionLocal()
    user = db.query(User).filter(User.name == user).first()
    if user:
        return user.books_being_borrowed
    else:
        return {"message": "user not found"}

def return_book():
    book = input("Enter the book title: ")
    user = input("Enter your name: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book).first()
    if book:
        if user in book.borrowed_by:
            book.borrowed_by.remove(user)
            book.copies += 1
            if book.copies > 0:
                book.availablity = True
            db.commit()
            user = db.query(User).filter(User.name == user).first()
            if user:
                user.books_currently_borrowed -= 1
                user.books_being_borrowed.remove(book.title)
                db.commit()
                return {"message": "book returned successfully"}
            else:
                return {"message": "user not found"}
        else:
            return {"message": "user did not borrow this book"}
    else:
        return {"message": "book not found"}

def book_info():
    book = input("Enter the book title: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book).first()
    if book:
        return book.to_dict()
    else:
        return {"message": "book not found"}

def user_info():
    user = input("Enter your name: ")
    db = SessionLocal()
    user = db.query(User).filter(User.name == user).first()
    if user:
        return user.__dict__
    else:
        return {"message": "user not found"}

def donate_book():
    book = input("Enter the book title: ")
    author = input("Enter the author name: ")
    published = input("Enter the published year: ")
    genre = input("Enter the genre: ")
    copies = input("Enter the number of copies: ")
    db = SessionLocal()
    book = Book(title=book, author=author, published=published, genre=genre, copies=copies)
    db.add(book)
    db.commit()
    return {"message": "book donated successfully"}

def change_details():
    user = input("Enter your name: ")
    password = input("Enter your original password: ")
    db = SessionLocal()
    user = db.query(User).filter(User.name == user).first()
    if user:
        if user.password == password:
            name = input("Enter your name: ")
            gmail = input("Enter your gmail: ")
            password = input("Enter your password: ")
            user.name = name
            user.gmail = gmail
            user.password = password
            db.commit()
            return {"message": "user details changed successfully"}
        else:
            return {"message": "incorrect password"}
    else:
        return {"message": "user not found"}

def update_book():
    book = input("Enter the book title: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book).first()
    if book:
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        published = input("Enter the published year: ")
        genre = input("Enter the genre: ")
        copies = input("Enter the number of copies: ")
        book.title = title
        book.author = author
        book.published = published
        book.genre = genre
        book.copies = copies
        db.commit()
        return {"message": "book updated successfully"}
    else:
        return {"message": "book not found"}

def add_new_book():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    published = input("Enter the published year: ")
    genre = input("Enter the genre: ")
    copies = input("Enter the number of copies: ")
    db = SessionLocal()
    book = Book(title=title, author=author, published=published, genre=genre, copies=copies)
    db.add(book)
    db.commit()
    return {"message": "book added successfully"}

def delete_book():
    book = input("Enter the book title: ")
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == book).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message": "book deleted successfully"}
    else:
        return {"message": "book not found"}


