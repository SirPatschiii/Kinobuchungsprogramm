from GUI import GUI
from Cinema import Cinema
from Movie import Movie
from Event import Event
from Booking import Booking


class Controller:
    def __init__(self):
        print("Controller works!")
        self.g_GUI = GUI()
        self.g_Cinema = Cinema()
        self.g_Movie = Movie()
        self.g_Event = Event()
        self.Booking = Booking()

        self.g_GUI.create_gui()
