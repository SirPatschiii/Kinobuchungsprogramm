import sqlite3
import logging as log


class Movie:
    def __init__(self):
        log.debug("Movie works!")

        self.cursor_db = None

    def connect_db(self):
        connect = None

        try:
            connect = sqlite3.connect("src/cinemadata.db")
            log.debug("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

        try:
            connect = sqlite3.connect("../src/cinemadata.db")
            log.debug("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

        self.cursor_db = connect.cursor()

    def title(self, movie_id):
        self.cursor_db.execute(f"SELECT name FROM movie WHERE movieID='{movie_id}'")
        movie = self.cursor_db.fetchone()
        return movie[0] if movie else None

    def movie_description(self, movie_id):
        self.cursor_db.execute(f"SELECT description FROM movie WHERE movieID='{movie_id}'")
        movie = self.cursor_db.fetchone()
        return movie[0] if movie else None
