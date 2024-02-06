import sqlite3
import logging as log
import os


class Event:
    def __init__(self):
        log.debug("Event works!")

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

    def title(self, event_id):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT date FROM events WHERE eventID='{event_id}'")
        event = self.cursor_db.fetchone()
        self.__disconnect_db()
        return event[0] if event else None
