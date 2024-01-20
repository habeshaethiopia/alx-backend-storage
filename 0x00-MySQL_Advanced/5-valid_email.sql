-- SQL script that creates a trigger that resets the 
-- attribute valid_email only when the email has been changed.
DROP TRIGGER IF EXISTS reset_valid_email;

CREATE trigger reset_valid_email
AFTER
UPDATE
    ON users FOR EACH ROW
UPDATE
    users
SET
    valid_email = 0
WHERE
    id = new.id
    AND new.email <> old.email;