-- update valid_email column if it changes
-- TRIGGER UPDATES VALUE IN TABLE IF EMAIL CHANGE

DROP TRIGGER IF EXISTS valid_email
CREATE TRIGGER valid_email
DELIMITER $$
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = NEW.valid_email;
    END IF;
END $$
DELIMITER ;
