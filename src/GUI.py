import sys
import tkinter as tk


global btn_exit
global btn_back

global btn_main_cinema

global btn_cinema_cinema1


class GUI:
    def __init__(self, p_controller):
        print("GUI works!")
        self.controller = p_controller
        self.window = tk.Tk()
        self.gui_status = "main"

    def create_gui(self):
        self.window.geometry("1000x700")
        self.window.resizable(False, False)
        self.window.title("Kinobuchungsprogramm")
        self.update_gui()
        self.window.mainloop()

    def update_gui(self):
        if self.gui_status == "main":
            self.__update_gui_main_menu()
        elif self.gui_status == "cinema":
            self.__update_gui_cinema_menu()
        elif self.gui_status == "movie":
            self.__update_gui_movie_menu()
        elif self.gui_status == "event":
            self.__update_gui_event_menu()
        elif self.gui_status == "booking":
            self.__update_gui_booking_menu()
        else:
            sys.exit(-1)

    def __update_gui_main_menu(self):
        global btn_cinema_cinema1

        try:
            btn_cinema_cinema1.destroy()
        except Exception as e:
            # Ignore exception
            pass

        global btn_main_cinema
        global btn_exit
        global btn_back

        btn_main_cinema = tk.Button(self.window, text="Kino", command=self.controller.change_gui_cinema, width=10, height=2)
        btn_main_cinema.place(x=450, y=325)
        btn_exit = tk.Button(self.window, text="Beenden", command=self.controller.exit, width=10, height=2)
        btn_exit.place(x=900, y=640)
        btn_back = tk.Button(self.window, text="Zurück", command=self.controller.back, width=10, height=2)
        btn_back.place(x=800, y=640)

    def __update_gui_cinema_menu(self):
        global btn_main_cinema

        try:
            btn_main_cinema.destroy()
        except Exception as e:
            # Ignore exception
            pass

        global btn_cinema_cinema1

        btn_cinema_cinema1 = tk.Button(self.window, text="Beispiel Kino 1", command=self.controller.change_cinema_movie, width=40, height=10)
        btn_cinema_cinema1.place(x=340, y=260)




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
