import sqlite3
import logging as log
import os


class Movie:
    def __init__(self):
        log.debug("Movie works!")

        self.cursor_db = None
        self.connect = None

    def __connect_db(self):
        current_file_path = os.path.abspath(__file__)
        project_root = os.path.dirname(os.path.dirname(current_file_path))
        database_path = os.path.join(project_root, "src", "cinemadata.db")
        try:
            self.connect = sqlite3.connect(database_path)
            log.debug("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

        self.cursor_db = self.connect.cursor()

    def __disconnect_db(self):
        try:
            self.connect.close()
            log.debug("Disconnect from the database was successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error disconnecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

    def title(self, movie_id):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT name FROM movie WHERE movieID='{movie_id}'")
        movie = self.cursor_db.fetchone()
        self.__disconnect_db()
        return movie[0] if movie else None

    def movie_description(self, movie_id):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT description FROM movie WHERE movieID='{movie_id}'")
        movie = self.cursor_db.fetchone()
        self.__disconnect_db()
        return movie[0] if movie else None
