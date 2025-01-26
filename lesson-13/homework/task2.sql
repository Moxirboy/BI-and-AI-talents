CREATE TABLE Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
);

INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');

UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984';

SELECT Title, Author FROM Books WHERE Genre = 'Dystopian';

DELETE FROM Books WHERE Year_Published < 1950;

ALTER TABLE Books ADD COLUMN Rating REAL;

UPDATE Books
SET Rating = 4.8
WHERE Title = 'To Kill a Mockingbird';

UPDATE Books
SET Rating = 4.7
WHERE Title = '1984';

SELECT * FROM Books ORDER BY Year_Published ASC;
