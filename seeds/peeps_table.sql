DROP TABLE IF EXISTS peeps;
DROP TABLE IF EXISTS users;

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
    ('david@test.com', 'password111', 'David', 'dave_test'),
    ('jane@test.com', 'password222', 'Jane', 'jane_test'),
    ('pickle@test.com', 'password333', 'Pickle', 'pickle_test'),
    ('john@test.com', 'password444', 'John', 'john_test');

INSERT INTO peeps 
    (message, created_at, user_id) 
VALUES 
    ('Hello! This is my very first chitter message!', '2023-05-10 09:05:06', 4),
    ('Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode', '2023-04-22 17:38:19', 1),
    ('I am a cute little kitty cat, and I had a really long nap just now! #toughlife','2023-05-16 14:15:54', 3),
    ('Had a great time at the Makers Academy today! It was fun learning about databases and web apps in Python', '2023-03-08 16:45:30', 2);
