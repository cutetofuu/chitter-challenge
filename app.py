from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager! \n")
        print("What would you like to do? \n 1 - List all albums \n 2 - List all artists \n")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()

            print("\nHere is the list of albums:")
            for album in albums:
                print(f"* {album.id} - {album.title}")
        elif user_input == "2":
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()

            print("\nHere is the list of artists:")
            for artist in artists:
                print(f"* {artist.id} - {artist.name} ({artist.genre})")
        else:
            print("Invalid input.")
            

if __name__ == '__main__':
    app = Application()
    app.run()