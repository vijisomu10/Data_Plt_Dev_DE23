BEGIN;
-- DROP TABLE members;

CREATE TABLE IF NOT EXISTS employer(
    employer_id INTEGER PRIMARY KEY, employer_name TEXT);

CREATE TABLE IF NOT EXISTS members(
    id INTEGER PRIMARY KEY, fn TEXT UNIQUE, ln TEXT, employerFK INTEGER, 
    FOREIGN KEY(employerFK) REFERENCES employer(employer_id));

INSERT OR IGNORE INTO members(id, fn, ln, employerFK) 
VALUES(1, 'Homer', 'Simpson', 1001);

INSERT OR IGNORE INTO members(id, fn, ln, employerFK) 
VALUES(2, 'Marge', 'Simpson', NULL);

INSERT OR IGNORE INTO members(id, fn, ln, employerFK) 
VALUES(3, 'Lisa', 'Simpson', NULL);

INSERT OR IGNORE INTO members(id, fn, ln, employerFK) 
VALUES(4, 'Bart', 'Simpson', NULL);

INSERT OR IGNORE INTO employer
VALUES (1001, 'Nuclear Power Plant');
COMMIT;