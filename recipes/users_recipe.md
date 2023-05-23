# Users Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

```
# EXAMPLE

Table: users

Columns:
id | email | password | name | username
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
INSERT INTO users 
    (email, password, name, username) 
VALUES 
    ('david@test.com', 'password111', 'David', 'dave_test'),
    ('jane@test.com', 'password222', 'Jane', 'jane_test'),
    ('pickle@test.com', 'password333', 'Pickle', 'pickle_test'),
    ('john@test.com', 'password444', 'John', 'john_test');

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 chitter < peeps_table.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# Table name: users

# Model class
# (in lib/user.py)
class User


# Repository class
# (in lib/user_repository.py)
class UserRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# Table name: users

# Model class
# (in lib/user.py)

class User:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.password = ""
        self.name = ""
        self.username = ""
```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# Table name: users

# Repository class
# (in lib/user_repository.py)

class UserRepository():
    def all():
        # Executes the SQL query:
        # SELECT * FROM users;

        # Returns an array of User objects.

    def find(id):
        # Executes the SQL query:
        # SELECT * FROM users WHERE id = %s;

        # Returns a single User object.

    def create(user)
        # Executes the SQL query:
        # INSERT INTO users (email, password, name, username) VALUES (%s, %s, %s, %s);

        # Creates a new User object.
        # Returns None

    def update(user)
        # Executes the SQL query:
        # UPDATE users SET email = %s, password = %s, name = %s, username = %s WHERE id = %s;

    def delete(user)
        # Executes the SQL query:
        # DELETE FROM users WHERE id = %s;

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# 1
# Get all users

repo = UserRepository()

users = repo.all()

len(users) # =>  4

users[0].id # =>  1
users[0].email # =>  'david@test.com'
users[0].password # =>  'password111'
users[0].name # =>  'David'
users[0].username # =>  'dave_test'

users[1].id # =>  2
users[1].email # =>  'jane@test.com'
users[1].password # =>  'password222'
users[1].name # =>  'Jane'
users[1].username # =>  'jane_test'

# 2
# Get a single user

repo = UserRepository()

user = repo.find(3)

user.id # =>  3
user.email # =>  'pickle@test.com'
user.password # =>  'password333'
user.name # =>  'Pickle'
user.username # =>  'pickle_test'


# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
