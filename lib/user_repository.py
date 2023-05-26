from lib.user import User
import hashlib

class UserRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users ORDER BY id')
        users = []
        for row in rows:
            user = User(row['id'], row['email'], row['password'], row['name'], row['username'])
            users.append(user)
        return users
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [id])
        return User(rows[0]['id'], rows[0]['email'], rows[0]['password'], rows[0]['name'], rows[0]['username'])
    
    def create(self, user):
        binary_password = user._password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        self._connection.execute('INSERT INTO users (email, password, name, username) VALUES (%s, %s, %s, %s)', [user._email, hashed_password, user.name, user.username])

    def update(self, user):
        self._connection.execute('UPDATE users SET email = %s, password = %s, name = %s, username = %s WHERE id = %s', [user._email, user._password, user.name, user.username, user.id])

    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])

    def check_password(self, email, password_attempt):
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        rows = self._connection.execute('SELECT * FROM users WHERE email = %s AND password = %s', [email, hashed_password_attempt])

        return len(rows) > 0
    
    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        return User(rows[0]['id'], rows[0]['email'], rows[0]['password'], rows[0]['name'], rows[0]['username'])
    