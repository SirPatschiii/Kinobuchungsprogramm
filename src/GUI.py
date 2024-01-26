import sys
import tkinter as tk


class GUI:
    def __init__(self):
        print("GUI works!")
        self.window = tk.Tk()
        self.gui_status = "main"

    def create_gui(self):
        self.window.geometry("1000x700")
        self.window.resizable(False, False)
        self.window.title("Kinobuchungsprogramm")
        self.update_gui("main")
        self.window.mainloop()

    def update_gui(self, gui_status):
        if gui_status == "main":
            self.__update_gui_main_menu()
        elif gui_status == "cinema":
            self.__update_gui_cinema_menu()
        elif gui_status == "movie":
            self.__update_gui_movie_menu()
        elif gui_status == "event":
            self.__update_gui_event_menu()
        elif gui_status == "booking":
            self.__update_gui_booking_menu()
        else:
            sys.exit(-1)

    def __update_gui_main_menu(self):
        btn = tk.Button(self.window, text="Test", command="", width=10, height=2)
        btn.place(x=50, y=50)

    def __update_gui_cinema_menu(self):
        pass

    def __update_gui_movie_menu(self):
        pass

    def __update_gui_event_menu(self):
        pass

    def __update_gui_booking_menu(self):
        pass

    def get_gui_status(self):
        return self.gui_status

    def set_gui_status(self, p_gui_status):
        self.gui_status = p_gui_status
        return
