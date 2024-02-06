import sqlite3
import logging as log
import os


class Cinema:
    def __init__(self):
        log.debug("Cinema Works!")

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

    def title(self):
        self.__connect_db()
        self.cursor_db.execute("SELECT name FROM cinema WHERE hallID='1'")
        user_data = self.cursor_db.fetchall()
        self.__disconnect_db()
        return user_data

    def get_booked_seats(self):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT booked_seats FROM cinema WHERE hallID='1'")
        booked_seats = self.cursor_db.fetchone()
        self.__disconnect_db()

        booked_seats_bool = [None for _ in range(20)]
        c = 0
        for i, character in enumerate(str(booked_seats)):
            match character:
                case "0":
                    booked_seats_bool[i - c] = False
                case "1":
                    booked_seats_bool[i - c] = True
                case _:
                    c += 1
                    continue

        return booked_seats_bool
