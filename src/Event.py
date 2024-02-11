import sqlite3
import logging as log
import os


class Event:
    def __init__(self):
        log.debug("Event works!")

        self.__cursor_db = None
        self.__connect = None
        self.__movie_id = ""
        self.__selected_movie = None
        self.__selected_hall_id = int()

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

    def set_selected_movie(self, movie_title_lbl):
        self.__selected_movie = movie_title_lbl

    def get_selected_movie(self):
        return self.__selected_movie

    def get_event_title(self):
        self.__connect_db()
        hall_id = self.__selected_hall_id
        movie = self.__selected_movie
        # TODO movie_id wird nicht richtig abgerufen
        self.__cursor_db.execute(f"""
            SELECT e.date, m.name
            FROM events e
            INNER JOIN movie m ON e.movieID = m.movieID
            WHERE e.hallID = '{hall_id}' AND m.name = '{movie}' """)
        events = self.__cursor_db.fetchall()
        self.__disconnect_db()
        return [event[0] for event in events] if events else []
