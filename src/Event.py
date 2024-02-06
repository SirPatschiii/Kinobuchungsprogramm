import sqlite3
import logging as log


class Event:
    def __init__(self):
        log.debug("Event works!")

        self.cursor_db = None
        self.connect = None

    def __connect_db(self):
        try:
            self.connect = sqlite3.connect("src/cinemadata.db")
            log.debug("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

        try:
            self.connect = sqlite3.connect("../src/cinemadata.db")
            log.debug("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            log.exception(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            log.exception(f"Database error: {e}")

        self.cursor_db = self.connect.cursor()

    def __disconnect_db(self):
        self.connect.close()

    def title(self, event_id):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT date FROM events WHERE eventID='{event_id}'")
        event = self.cursor_db.fetchone()
        self.__disconnect_db()
        return event[0] if event else None
