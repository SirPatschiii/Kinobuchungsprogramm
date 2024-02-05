import sqlite3
import logging as log


class Cinema:
    def __init__(self):
        log.debug("Cinema Works!")

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

    def title(self):
        self.cursor_db.execute("SELECT name FROM cinema WHERE hallID='1'")
        user_data = self.cursor_db.fetchall()
        return user_data
