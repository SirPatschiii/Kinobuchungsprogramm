import logging


class Booking:
    def __init__(self):
        logging.debug("Booking works!")

        self.__selected_cinema = ""
        self.__selected_movie = ""
        self.__selected_event = ""

    def set_selected_cinema(self, cinema_title):
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
        print(self.__selected_event)
        return self.__selected_event
