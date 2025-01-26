-- 1. Create the Books table
CREATE TABLE Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
);

-- 2. Insert initial data
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');

-- 3. Update 1984's year to 1950
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984';

-- 4. Query Dystopian books
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian';

-- 5. Delete books published before 1950
DELETE FROM Books WHERE Year_Published < 1950;

-- 6. Add and update Rating column
ALTER TABLE Books ADD COLUMN Rating REAL;

UPDATE Books
SET Rating = 4.8
WHERE Title = 'To Kill a Mockingbird';

UPDATE Books
SET Rating = 4.7
WHERE Title = '1984';

-- 7. Retrieve all books sorted by Year_Published ascending
SELECT * FROM Books ORDER BY Year_Published ASC;
