import logging as log
import sqlite3
import os


class Booking:
    def __init__(self):
        log.debug("Booking works!")

        self.connect = None

        self.__selected_cinema = ""
        self.__selected_movie = ""
        self.__selected_event = ""

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
        self.connect.close()

    def set_selected_cinema(self, cinema_title):
        self.__selected_cinema = cinema_title

    def get_selected_cinema(self):
        return self.__selected_cinema

    def set_selected_movie(self, movie_title_lbl):
        self.__selected_movie = movie_title_lbl

    def get_selected_movie(self):
        return self.__selected_movie

    def set_selected_event(self, event_rad_selection):
        self.__selected_event = event_rad_selection

    def get_selected_event(self):
        print(self.__selected_event)
        return self.__selected_event

    def get_selected_seats(self):
        pass