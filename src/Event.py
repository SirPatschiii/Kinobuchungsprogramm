import sqlite3
import logging as log
import os


class Event:
    def __init__(self):
        log.debug("Event works!")

        self.cursor_db = None
        self.connect = None
        self.__movie_id = ""

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

    def set_movie_id(self, movie_id):
        self.__movie_id = movie_id

    def get_movie_id(self):
        return self.__movie_id

    def get_event_title(self):
        self.__connect_db()
        hall_id = self.__selected_hall_id
        movie_id = self.__movie_id
        # TODO movie_id wird nicht richtig abgerufen
        self.cursor_db.execute(f"""
            SELECT date 
            FROM events 
            WHERE hallID='{hall_id}' AND movieID='1'""")
        events = self.cursor_db.fetchall()
        self.__disconnect_db()
        return [event[0] for event in events] if events else []

