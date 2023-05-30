from playwright.sync_api import Page, expect

def test_get_peeps(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")
    name_tags = page.locator(".t-name")
    username_tags = page.locator(".t-username")
    message_tags = page.locator(".t-peep")
    created_at_tags = page.locator(".t-created-at")
    expect(message_tags).to_have_text([
        "I am a cute little kitty cat, and I had a really long nap just now! #toughlife",
        "Hello! This is my very first chitter message!",
        "Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode",
        "Had a great time at the Makers Academy today! It was fun learning about databases and web apps in Python"
    ])
    expect(created_at_tags).to_have_text([
        "2023-05-16 14:15:54",
        "2023-05-10 09:05:06",
        "2023-04-22 17:38:19",
        "2023-03-08 16:45:30"
    ])
    expect(name_tags).to_have_text([
        "Pickle",
        "John",
        "David",
        "Jane"
    ])
    expect(username_tags).to_have_text([
        "@pickle_test",
        "@john_test",
        "@dave_test",
        "@jane_test"
    ])

def test_create_user(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.fill("input[name=email]", "test@test.com")
    page.fill("input[name=password]", "password456!")
    page.fill("input[name=name]", "Arnie")
    page.fill("input[name=username]", "arnie_test")

    page.click("text='Create New Account'")

    account_success_tag = page.locator("h2")
    expect(account_success_tag).to_have_text("Account successfully created.")

def test_create_user_no_input_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.click("text='Create New Account'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Email can't be blank, Password can't be blank, Name can't be blank, Username can't be blank")

def test_create_user_valid_email_and_password_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.fill("input[name=email]", "test@test.com")
    page.fill("input[name=password]", "password456!")

    page.click("text='Create New Account'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Username can't be blank")

def test_create_user_valid_email_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.fill("input[name=email]", "test@test.com")

    page.click("text='Create New Account'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Password can't be blank, Name can't be blank, Username can't be blank")

def test_create_user_invalid_email_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.fill("input[name=email]", "test.com")

    page.click("text='Create New Account'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Invalid email, Password can't be blank, Name can't be blank, Username can't be blank")

def test_create_user_valid_password_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.fill("input[name=password]", "password456&")

    page.click("text='Create New Account'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Email can't be blank, Name can't be blank, Username can't be blank")

def test_create_user_invalid_password_length_and_characters_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.fill("input[name=password]", "pass1")

    page.click("text='Create New Account'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Email can't be blank, Password must be at least 8 characters long, Password must have at least 1 special character, Name can't be blank, Username can't be blank")

def test_create_user_invalid_password_length_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Sign Up'")

    page.fill("input[name=password]", "pass1&")

    page.click("text='Create New Account'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Email can't be blank, Password must be at least 8 characters long, Name can't be blank, Username can't be blank")


def test_create_peep(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Login'")

    page.fill("input[name=email]", 'john@test.com')
    page.fill("input[name=password]", 'password444%')

    page.click("text='Login'")

    page.click("text='Back to home'")
    
    page.fill("textarea[name=message]", "Hello! I'm new to Chitter.")

    page.click("text='Peep'")

    name_tags = page.locator(".t-name")
    username_tags = page.locator(".t-username")
    message_tags = page.locator(".t-peep")
    created_at_tags = page.locator(".t-created-at")
    expect(message_tags).to_have_text([
        "Hello! I'm new to Chitter.",
        "I am a cute little kitty cat, and I had a really long nap just now! #toughlife",
        "Hello! This is my very first chitter message!",
        "Today I made a shop manager program using Python, Pytest, Psycopg and PostgreSQL #100daysofcode",
        "Had a great time at the Makers Academy today! It was fun learning about databases and web apps in Python"
    ])
    expect(created_at_tags).to_have_count(5)
    expect(name_tags).to_have_text([
        "John",
        "Pickle",
        "John",
        "David",
        "Jane"
    ])
    expect(username_tags).to_have_text([
        "@john_test",
        "@pickle_test",
        "@john_test",
        "@dave_test",
        "@jane_test"
    ])

def test_create_peep_no_input_given_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Login'")

    page.fill("input[name=email]", 'pickle@test.com')
    page.fill("input[name=password]", 'password333#')

    page.click("text='Login'")

    page.click("text='Back to home'")

    page.click("text='Peep'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Peep can't be blank")

def test_user_login(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Login'")

    page.fill("input[name=email]", 'john@test.com')
    page.fill("input[name=password]", 'password444%')

    page.click("text='Login'")

    login_success_tag = page.locator("h2")
    expect(login_success_tag).to_have_text("Successfully logged in.")

def test_user_login_errors(page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_table.sql')
    page.goto(f"http://{test_web_address}/home")

    page.click("text='Login'")

    page.fill("input[name=email]", 'notauser@test.com')
    page.fill("input[name=password]", 'password777!')

    page.click("text='Login'")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("Sorry, your email/password was incorrect.")