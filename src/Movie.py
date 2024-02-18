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
        # This method creates the connection to the database
        # Therefor the absolute path is determined to secure the connection is successful
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
        # close the connection to the database
        try:
            self.__connect.close()
            log.debug("Disconnect from the database was successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error disconnecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

    def set_selected_cinema(self, hall_id):
        # get selected_hall_id from the controller
        self.__selected_hall_id = hall_id

    def get_selected_cinema(self):
        # output the selected_hall_id from set_selected_cinema
        return self.__selected_hall_id

    def get_movie_title(self):
        # call the name of the movie with the selected hall_id out of the database
        self.__connect_db()
        hall_id = self.__selected_hall_id
        self.__cursor_db.execute(f"SELECT name FROM movie WHERE hallID='{hall_id}'")
        movies = self.__cursor_db.fetchall()
        return [movie[0] for movie in movies] if movies else []

    def set_selected_movie(self, movie_title_lbl):
        # get the selected_movie from the controller
        self.__selected_movie = movie_title_lbl

    def get_selected_movie(self):
        # output the selected_movie from set_selected_movie
        return self.__selected_movie

    def get_movie_description(self):
        # call the description to each movie out of the database and put it in a list.
        # output the list of the movie descriptions
        self.__connect_db()
        movie_descriptions = []
        movie_titles = self.get_movie_title()
        for title in movie_titles:
            self.__cursor_db.execute(f"SELECT description FROM movie WHERE name='{title}'")
            description = self.__cursor_db.fetchone()
            movie_descriptions.append(description[0] if description else None)
        return movie_descriptions
