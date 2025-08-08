-- CREATE TABLE books (
--     id SERIAL PRIMARY KEY,
--     Title VARCHAR(255) NOT NULL,
--     Availablity BOOlEAN DEFAULT TRUE ,
--     Borrowed_By VARCHAR(255) ,
--     Author VARCHAR(255),
--     Published INTEGER,
--     Genre VARCHAR(255)

-- )


INSERT INTO books (Title, Availablity, Borrowed_by, Author, Published, Genre)
VALUES
    ('Harry Potter', TRUE, 'N/A', 'J.K.Rowling', 1997, 'Fantasy'),
    ('1984', TRUE, '', 'George Orwell', 1949, 'Dystopian'),
    ('To Kill a Mockingbird', TRUE, '', 'Harper Lee', 1960, 'Thriller');