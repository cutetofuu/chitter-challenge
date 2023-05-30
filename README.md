# Chitter

## Project Summary

This is a small web application that mimics some of the features of Twitter. It is written using Python, Flask, HTML, Jinja templates, Psycopg, and uses PostgreSQL as a database. Unit and integrated testing are done using Pytest and Playwright.

## Features

`peeps`

  - Shows a collection of peeps in reverse chronological order
  - Posts a new peep •only• if a user is logged in

`users`

  - Allows a new user to sign up for Chitter
  - Allows an existing user to log in and log out

## Instructions

1. Fork and clone this repository.

2. Set up and activate the virtual environment by running `pipenv install` and then `pipenv shell`.

3. Create the databases using the following scripts:
    - Development database: `createdb chitter`
    - Test database: `createdb chitter_test`

4. Seed the development database: `python seed_dev_database.py`

5. Install pytest for the tests: `pipenv install pytest`

6. Run the tests: `pytest`

7. Run the app: `python app.py`

8. Open up your browser and type in `localhost:5000/[insert path here]`. The available routes are found below.

## Routes

### `/home`
- User can view a collection of peeps, even if they're not logged in.
- User can post a new peep •only• if they're logged in.

### `/signup`
- User can sign up for Chitter using a valid email, password, name and username.

### `/login`
- User can sign up for Chitter using a valid email and password.

### `/logout`
- Lets a user know that they've successfully signed up to Chitter.
- Provides a link to take the user back to the home page.

## Features I would like to fix/add

- [ ] Fix timestamp for new peeps to not display milliseconds
- [ ] Fix password input box to not display the typed-in password
- [ ] Show a page for a specific peep
    - when the peep id is given
    - or a peep is clicked on
- [ ] Update the like count for a specific peep
- [ ] Delete an existing peep
- [ ] Receive an email if tagged in a peep
- [ ] Check if username and email already exist when signing up
- [ ] Show a page for a specific user, with a list of all of their peeps
