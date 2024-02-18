import logging as log
import sqlite3
import os


class Booking:
    def __init__(self):

        log.debug("Booking works!")

        self.__cursor_db = None
        self.__connect = None

        self.__selected_cinema = ""
        self.__selected_movie = None
        self.__selected_event = ""
        self.__booked_seats = ""
        self.__booking_id = None
        self.__selected_seats = None

    def __connect_db(self):
        # This method creates the connection to the database
        # Therefor the absolute path is determined to secure the connection is successful
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
        # close the connection to the database
        self.__connect.close()

    def set_selected_cinema(self, cinema_title, hall_id):
        # get the selected_cinema from the controller
        self.__selected_cinema = cinema_title

    def get_selected_cinema(self):
        # output the selected_cinema from set_selected_cinema
        return self.__selected_cinema

    def set_selected_movie(self, movie_title_lbl):
        # get the selected movie_title from the controller
        self.__selected_movie = movie_title_lbl

    def get_selected_movie(self):
        # output the selected_movie from set_selected_movie
        return self.__selected_movie

    def set_selected_event(self, event_rad_selection):
        # get the event_rad_selection from the controller
        self.__selected_event = event_rad_selection

    def get_selected_event(self):
        # output the selected_event from set_selected_event
        return self.__selected_event

    def set_booked_seats(self, seat_list):
        # get the booked_seats from the controller
        self.__booked_seats = seat_list

    def get_booked_seats(self):
        # output the booked_seats from set_booked_seats
        return self.__booked_seats

    def set_selected_seats(self, selected_seats):
        # get the selected_seats from the controller
        self.__selected_seats = selected_seats

    def get_selected_seats(self):
        # output the selected_seats from set_selected_seats
        return self.__selected_seats

    def update_database(self):
        try:
            self.__connect_db()
            # seperated the selected_seats list into individual seats
            selected_seats_str = ', '.join(str(seat) for seat in self.__selected_seats)

            # give not a return, if the selected_seats list is empty
            if selected_seats_str == '':
                return None
            cinema_title = self.__selected_cinema if self.__selected_cinema else ""

            # call the matching hall_id with the cinema_title from the database
            self.__cursor_db.execute("""
                SELECT hallID 
                FROM cinema 
                WHERE name=?""", (cinema_title,))
            hall_id = self.__cursor_db.fetchone()[0]

            # call the matching movie_id with the name of the selected_movie from the database
            self.__cursor_db.execute("""
                SELECT movieID 
                FROM movie 
                WHERE name=?""", (self.__selected_movie,))

            movie_id = self.__cursor_db.fetchone()[0]

            # call the matching event_id with the selected_event and the hall_id from the database
            self.__cursor_db.execute("""
                SELECT eventID 
                FROM events 
                WHERE date=? AND hallID=?""", (self.__selected_event, hall_id,))
            event_id = self.__cursor_db.fetchone()[0]

            # write the hall_id, movie_id, event_id, selected_seats_str together as a new record into the database
            self.__cursor_db.execute(
                "INSERT INTO bookings (hallID, movieID, eventID, selected_seats) VALUES (?, ?, ?, ?)",
                (hall_id, movie_id, event_id, selected_seats_str))
            self.__connect.commit()

            # updated the record of the booked_seats in the database
            self.__cursor_db.execute("""
                UPDATE events 
                SET booked_seats=? 
                WHERE eventID=? AND hallID=? AND movieID=?  """, (self.__booked_seats, event_id, hall_id, movie_id))
            self.__connect.commit()

            # call the booking_id of the last record of the database
            self.__booking_id = self.__cursor_db.lastrowid
            self.__disconnect_db()

            # output from the database written data
            return (self.__booking_id, cinema_title, self.__selected_movie, self.__selected_event,
                    self.__selected_seats)
        except Exception as e:
            print(f"Fehler beim Aktualisieren der Datenbank: {e}")
            return None
