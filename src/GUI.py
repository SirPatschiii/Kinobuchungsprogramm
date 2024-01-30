import sys
import tkinter as tk

global btn_exit
global btn_back

global btn_main_cinema

global btn_cinema_cinema1

global lbl_movie_lab1
global lbl_movie_lab2
global lbl_movie_lab3
global btn_movie_mov1
global btn_movie_mov2
global btn_movie_mov3

global lbl_event_lab1
global rad_event_rad1
global rad_event_rad2
global rad_event_rad3
global btn_event_btn1
global radio_var
global event_lbl1_var


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
        except Exception:
            # Ignore exception
            pass

        global btn_main_cinema
        global btn_exit
        global btn_back

        btn_main_cinema = tk.Button(self.window, text="Kinoauswahl", command=self.controller.change_gui_cinema,
                                    width=40, height=10)
        btn_main_cinema.place(x=340, y=260)
        btn_exit = tk.Button(self.window, text="Beenden", command=self.controller.exit, width=10, height=2)
        btn_exit.place(x=900, y=640)
        btn_back = tk.Button(self.window, text="Zurück", command=self.controller.back, width=10, height=2)
        btn_back.place(x=800, y=640)

    def __update_gui_cinema_menu(self):
        global btn_main_cinema
        global lbl_movie_lab1
        global lbl_movie_lab2
        global lbl_movie_lab3
        global btn_movie_mov1
        global btn_movie_mov2
        global btn_movie_mov3

        try:
            btn_main_cinema.destroy()
            lbl_movie_lab1.destroy()
            lbl_movie_lab2.destroy()
            lbl_movie_lab3.destroy()
            btn_movie_mov1.destroy()
            btn_movie_mov2.destroy()
            btn_movie_mov3.destroy()
        except Exception:
            # Ignore exception
            pass

        global btn_cinema_cinema1

        btn_cinema_cinema1 = tk.Button(self.window, text=self.controller.cinema_title(),
                                       command=self.controller.change_cinema_movie, width=40, height=10)
        btn_cinema_cinema1.place(x=340, y=260)

    def __update_gui_movie_menu(self):
        global btn_cinema_cinema1
        global lbl_event_lab1
        global rad_event_rad1
        global rad_event_rad2
        global rad_event_rad3
        global btn_event_btn1

        try:
            btn_cinema_cinema1.destroy()
            lbl_event_lab1.destroy()
            rad_event_rad1.destroy()
            rad_event_rad2.destroy()
            rad_event_rad3.destroy()
            btn_event_btn1.destroy()
        except Exception:
            # Ignore exception
            pass

        global lbl_movie_lab1
        global lbl_movie_lab2
        global lbl_movie_lab3

        lbl_movie_lab1 = tk.Label(self.window, text="1", font=("Arial", 20), width=10, height=10)
        lbl_movie_lab1.place(x=0, y=-50)
        lbl_movie_lab2 = tk.Label(self.window, text="2", font=("Arial", 20), width=10, height=10)
        lbl_movie_lab2.place(x=0, y=175)
        lbl_movie_lab3 = tk.Label(self.window, text="3", font=("Arial", 20), width=10, height=10)
        lbl_movie_lab3.place(x=0, y=400)

        global btn_movie_mov1
        global btn_movie_mov2
        global btn_movie_mov3
        movie_titles = self.controller.movie_titles()
        btn_movie_mov1 = tk.Button(self.window, text=movie_titles[0],
                                   command=lambda movie_title_lbl=movie_titles[0]: self.controller.change_movie_event(
                                       movie_title_lbl),
                                   width=60, height=5)
        btn_movie_mov1.place(x=150, y=70)
        btn_movie_mov2 = tk.Button(self.window, text=movie_titles[1],
                                   command=lambda movie_title_lbl=movie_titles[1]: self.controller.change_movie_event(
                                       movie_title_lbl),
                                   width=60, height=5)
        btn_movie_mov2.place(x=150, y=290)
        btn_movie_mov3 = tk.Button(self.window, text=movie_titles[2],
                                   command=lambda movie_title_lbl=movie_titles[2]: self.controller.change_movie_event(
                                       movie_title_lbl),
                                   width=60, height=5)
        btn_movie_mov3.place(x=150, y=520)

    def __update_gui_event_menu(self):
        global lbl_movie_lab1
        global lbl_movie_lab2
        global lbl_movie_lab3
        global btn_movie_mov1
        global btn_movie_mov2
        global btn_movie_mov3

        try:
            lbl_movie_lab1.destroy()
            lbl_movie_lab2.destroy()
            lbl_movie_lab3.destroy()
            btn_movie_mov1.destroy()
            btn_movie_mov2.destroy()
            btn_movie_mov3.destroy()
        except Exception:
            # Ignore exception
            pass

        global lbl_event_lab1
        global rad_event_rad1
        global rad_event_rad2
        global rad_event_rad3
        global btn_event_btn1
        global radio_var
        global event_lbl1_var

        self.radio_var = tk.StringVar(value="Option 1")
        event_select = self.controller.show_events()
        lbl_event_lab1 = tk.Label(self.window, text=event_lbl1_var, font=("Arial", 14), width=10, height=2)
        lbl_event_lab1.place(x=80, y=80)
        rad_event_rad1 = tk.Radiobutton(self.window, text=event_select[0], variable=self.radio_var,
                                        value="Option 1")
        rad_event_rad2 = tk.Radiobutton(self.window, text=event_select[1], variable=self.radio_var,
                                        value="option 2")
        rad_event_rad3 = tk.Radiobutton(self.window, text=event_select[2], variable=self.radio_var,
                                        value="Option 3")
        rad_event_rad1.select()
        rad_event_rad1.place(x=300, y=100)
        rad_event_rad2.place(x=300, y=150)
        rad_event_rad3.place(x=300, y=200)
        btn_event_btn1 = tk.Button(self.window, text="Weiter", command=self.controller.change_event_booking, width=10,
                                   height=2)
        btn_event_btn1.place(x=700, y=640)

    def __update_gui_booking_menu(self):
        global lbl_event_lab1
        global rad_event_rad1
        global rad_event_rad2
        global rad_event_rad3
        global btn_event_btn1
        try:
            lbl_event_lab1.destroy()
            rad_event_rad1.destroy()
            rad_event_rad2.destroy()
            rad_event_rad3.destroy()
            btn_event_btn1.destroy()
        except Exception:
            # Ignore exception
            pass

    def get_selected_radiobutton(self):
        return self.radio_var.get()

    def get_gui_status(self):
        return self.gui_status

    def set_gui_status(self, p_gui_status):
        self.gui_status = p_gui_status
        return

    def set_event_lbl1_var(self, p_event_lbl1_var):
        global event_lbl1_var
        event_lbl1_var = p_event_lbl1_var
