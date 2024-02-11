import sqlite3
import logging as log
import os


class Movie:
    def __init__(self):
        log.debug("Movie works!")

        self.__cursor_db = None
        self.__connect = None
        self.__selected_movie = ""
        self.__selected_hall_id = None

    def __connect_db(self):
        current_file_path = os.path.abspath(__file__)
        project_root = os.path.dirname(os.path.dirname(current_file_path))
        database_path = os.path.join(project_root, "src", "cinemadata.db")
        try:
            self.__connect = sqlite3.connect(database_path)
            log.debug("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

        self.__cursor_db = self.__connect.cursor()

    def __disconnect_db(self):
        try:
            self.__connect.close()
            log.debug("Disconnect from the database was successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error disconnecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

    def set_selected_cinema(self, hall_id):
        self.__selected_hall_id = hall_id

    def get_selected_cinema(self):
        return self.__selected_hall_id

    def get_movie_title(self):
        self.__connect_db()
        hall_id = self.__selected_hall_id
        self.__cursor_db.execute(f"SELECT name FROM movie WHERE hallID='{hall_id}'")
        movies = self.__cursor_db.fetchall()
        return [movie[0] for movie in movies] if movies else []

    def set_selected_movie(self, movie_title_lbl):
        self.__selected_movie = movie_title_lbl

    def get_selected_movie(self):
        return self.__selected_movie

    def get_movie_description(self):
        self.__connect_db()
        movie_descriptions = []
        movie_titles = self.get_movie_title()
        for title in movie_titles:
            self.__cursor_db.execute(f"SELECT description FROM movie WHERE name='{title}'")
            description = self.__cursor_db.fetchone()
            movie_descriptions.append(description[0] if description else None)
        return movie_descriptions
