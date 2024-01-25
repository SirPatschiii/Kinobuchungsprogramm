from GUI import GUI
from Button import Button
from Entry import Entry
from Label import Label
from Spinbox import Spinbox
from Radiobox import Radiobox
from Cinema import Cinema
from Movie import Movie
from Event import Event
from Booking import Booking


class Controller:
    def __init__(self):
        print("Controller works!")
        self.g_GUI = GUI()
        self.g_Button = Button(self.g_GUI.get_window())
        self.g_Entry = Entry()
        self.g_Label = Label()
        self.g_Spinbox = Spinbox()
        self.g_Radiobox = Radiobox()
        self.g_Cinema = Cinema()
        self.g_Movie = Movie()
        self.g_Event = Event()
        self.Booking = Booking()

        self.g_GUI.create_gui()
