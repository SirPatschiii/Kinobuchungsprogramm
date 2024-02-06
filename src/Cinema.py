import sqlite3
import logging as log


class Cinema:
    def __init__(self):
        log.debug("Cinema Works!")

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

    def title(self):
        self.__connect_db()
        self.cursor_db.execute("SELECT name FROM cinema WHERE hallID='1'")
        user_data = self.cursor_db.fetchall()
        self.__disconnect_db()
        return user_data
