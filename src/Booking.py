import logging as log
import sqlite3
import os


class Booking:
    def __init__(self):

        log.debug("Booking works!")

        self.cursor_db = None
        self.connect = None

        self.__selected_cinema = ""
        self.__selected_movie = ""
        self.__selected_event = ""
        self.__booked_seats = ""
        self.__booking_id = None
        self.__selected_seats = None

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

    def set_selected_cinema(self, cinema_title, hall_id):
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
        return self.__selected_event

    def set_booked_seats(self, seat_list):
        self.__booked_seats = seat_list

    def get_booked_seats(self):
        return self.__booked_seats

    def set_selected_seats(self, selected_seats):
        self.__selected_seats = selected_seats

    def get_selected_seats(self):
        return self.__selected_seats

    def update_database(self):
        try:
            self.__connect_db()
            selected_seats_str = ', '.join(str(seat) for seat in self.__selected_seats)
            cinema_title = self.__selected_cinema[0] if self.__selected_cinema else ""
            self.cursor_db.execute("""
                SELECT hallID 
                FROM cinema 
                WHERE name=?""", (cinema_title,))
            hall_id = self.cursor_db.fetchone()[0]

            self.cursor_db.execute("""
                SELECT movieID 
                FROM movie 
                WHERE name=?""", (self.__selected_movie,))

            movie_id = self.cursor_db.fetchone()[0]

            self.cursor_db.execute("""
                SELECT eventID 
                FROM events 
                WHERE date=?""", (self.__selected_event,))
            event_id = self.cursor_db.fetchone()[0]

            self.cursor_db.execute(
                "INSERT INTO bookings (hallID, movieID, eventID, selected_seats) VALUES (?, ?, ?, ?)",
                (hall_id, movie_id, event_id, selected_seats_str))
            self.connect.commit()

            self.cursor_db.execute("UPDATE events SET booked_seats=? WHERE hallID=?", (self.__booked_seats, hall_id))
            self.connect.commit()

            self.__booking_id = self.cursor_db.lastrowid
            self.__disconnect_db()

            return (self.__booking_id, cinema_title, self.__selected_movie, self.__selected_event,
                    self.__selected_seats)
        except Exception as e:
            print(f"Fehler beim Aktualisieren der Datenbank: {e}")
            return None
