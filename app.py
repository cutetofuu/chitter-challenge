import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.peep_repository import PeepRepository
from lib.peep import Peep
from lib.user_repository import UserRepository
from lib.user import User
from datetime import datetime

# Create a new Flask app
app = Flask(__name__)

# PEEPS ROUTES

@app.route("/home", methods=["GET"])
def get_all_peeps():
    connection = get_flask_database_connection(app)
    peep_repo = PeepRepository(connection)
    peeps = peep_repo.all_with_usernames()
    return render_template("peeps/index.html", peeps=peeps)

@app.route("/home", methods=["POST"])
def create_new_peep():
    connection = get_flask_database_connection(app)
    peep_repo = PeepRepository(connection)
    peeps = peep_repo.all_with_usernames()
    
    message = request.form["message"]
    created_at = datetime.now()
    user_id = 3

    peep = Peep(None, message, created_at, user_id)

    if not peep.is_valid():
        return render_template('peeps/index.html', peeps=peeps, peep=peep, errors=peep.generate_errors()), 400

    peep_repo.create(peep)

    return redirect("/home")

# USERS ROUTES

@app.route("/signup", methods=["GET"])
def get_new_user():
    return render_template("users/signup.html")

@app.route("/signup", methods=["POST"])
def create_new_user():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)

    email = request.form["email"]
    password = request.form["password"]
    name = request.form["name"]
    username = request.form["username"]

    user = User(None, email, password, name, username)

    if not user.is_valid():
        return render_template('users/signup.html', user=user, errors=user.generate_errors()), 400

    user_repo.create(user)

    return redirect("/signup-success")

@app.route("/signup-success", methods=["GET"])
def get_new_user_confirmation():
    return render_template("users/signup_success.html")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
