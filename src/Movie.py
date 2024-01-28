import sqlite3


class Movie:
    def __init__(self):
        self.cursor_db = None
        print("Movie works!")

    def connect_db(self):
        connect = sqlite3.connect("cinemadata.db")
        self.cursor_db = connect.cursor()


    def title(self, movieID):
        self.cursor_db.execute(f"SELECT name FROM movie WHERE movieID='{movieID}'")
        movie = self.cursor_db.fetchone()
        return movie[0] if movie else None

