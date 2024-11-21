BEGIN;
CREATE TABLE IF NOT EXISTS members(id PRIMARY KEY, fn, ln);
INSERT OR IGNORE INTO members VALUES(1, "Homer", "Simpson");
INSERT OR IGNORE INTO members VALUES(2, "Marge", "Simpson");
INSERT OR IGNORE INTO members VALUES(3, "Lisa", "Simpson");
INSERT OR IGNORE INTO members VALUES(4, "Bart", "Simpson");
COMMIT;