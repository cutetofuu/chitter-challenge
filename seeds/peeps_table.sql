DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT,
    password TEXT,
    name TEXT,
    username TEXT
);

CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    message VARCHAR(280),
    created_at TIMESTAMP,
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

INSERT INTO users 
    (email, password, name, username) 
VALUES 
    ('david@test.com', '40ccbdf74ca095cbf6a05ede129d3aebdaa16e799b5897be82ca0948fd995d20', 'David', 'dave_test'),
    ('jane@test.com', '74003ee4634d383f4a1921d434f16e6ef14e2a3259246c130e8a31055250635e', 'Jane', 'jane_test'),
    ('pickle@test.com', '7052d09741567eaa79757c241d3ee5e2022ad63690ef0f3b2e02f62d5ca6cf6e', 'Pickle', 'pickle_test'),
    ('john@test.com', 'c6e8b79a09af0a5955447f0fc10348e911a867d11aa4505d411081ace5aa4298', 'John', 'john_test');

INSERT INTO peeps 
    (message, created_at, user_id) 
VALUES 
    ('Hello! This is my very first chitter message!', '2023-05-10 09:05:06', 4),
    ('Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode', '2023-04-22 17:38:19', 1),
    ('I am a cute little kitty cat, and I had a really long nap just now! #toughlife','2023-05-16 14:15:54', 3),
    ('Had a great time at the Makers Academy today! It was fun learning about databases and web apps in Python', '2023-03-08 16:45:30', 2);
