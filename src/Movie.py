import sqlite3


class Movie:
    def __init__(self):
        self.cursor_db = None
        print("Movie works!")

    def connect_db(self):
        connect = None
        try:
            connect = sqlite3.connect("src/cinemadata.db")
        except Exception:
            pass
        try:
            connect = sqlite3.connect("../src/cinemadata.db")
        except Exception:
            pass
        self.cursor_db = connect.cursor()


    def title(self, movieID):
        self.cursor_db.execute(f"SELECT name FROM movie WHERE movieID='{movieID}'")
        movie = self.cursor_db.fetchone()
        return movie[0] if movie else None

