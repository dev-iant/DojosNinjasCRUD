INSERT INTO dojos (name, created_at, updated_at)
VALUES 
("Jarrod", now(), now()),
("Jessica", now(), now()),
("Beauregarde", now(), now());

SELECT * FROM dojos;

DELETE FROM dojos
WHERE iddojo <= 3;

INSERT INTO dojos (name, created_at, updated_at)
VALUES 
("Colorado", now(), now()),
("Tokyo", now(), now()),
("London", now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_iddojo, created_at, updated_at)
VALUES
("Jose", "Bonilla", 52, 4, now(), now()),
("Carlos", "Alvarez", 19, 4, now(), now()),
("Luke", "P", 24, 4, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_iddojo, created_at, updated_at)
VALUES
("Jarrod", "Vickers", 32, 5, now(), now()),
("Rindy", "Fisk", 41, 5, now(), now()),
("May", "Schatz", 24, 5, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_iddojo, created_at, updated_at)
VALUES
("Sam", "R", 28, 6, now(), now()),
("Adrian", "Adrian", 22, 6, now(), now()),
("Haley", "Beltran", 37, 6, now(), now());

SELECT * FROM ninjas;

SELECT * FROM ninjas
WHERE dojo_iddojo = 4;

SELECT * FROM ninjas
WHERE dojo_iddojo = 6;

SELECT dojo_iddojo FROM ninjas
WHERE idninja = 9;