from lib.peep import Peep

class PeepRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM peeps')
        peeps = [] 
        for row in rows:
            peep = Peep(row['id'], row['message'], str(row['created_at']), row['user_id'])
            peeps.append(peep)
        return peeps
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM peeps WHERE id = %s', [id])
        return Peep(rows[0]['id'], rows[0]['message'], str(rows[0]['created_at']), rows[0]['user_id'])
    
    def create(self, peep):
        self._connection.execute('INSERT INTO peeps (message, created_at, user_id) VALUES (%s, %s, %s)', [peep.message, peep.created_at, peep.user_id])

    def delete(self, id):
        self._connection.execute('DELETE FROM peeps WHERE id = %s', [id])