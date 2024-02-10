import sys
import logging as log

from GUI import GUI
from Cinema import Cinema
from Movie import Movie
from Event import Event
from Booking import Booking


class Controller:
    def __init__(self):
        self.__o_gui = GUI(self)
        self.__o_cinema = Cinema()
        self.__o_movie = Movie()
        self.__o_event = Event()
        self.__o_booking = Booking()

        log.debug("Controller works!")

        self.__o_gui.create_gui()

    def change_gui_cinema(self):
        self.__o_cinema.get_all_cinemas()
        self.__o_gui.set_gui_status("cinema")
        self.__o_gui.update_gui()

    def change_cinema_movie(self):
        self.__o_gui.set_gui_status("movie")
        self.__o_gui.update_gui()

    def change_movie_event(self, movie_title_lbl):
        self.__o_gui.set_event_lab1_var(movie_title_lbl)
        self.__o_event.set_selected_movie(movie_title_lbl)
        self.__o_gui.set_gui_status("event")
        self.__o_gui.update_gui()
        self.__o_cinema.set_selected_movie(movie_title_lbl)
        self.__o_booking.set_selected_movie(movie_title_lbl)



    def change_event_booking(self):
        self.__o_gui.set_gui_status("booking")
        self.__o_gui.set_booked_seats(self.__o_cinema.get_booked_seats())
        self.__o_gui.update_gui()

    def change_booking_main(self):
        self.__o_gui.set_gui_status("main")
        self.__o_gui.update_gui()

    def back(self):
        match self.__o_gui.get_gui_status():
            case "main":
                self.__o_gui.set_gui_status("main")
                self.__o_gui.update_gui()
            case "cinema":
                self.__o_gui.set_gui_status("main")
                self.__o_gui.update_gui()
            case "movie":
                self.__o_gui.set_gui_status("cinema")
                self.__o_gui.update_gui()
            case "event":
                self.__o_gui.set_gui_status("movie")
                self.__o_gui.update_gui()
            case "booking":
                self.__o_gui.set_gui_status("event")
                self.__o_gui.update_gui()

    def get_all_cinemas(self):
        return self.__o_cinema.get_all_cinemas()

    def movie_titles(self):
        movies = self.__o_movie.get_movie_title()
        return movies

    def show_events(self):
        events = self.__o_event.get_event_title()
        event_titles = [event for event in events]  # Extracting titles from the fetched events
        return event_titles

    def set_selected_cinema(self, cinema_title, hall_id):
        self.__o_booking.set_selected_cinema(cinema_title, hall_id)
        self.__o_movie.set_selected_cinema(hall_id)
        self.__o_event.set_selected_cinema(hall_id)
        self.__o_cinema.set_selected_cinema(hall_id)

    def set_selected_event(self, p_selected_event):
        self.__o_booking.set_selected_event(p_selected_event)
        self.__o_cinema.set_selected_event(p_selected_event)

    def set_seat_state(self, p_index):
        booked_seats = self.__o_gui.get_booked_seats()
        if not booked_seats[p_index - 1]:
            booked_seats[p_index - 1] = True
        self.__o_gui.set_booked_seats(booked_seats)
        self.__o_gui.update_gui()

    def show_movie_description(self):
        movie_descriptions = self.__o_movie.movie_description()
        return movie_descriptions

    def get_selected_cinema(self):
        return self.__o_booking.get_selected_cinema()

    def get_selected_movie(self):
        return self.__o_booking.get_selected_movie()

    def get_selected_event(self):
        return self.__o_booking.get_selected_event()

    def get_total_seats(self):
        return self.__o_cinema.get_total_seats()

    def get_booked_seats(self):
        return self.__o_cinema.get_booked_seats()

    def book_seats(self, seat_list, selected_seats):
        self.__o_booking.set_booked_seats(seat_list)
        self.__o_booking.set_selected_seats(selected_seats)
        # self.__o_booking.update_database()
        self.change_booking_main()
        self.__o_gui.update_gui()
        booking_data = self.__o_booking.update_database()
        if booking_data:
            self.__o_gui.booking_pop_up(*booking_data)
        self.__o_gui.update_gui()

    def exit(self):
        sys.exit(1)
