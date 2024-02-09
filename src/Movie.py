import sqlite3
import logging as log
import os


class Movie:
    def __init__(self):
        log.debug("Movie works!")

        self.cursor_db = None
        self.connect = None
        self.__selected_movie = ""
        self.__selected_hall_id = None

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

    def set_selected_cinema(self, hall_id):
        self.__selected_hall_id = hall_id

    def get_selected_cinema(self):
        return self.__selected_hall_id

    def get_movie_title(self):
        self.__connect_db()
        hall_id = self.__selected_hall_id
        self.cursor_db.execute(f"SELECT name FROM movie WHERE hallID='{hall_id}'")
        movies = self.cursor_db.fetchall()
        return [movie[0] for movie in movies] if movies else []

    def set_selected_movie(self, movie_title_lbl):
        self.__selected_movie = movie_title_lbl

    def get_selected_movie(self):
        return self.__selected_movie

    def get_movie_id(self):
        self.cursor_db()
        movie_title = self.__selected_movie
        self.cursor_db.execute(f"SELECT movieID FROM movie WHERE name='{movie_title}'")
        movie_id = self.cursor_db.fetchone()
        return movie_id
        # TODO movie_id wird nicht bzw. nicht richtig abgerufen


    def movie_description(self):
        self.__connect_db()
        movie_descriptions = []
        movie_titles = self.get_movie_title()
        for title in movie_titles:
            self.cursor_db.execute(f"SELECT description FROM movie WHERE name='{title}'")
            description = self.cursor_db.fetchone()
            movie_descriptions.append(description[0] if description else None)
        return movie_descriptions
