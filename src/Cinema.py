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

    def title(self, hall_id):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT name FROM cinema WHERE hallID= '{hall_id}' ")
        user_data = self.cursor_db.fetchall()
        self.__disconnect_db()
        return user_data[0] if user_data else None

    def get_total_seats(self):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT total_seats FROM cinema WHERE hallID='1'")
        total_seats = self.cursor_db.fetchone()
        self.__disconnect_db()
        return total_seats

    def get_booked_seats(self):
        self.__connect_db()
        self.cursor_db.execute(f"SELECT booked_seats FROM cinema WHERE hallID='1'")
        booked_seats_str = self.cursor_db.fetchone()[0]
        self.__disconnect_db()

        booked_seats = ['green' if seat == '0' else 'red' for seat in booked_seats_str]
        return booked_seats
