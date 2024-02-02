import sys

from GUI import GUI
from Cinema import Cinema
from Movie import Movie
from Event import Event
from Booking import Booking


class Controller:
    def __init__(self):
        print("Controller works!")
        self.g_GUI = GUI(self)
        self.g_Cinema = Cinema()
        self.g_Movie = Movie()
        self.g_Event = Event()
        self.Booking = Booking()

        self.g_GUI.create_gui()

    def change_gui_cinema(self):
        self.g_GUI.set_gui_status("cinema")
        self.g_GUI.update_gui()

    def change_cinema_movie(self):
        self.g_GUI.set_gui_status("movie")
        self.g_GUI.update_gui()

    def change_movie_event(self, movie_title_lbl):
        self.g_GUI.set_event_lab1_var(movie_title_lbl)
        self.g_GUI.set_gui_status("event")
        self.g_GUI.update_gui()

    def change_event_booking(self):
        self.g_GUI.set_gui_status("booking")
        self.g_GUI.update_gui()

    def change_booking_main(self):
        self.g_GUI.set_gui_status("main")
        self.g_GUI.update_gui()
        self.g_GUI.booking_pop_up()

    def back(self):
        match self.g_GUI.get_gui_status():
            case "main":
                self.g_GUI.set_gui_status("main")
                self.g_GUI.update_gui()
            case "cinema":
                self.g_GUI.set_gui_status("main")
                self.g_GUI.update_gui()
            case "movie":
                self.g_GUI.set_gui_status("cinema")
                self.g_GUI.update_gui()
            case "event":
                self.g_GUI.set_gui_status("movie")
                self.g_GUI.update_gui()
            case "booking":
                self.g_GUI.set_gui_status("event")
                self.g_GUI.update_gui()

    def cinema_title(self):
        self.g_Cinema.connect_db()
        return self.g_Cinema.title()

    def movie_titles(self):
        movie_ids = ['1', '2', '3']
        titles = []
        self.g_Movie.connect_db()
        for movie_id in movie_ids:
            title = self.g_Movie.title(movie_id)
            titles.append(title)
        return titles

    def show_events(self):
        event_ids = ['1', '2', '3']
        event_list = []
        self.g_Event.connect_db()
        for event_id in event_ids:
            events = self.g_Event.title(event_id)
            event_list.append(events)
        return event_list

    def show_movie_description(self):
        movie_ids = ['1', '2', '3']
        descriptions = []
        self.g_Movie.connect_db()
        for movie_id in movie_ids:
            description = self.g_Movie.movie_description(movie_id)
            descriptions.append(description)
        return descriptions

    def exit(self):
        sys.exit(1)
