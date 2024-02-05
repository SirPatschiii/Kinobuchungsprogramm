import sys
import logging as log
from pathlib import Path
import time
import tkinter as tk
import tkinter.constants


class GUI:
    def __init__(self, p_controller):
        self.__o_controller = p_controller

        if not log.root.handlers:
            __log_file = Path(__file__).resolve().parent / 'logfile.log'
            if __log_file.exists():
                __log_file.unlink()
                time.sleep(0.1)

            log.basicConfig(filename=__log_file, level=log.DEBUG)

        log.debug("GUI works!")

        self.__window = tk.Tk()
        self.__gui_status = "main"

        self.btn_exit = None
        self.btn_back = None

        self.btn_main_cinema = None

        self.btn_cinema_cinema1 = None

        self.lbl_movie_lab1 = None
        self.lbl_movie_lab2 = None
        self.lbl_movie_lab3 = None
        self.btn_movie_mov1 = None
        self.btn_movie_mov2 = None
        self.btn_movie_mov3 = None
        self.txt_movie_txt1 = None
        self.txt_movie_txt2 = None
        self.txt_movie_txt3 = None
        self.scb_movie_scb1 = None
        self.scb_movie_scb2 = None
        self.scb_movie_scb3 = None
        self.fra_movie_fra1 = None
        self.fra_movie_fra2 = None
        self.fra_movie_fra3 = None

        self.lbl_event_lab1 = None
        self.rad_event_rad1 = None
        self.rad_event_rad2 = None
        self.rad_event_rad3 = None
        self.btn_event_btn1 = None
        self.radio_var = None
        self.event_lab1_var = None

        self.lbl_booking_lab1 = None
        self.lbl_booking_lab2 = None
        self.lbl_booking_lab3 = None
        self.btn_booking_btn_list = []
        self.btn_booking_btn1 = None

    def create_gui(self):
        self.__window.geometry("1000x700")
        self.__window.resizable(False, False)
        self.__window.title("Kinobuchungsprogramm")
        self.update_gui()
        self.__window.mainloop()

    def update_gui(self):
        if self.__gui_status == "main":
            self.__update_gui_main_menu()
        elif self.__gui_status == "cinema":
            self.__update_gui_cinema_menu()
        elif self.__gui_status == "movie":
            self.__update_gui_movie_menu()
        elif self.__gui_status == "event":
            self.__update_gui_event_menu()
        elif self.__gui_status == "booking":
            self.__update_gui_booking_menu()
        else:
            sys.exit(-1)

    def __update_gui_main_menu(self):
        self.__clear_gui()

        self.btn_main_cinema = tk.Button(self.__window, text="Kinoauswahl",
                                         command=self.__o_controller.change_gui_cinema, width=40, height=10)
        self.btn_main_cinema.place(x=340, y=260)
        self.btn_exit = tk.Button(self.__window, text="Beenden", command=self.__o_controller.exit, width=10, height=2)
        self.btn_exit.place(x=900, y=640)
        self.btn_back = tk.Button(self.__window, text="Zurück", command=self.__o_controller.back, width=10, height=2)
        self.btn_back.place(x=800, y=640)

    def __update_gui_cinema_menu(self):
        self.__clear_gui()

        self.btn_cinema_cinema1 = tk.Button(self.__window, text=self.__o_controller.cinema_title(),
                                            command=lambda: self.__o_controller.change_cinema_movie(
                                                self.__o_controller.cinema_title()), width=40, height=10)
        self.btn_cinema_cinema1.place(x=340, y=260)

    def __update_gui_movie_menu(self):
        self.__clear_gui()

        self.lbl_movie_lab1 = tk.Label(self.__window, text="1", font=("Arial", 20), width=10, height=10)
        self.lbl_movie_lab1.place(x=0, y=-50)
        self.lbl_movie_lab2 = tk.Label(self.__window, text="2", font=("Arial", 20), width=10, height=10)
        self.lbl_movie_lab2.place(x=0, y=175)
        self.lbl_movie_lab3 = tk.Label(self.__window, text="3", font=("Arial", 20), width=10, height=10)
        self.lbl_movie_lab3.place(x=0, y=400)

        self.movie_titles = self.__o_controller.movie_titles()

        self.btn_movie_mov1 = tk.Button(self.__window, text=self.movie_titles[0], command=lambda
                                        movie_title_lbl=self.movie_titles[0]: self.__o_controller.change_movie_event(
                                        movie_title_lbl), width=50, height=5)
        self.btn_movie_mov1.place(x=150, y=70)
        self.btn_movie_mov2 = tk.Button(self.__window, text=self.movie_titles[1], command=lambda
                                        movie_title_lbl=self.movie_titles[1]: self.__o_controller.change_movie_event(
                                        movie_title_lbl), width=50, height=5)
        self.btn_movie_mov2.place(x=150, y=290)
        self.btn_movie_mov3 = tk.Button(self.__window, text=self.movie_titles[2], command=lambda
                                        movie_title_lbl=self.movie_titles[2]: self.__o_controller.change_movie_event(
                                        movie_title_lbl), width=50, height=5)
        self.btn_movie_mov3.place(x=150, y=520)

        self.movie_descriptions = self.__o_controller.show_movie_description()

        self.fra_movie_fra1 = tk.Frame(self.__window, width=55, height=5)
        self.fra_movie_fra1.place(x=550, y=70)
        self.txt_movie_txt1 = tk.Text(self.fra_movie_fra1, width=50, height=5)
        self.scb_movie_scb1 = tk.Scrollbar(self.fra_movie_fra1)
        self.txt_movie_txt1.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.Y)
        self.scb_movie_scb1.pack(side=tkinter.constants.RIGHT, fill=tkinter.constants.Y)
        self.scb_movie_scb1.config(command=self.txt_movie_txt1.yview)
        self.txt_movie_txt1.config(yscrollcommand=self.scb_movie_scb1.set)
        self.txt_movie_txt1.insert(tkinter.END, self.movie_descriptions[0])
        self.txt_movie_txt1.config(state=tk.DISABLED)

        self.fra_movie_fra2 = tk.Frame(self.__window, width=55, height=5)
        self.fra_movie_fra2.place(x=550, y=290)
        self.txt_movie_txt2 = tk.Text(self.fra_movie_fra2, width=50, height=5)
        self.scb_movie_scb2 = tk.Scrollbar(self.fra_movie_fra2)
        self.txt_movie_txt2.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.Y)
        self.scb_movie_scb2.pack(side=tkinter.constants.RIGHT, fill=tkinter.constants.Y)
        self.scb_movie_scb2.config(command=self.txt_movie_txt2.yview)
        self.txt_movie_txt2.config(yscrollcommand=self.scb_movie_scb2.set)
        self.txt_movie_txt2.insert(tkinter.END, self.movie_descriptions[1])
        self.txt_movie_txt2.config(state=tk.DISABLED)

        self.fra_movie_fra3 = tk.Frame(self.__window, width=55, height=5)
        self.fra_movie_fra3.place(x=550, y=520)
        self.txt_movie_txt3 = tk.Text(self.fra_movie_fra3, width=50, height=5)
        self.scb_movie_scb3 = tk.Scrollbar(self.fra_movie_fra3)
        self.txt_movie_txt3.pack(side=tkinter.constants.LEFT, fill=tk.constants.Y)
        self.scb_movie_scb3.pack(side=tkinter.constants.LEFT, fill=tk.constants.Y)
        self.scb_movie_scb3.config(command=self.txt_movie_txt3.yview)
        self.txt_movie_txt3.config(yscrollcommand=self.scb_movie_scb3.set)
        self.txt_movie_txt3.insert(tkinter.END, self.movie_descriptions[2])
        self.txt_movie_txt3.config(state=tk.DISABLED)

    def __update_gui_event_menu(self):
        self.__clear_gui()

        self.event_select = self.__o_controller.show_events()

        self.__radio_var = tk.StringVar(value=self.event_select[0])

        self.event_select = self.__o_controller.show_events()
        self.lbl_event_lab1 = tk.Label(self.__window, text=self.event_lab1_var, font=("Arial", 14), width=50, height=2,
                                       anchor="w")
        self.lbl_event_lab1.place(x=80, y=60)
        self.rad_event_rad1 = tk.Radiobutton(self.__window, text=self.event_select[0], variable=self.__radio_var,
                                             value=self.event_select[0], font=("Arial", 12))
        self.rad_event_rad2 = tk.Radiobutton(self.__window, text=self.event_select[1], variable=self.__radio_var,
                                             value=self.event_select[1], font=("Arial", 12))
        self.rad_event_rad3 = tk.Radiobutton(self.__window, text=self.event_select[2], variable=self.__radio_var,
                                             value=self.event_select[2], font=("Arial", 12))
        self.rad_event_rad1.select()
        self.rad_event_rad1.place(x=150, y=150)
        self.rad_event_rad2.place(x=150, y=200)
        self.rad_event_rad3.place(x=150, y=250)
        self.event_rad_selection = self.__radio_var.get()
        self.btn_event_btn1 = tk.Button(self.__window, text="Weiter",
                                        command=lambda: self.__o_controller.change_event_booking(
                                            self.event_rad_selection), width=10, height=2)
        # TODO Bug: selected_event was shown after go Back on the event selection and then forward to the seat
        #  selection.
        #  The algorithm is ignoring the choice of the user, in booking it will always display the first event time WIP
        self.btn_event_btn1.place(x=700, y=640)

    def __update_gui_booking_menu(self):
        self.__clear_gui()

        self.lbl_booking_lab1 = tk.Label(self.__window, text=self.__o_controller.get_selected_movie(),
                                         font=("Arial", 14), width=50, height=2, anchor="w")
        self.lbl_booking_lab1.place(x=80, y=60)
        self.lbl_booking_lab2 = tk.Label(self.__window, text=self.__o_controller.get_selected_cinema(),
                                         font=("Arial", 14), width=50, height=2, anchor="w")
        self.lbl_booking_lab2.place(x=80, y=110)
        self.lbl_booking_lab3 = tk.Label(self.__window, text=self.__o_controller.get_selected_event(),
                                         font=("Arial", 14), width=50, height=2, anchor="e")
        # TODO Bug: selected_event was shown after go Back on the event selection and then forward to the seat
        #  selection.
        #  The algorithm is ignoring the choice of the user, in booking it will always display the first event time WIP
        self.lbl_booking_lab3.place(x=350, y=60)

        for i in range(4):
            for j in range(5):
                button = tk.Button(self.__window, text=(i * 5) + (j + 1), font=("Arial", 14), width=7, height=2)
                button.place(x=250 + (100 * j), y=240 + (80 * i))
                self.btn_booking_btn_list.append(button)

        self.btn_booking_btn1 = tk.Button(self.__window, text="Buchen", command=self.__o_controller.change_booking_main,
                                          width=10, height=2)
        self.btn_booking_btn1.place(x=700, y=640)

    def booking_pop_up(self):
        pop_up = tk.Tk()
        pop_up.geometry("400x400")
        pop_up.resizable(False, False)
        pop_up.title("Buchungszusammenfassung")

        btn_p_exit = tk.Button(pop_up, text="Exit", command=pop_up.destroy, width=10, height=2)
        btn_p_exit.place(x=160, y=350)

        pop_up.mainloop()

    def __clear_gui(self):
        # This method destroys all elements on the current GUI to ensure only the correct widgets for the current
        # GUI state get displayed

        try:
            self.btn_main_cinema.destroy()

            self.btn_cinema_cinema1.destroy()

            self.lbl_movie_lab1.destroy()
            self.lbl_movie_lab2.destroy()
            self.lbl_movie_lab3.destroy()
            self.btn_movie_mov1.destroy()
            self.btn_movie_mov2.destroy()
            self.btn_movie_mov3.destroy()
            self.txt_movie_txt1.destroy()
            self.txt_movie_txt2.destroy()
            self.txt_movie_txt3.destroy()
            self.scb_movie_scb1.destroy()
            self.scb_movie_scb2.destroy()
            self.scb_movie_scb3.destroy()
            self.fra_movie_fra1.destroy()
            self.fra_movie_fra2.destroy()
            self.fra_movie_fra3.destroy()

            self.lbl_event_lab1.destroy()
            self.rad_event_rad1.destroy()
            self.rad_event_rad2.destroy()
            self.rad_event_rad3.destroy()
            self.btn_event_btn1.destroy()

            self.lbl_booking_lab1.destroy()
            self.lbl_booking_lab2.destroy()
            self.lbl_booking_lab3.destroy()
            self.btn_booking_btn1.destroy()
        except AttributeError as e:
            log.exception(f"AttributeError: {e}")
        except tk.TclError as e:
            log.exception(f"Error while destroying widgets: {e}")

        for button in self.btn_booking_btn_list:
            try:
                button.destroy()
            except AttributeError as e:
                log.exception(f"AttributeError: {e}")
            except tk.TclError as e:
                log.exception(f"Error while destroying widgets: {e}")

    def get_selected_radiobutton(self):
        return self.__radio_var.get()

    def get_gui_status(self):
        return self.__gui_status

    def set_gui_status(self, p_gui_status):
        self.__gui_status = p_gui_status
        return

    def set_event_lab1_var(self, p_event_lbl1_var):
        self.event_lab1_var = p_event_lbl1_var
        return
