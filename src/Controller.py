from GUI import GUI
from Button import Button
from Entry import Entry
from Label import Label
from Spinbox import Spinbox
from Radiobox import Radiobox


class Controller:
    def __init__(self):
        print("Controller works!")
        self.g_GUI = GUI()
        self.g_Button = Button()
        self.g_Entry = Entry()
        self.g_Label = Label()
        self.g_Spinbox = Spinbox()
        self.g_Radiobox = Radiobox()
