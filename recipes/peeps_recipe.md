# Peeps Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

```
# EXAMPLE

Table: peeps

Columns:
id | message | created_at | user_id
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
INSERT INTO peeps 
    (message, created_at, user_id) 
VALUES 
    ('Hello! This is my very first chitter message!', 'password111', datetime.now(), 4),
    ('Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode', datetime.now(), 1),
    ('I am a cute little kitty cat, and I had a really long nap just now! #toughlife', datetime.now(), 3),
    ('Had a great time at the Makers Academy today! It was fun learning about databases and web apps in Python', datetime.now(), 2);

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 chitter < peeps_table.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# Table name: peeps

# Model class
# (in lib/peep.py)
class Peep


# Repository class
# (in lib/peep_repository.py)
class PeepRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# Table name: peeps

# Model class
# (in lib/peep.py)

class Peep:
    def __init__(self):
        self.id = 0
        self.message = ""
        self.created_at = ""
        self.user_id = 0
```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# Table name: peeps

# Repository class
# (in lib/peep_repository.py)

class PeepRepository():
    def all():
        # Executes the SQL query:
        # SELECT * FROM peeps;

        # Returns an array of Peep objects.

    def find(id):
        # Executes the SQL query:
        # SELECT * FROM peeps WHERE id = %s;

        # Returns a single Peep object.

    def create(peep)
        # Executes the SQL query:
        # INSERT INTO peeps (message, created_at, user_id) VALUES (%s, %s, %s);

        # Creates a new Peep object.
        # Returns None

    def delete(peep)
        # Executes the SQL query:
        # DELETE FROM peeps WHERE id = %s;

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# 1
# Get all peeps

repo = PeepRepository()

peeps = repo.all()

len(peeps) # =>  4

peeps[0].id # =>  1
peeps[0].message # =>  'Hello! This is my very first chitter message!'
peeps[0].created_at # =>  '2023-05-10 09:05:06'
peeps[0].user_id # =>  4

peeps[1].id # =>  2
peeps[1].message # =>  'Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode'
peeps[1].created_at # =>  2023-04-22 17:38:19'
peeps[1].user_id # =>  1

# 2
# Get a single peep

repo = PeepRepository()

peep = repo.find(3)

peep.id # =>  3
peep.message # =>  'I am a cute little kitty cat, and I had a really long nap just now! #toughlife'
peep.created_at # =>  '2023-05-16 14:15:54'
peep.user_id # =>  3


# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
