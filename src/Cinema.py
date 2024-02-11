import sqlite3
import logging as log
import os


class Cinema:
    def __init__(self):
        log.debug("Cinema Works!")

        self.__cursor_db = None
        self.__connect = None
        self.__selected_event = ""
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

    def get_all_cinemas(self):
        self.__connect_db()
        self.__cursor_db.execute("SELECT hallID, name FROM cinema")
        cinemas = self.__cursor_db.fetchall()
        self.__disconnect_db()
        return cinemas

    def title(self, hall_id):
        self.__connect_db()
        self.__cursor_db.execute(f"SELECT name FROM cinema WHERE hallID= '{hall_id}' ")
        user_data = self.__cursor_db.fetchall()
        self.__disconnect_db()
        return user_data[0] if user_data else None

    def get_total_seats(self):
        self.__connect_db()
        self.__cursor_db.execute(f"SELECT total_seats FROM cinema WHERE hallID='1'")
        total_seats = self.__cursor_db.fetchone()
        self.__disconnect_db()
        return total_seats

    def set_selected_event(self, event_rad_selection):
        self.__selected_event = event_rad_selection

    def get_selected_event(self):
        return self.__selected_event

    def set_selected_cinema(self, hall_id):
        self.__selected_hall_id = hall_id

    def get_selected_cinema(self):
        return self.__selected_hall_id

    def set_selected_movie(self, movie_title_lbl):
        self.__selected_movie = movie_title_lbl

    def get_selected_movie(self):
        return self.__selected_movie

    def get_booked_seats(self):
        self.__connect_db()
        selected_event = self.__selected_event
        hall_id = self.__selected_hall_id
        movie = self.__selected_movie
        self.__cursor_db.execute(f"""
            SELECT e.booked_seats
            FROM events e
            INNER JOIN movie m ON e.movieID = m.movieID
            WHERE e.hallID = '{hall_id}' AND m.name = '{movie}' AND e.date = '{selected_event}' """)
        booked_seats_str = self.__cursor_db.fetchone()[0]
        self.__disconnect_db()

        booked_seats = ['green' if seat == '0' else 'red' for seat in booked_seats_str]
        return booked_seats
