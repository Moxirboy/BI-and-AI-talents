-- 1. Create the Roster table
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

-- 2. Insert the initial data
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

-- 3. Update Jadzia Dax's name to Ezri Dax
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

-- 4. Query Bajoran characters
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';

-- 5. Delete characters over 100 years old
DELETE FROM Roster WHERE Age > 100;

-- 6. Add and update the Rank column
ALTER TABLE Roster ADD COLUMN Rank TEXT;

UPDATE Roster
SET Rank = 'Captain'
WHERE Name = 'Benjamin Sisko';

UPDATE Roster
SET Rank = 'Major'
WHERE Name = 'Kira Nerys';

-- Note: The following update has no effect as Ezri was already deleted
UPDATE Roster
SET Rank = 'Lieutenant'
WHERE Name = 'Ezri Dax';

-- 7. Retrieve all characters sorted by Age descending
SELECT * FROM Roster ORDER BY Age DESC;
