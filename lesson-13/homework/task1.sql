CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';

DELETE FROM Roster WHERE Age > 100;

ALTER TABLE Roster ADD COLUMN Rank TEXT;

UPDATE Roster
SET Rank = 'Captain'
WHERE Name = 'Benjamin Sisko';

UPDATE Roster
SET Rank = 'Major'
WHERE Name = 'Kira Nerys';

UPDATE Roster
SET Rank = 'Lieutenant'
WHERE Name = 'Ezri Dax';

SELECT * FROM Roster ORDER BY Age DESC;
