from lib.user import User

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
        self._connection.execute('INSERT INTO users (email, password, name, username) VALUES (%s, %s, %s, %s)', [user.email, user.password, user.name, user.username])

    def update(self, user):
        self._connection.execute('UPDATE users SET email = %s, password = %s, name = %s, username = %s WHERE id = %s', [user.email, user.password, user.name, user.username, user.id])

    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])