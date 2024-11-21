BEGIN;
CREATE TABLE IF NOT EXISTS student_reg(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT UNIQUE,
                last_name TEXT UNIQUE,
                email TEXT,
                addres TEXT,
                mobile_number INTEGER);

INSERT INTO IGNORE INTO student_reg
    (first_name, last_name, email, addres, mobile_number)
    VALUES
    (?,?,?,?,?);
COMMIT;
                
