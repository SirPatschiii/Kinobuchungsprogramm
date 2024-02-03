import sys
import tkinter as tk
import tkinter.constants

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
global txt_movie_txt1
global txt_movie_txt2
global txt_movie_txt3
global scb_movie_scb1
global scb_movie_scb2
global scb_movie_scb3
global fra_movie_fra1
global fra_movie_fra2
global fra_movie_fra3

global lbl_event_lab1
global rad_event_rad1
global rad_event_rad2
global rad_event_rad3
global btn_event_btn1
global radio_var
global event_lab1_var

global lbl_booking_lab1
global lbl_booking_lab2
global lbl_booking_lab3
global btn_booking_btn_list
global btn_booking_btn1


class GUI:
    def __init__(self, p_controller):
        print("GUI works!")
        self.__o_controller = p_controller
        self.__window = tk.Tk()
        self.__gui_status = "main"

        global btn_booking_btn_list
        btn_booking_btn_list = []

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

        global btn_main_cinema
        global btn_exit
        global btn_back

        btn_main_cinema = tk.Button(self.__window, text="Kinoauswahl", command=self.__o_controller.change_gui_cinema,
                                    width=40, height=10)
        btn_main_cinema.place(x=340, y=260)
        btn_exit = tk.Button(self.__window, text="Beenden", command=self.__o_controller.exit, width=10, height=2)
        btn_exit.place(x=900, y=640)
        btn_back = tk.Button(self.__window, text="Zurück", command=self.__o_controller.back, width=10, height=2)
        btn_back.place(x=800, y=640)

    def __update_gui_cinema_menu(self):
        self.__clear_gui()

        global btn_cinema_cinema1

        btn_cinema_cinema1 = tk.Button(self.__window, text=self.__o_controller.cinema_title(),
                                       command=lambda: self.__o_controller.change_cinema_movie(self.__o_controller.cinema_title()), width=40, height=10)
        btn_cinema_cinema1.place(x=340, y=260)

    def __update_gui_movie_menu(self):
        self.__clear_gui()

        global lbl_movie_lab1
        global lbl_movie_lab2
        global lbl_movie_lab3

        lbl_movie_lab1 = tk.Label(self.__window, text="1", font=("Arial", 20), width=10, height=10)
        lbl_movie_lab1.place(x=0, y=-50)
        lbl_movie_lab2 = tk.Label(self.__window, text="2", font=("Arial", 20), width=10, height=10)
        lbl_movie_lab2.place(x=0, y=175)
        lbl_movie_lab3 = tk.Label(self.__window, text="3", font=("Arial", 20), width=10, height=10)
        lbl_movie_lab3.place(x=0, y=400)

        global btn_movie_mov1
        global btn_movie_mov2
        global btn_movie_mov3

        movie_titles = self.__o_controller.movie_titles()
        btn_movie_mov1 = tk.Button(self.__window, text=movie_titles[0],
                                   command=lambda movie_title_lbl=movie_titles[0]: self.__o_controller.change_movie_event(
                                       movie_title_lbl), width=50, height=5)
        btn_movie_mov1.place(x=150, y=70)
        btn_movie_mov2 = tk.Button(self.__window, text=movie_titles[1],
                                   command=lambda movie_title_lbl=movie_titles[1]: self.__o_controller.change_movie_event(
                                       movie_title_lbl), width=50, height=5)
        btn_movie_mov2.place(x=150, y=290)
        btn_movie_mov3 = tk.Button(self.__window, text=movie_titles[2],
                                   command=lambda movie_title_lbl=movie_titles[2]: self.__o_controller.change_movie_event(
                                       movie_title_lbl), width=50, height=5)
        btn_movie_mov3.place(x=150, y=520)

        global txt_movie_txt1
        global txt_movie_txt2
        global txt_movie_txt3
        global scb_movie_scb1
        global scb_movie_scb2
        global scb_movie_scb3
        global fra_movie_fra1
        global fra_movie_fra2
        global fra_movie_fra3

        movie_descriptions = self.__o_controller.show_movie_description()

        fra_movie_fra1 = tk.Frame(self.__window, width=55, height=5)
        fra_movie_fra1.place(x=550, y=70)
        txt_movie_txt1 = tk.Text(fra_movie_fra1, width=50, height=5)
        scb_movie_scb1 = tk.Scrollbar(fra_movie_fra1)
        txt_movie_txt1.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.Y)
        scb_movie_scb1.pack(side=tkinter.constants.RIGHT, fill=tkinter.constants.Y)
        scb_movie_scb1.config(command=txt_movie_txt1.yview)
        txt_movie_txt1.config(yscrollcommand=scb_movie_scb1.set)
        txt_movie_txt1.insert(tkinter.END, movie_descriptions[0])
        txt_movie_txt1.config(state=tk.DISABLED)

        fra_movie_fra2 = tk.Frame(self.__window, width=55, height=5)
        fra_movie_fra2.place(x=550, y=290)
        txt_movie_txt2 = tk.Text(fra_movie_fra2, width=50, height=5)
        scb_movie_scb2 = tk.Scrollbar(fra_movie_fra2)
        txt_movie_txt2.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.Y)
        scb_movie_scb2.pack(side=tkinter.constants.RIGHT, fill=tkinter.constants.Y)
        scb_movie_scb2.config(command=txt_movie_txt2.yview)
        txt_movie_txt2.config(yscrollcommand=scb_movie_scb2.set)
        txt_movie_txt2.insert(tkinter.END, movie_descriptions[1])
        txt_movie_txt2.config(state=tk.DISABLED)

        fra_movie_fra3 = tk.Frame(self.__window, width=55, height=5)
        fra_movie_fra3.place(x=550, y=520)
        txt_movie_txt3 = tk.Text(fra_movie_fra3, width=50, height=5)
        scb_movie_scb3 = tk.Scrollbar(fra_movie_fra3)
        txt_movie_txt3.pack(side=tkinter.constants.LEFT, fill=tk.constants.Y)
        scb_movie_scb3.pack(side=tkinter.constants.LEFT, fill=tk.constants.Y)
        scb_movie_scb3.config(command=txt_movie_txt3.yview)
        txt_movie_txt3.config(yscrollcommand=scb_movie_scb3.set)
        txt_movie_txt3.insert(tkinter.END, movie_descriptions[2])
        txt_movie_txt3.config(state=tk.DISABLED)

    def __update_gui_event_menu(self):
        self.__clear_gui()

        global lbl_event_lab1
        global rad_event_rad1
        global rad_event_rad2
        global rad_event_rad3
        global btn_event_btn1
        global radio_var
        global event_lab1_var

        event_select = self.__o_controller.show_events()

        self.__radio_var = tk.StringVar(value=event_select[0])

        event_select = self.__o_controller.show_events()
        lbl_event_lab1 = tk.Label(self.__window, text=event_lab1_var, font=("Arial", 14), width=50, height=2, anchor="w")
        lbl_event_lab1.place(x=80, y=60)
        rad_event_rad1 = tk.Radiobutton(self.__window, text=event_select[0], variable=self.__radio_var,
                                        value=event_select[0], font=("Arial", 12))
        rad_event_rad2 = tk.Radiobutton(self.__window, text=event_select[1], variable=self.__radio_var,
                                        value=event_select[1], font=("Arial", 12))
        rad_event_rad3 = tk.Radiobutton(self.__window, text=event_select[2], variable=self.__radio_var,
                                        value=event_select[2], font=("Arial", 12))
        rad_event_rad1.select()
        rad_event_rad1.place(x=150, y=150)
        rad_event_rad2.place(x=150, y=200)
        rad_event_rad3.place(x=150, y=250)
        event_rad_selection = self.__radio_var.get()
        btn_event_btn1 = tk.Button(self.__window, text="Weiter", command=lambda: self.__o_controller.change_event_booking(event_rad_selection), width=10,
                                   height=2)
        # TODO Bug: selected_event was shown after go Back on the event selection and then forward to the seat selection
        btn_event_btn1.place(x=700, y=640)

    def __update_gui_booking_menu(self):
        self.__clear_gui()

        global lbl_booking_lab1
        global lbl_booking_lab2
        global lbl_booking_lab3
        global btn_booking_btn_list
        global btn_booking_btn1

        lbl_booking_lab1 = tk.Label(self.__window, text=self.__o_controller.get_selected_movie(), font=("Arial", 14), width=50, height=2, anchor="w")
        lbl_booking_lab1.place(x=80, y=60)
        lbl_booking_lab2 = tk.Label(self.__window, text=self.__o_controller.get_selected_cinema(), font=("Arial", 14), width=50, height=2, anchor="w")
        lbl_booking_lab2.place(x=80, y=110)
        lbl_booking_lab3 = tk.Label(self.__window, text=self.__o_controller.get_selected_event(), font=("Arial", 14), width=50, height=2,
                                    anchor="e")
        # TODO Bug: selected_event was shown after go Back on the event selection and then forward to the seat selection
        lbl_booking_lab3.place(x=350, y=60)

        for i in range(4):
            for j in range(5):
                button = tk.Button(self.__window, text=(i * 5) + (j + 1), font=("Arial", 14), width=7, height=2)
                button.place(x=250 + (100 * j), y=240 + (80 * i))
                btn_booking_btn_list.append(button)

        btn_booking_btn1 = tk.Button(self.__window, text="Buchen", command=self.__o_controller.change_booking_main,
                                     width=10, height=2)
        btn_booking_btn1.place(x=700, y=640)

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

        global btn_main_cinema

        global btn_cinema_cinema1

        global lbl_movie_lab1
        global lbl_movie_lab2
        global lbl_movie_lab3
        global btn_movie_mov1
        global btn_movie_mov2
        global btn_movie_mov3
        global txt_movie_txt1
        global txt_movie_txt2
        global txt_movie_txt3
        global scb_movie_scb1
        global scb_movie_scb2
        global scb_movie_scb3
        global fra_movie_fra1
        global fra_movie_fra2
        global fra_movie_fra3

        global lbl_event_lab1
        global rad_event_rad1
        global rad_event_rad2
        global rad_event_rad3
        global btn_event_btn1

        global lbl_booking_lab1
        global lbl_booking_lab2
        global lbl_booking_lab3
        global btn_booking_btn1

        try:
            btn_main_cinema.destroy()

            btn_cinema_cinema1.destroy()

            lbl_movie_lab1.destroy()
            lbl_movie_lab2.destroy()
            lbl_movie_lab3.destroy()
            btn_movie_mov1.destroy()
            btn_movie_mov2.destroy()
            btn_movie_mov3.destroy()
            txt_movie_txt1.destroy()
            txt_movie_txt2.destroy()
            txt_movie_txt3.destroy()
            scb_movie_scb1.destroy()
            scb_movie_scb2.destroy()
            scb_movie_scb3.destroy()
            fra_movie_fra1.destroy()
            fra_movie_fra2.destroy()
            fra_movie_fra3.destroy()

            lbl_event_lab1.destroy()
            rad_event_rad1.destroy()
            rad_event_rad2.destroy()
            rad_event_rad3.destroy()
            btn_event_btn1.destroy()

            lbl_booking_lab1.destroy()
            lbl_booking_lab2.destroy()
            lbl_booking_lab3.destroy()
            btn_booking_btn1.destroy()
        except:
            pass

        global btn_booking_btn_list

        for button in btn_booking_btn_list:
            try:
                button.destroy()
            except:
                pass

    def get_selected_radiobutton(self):
        return self.__radio_var.get()

    def get_gui_status(self):
        return self.__gui_status

    def set_gui_status(self, p_gui_status):
        self.__gui_status = p_gui_status
        return

    def set_event_lab1_var(self, p_event_lbl1_var):
        global event_lab1_var
        event_lab1_var = p_event_lbl1_var
        return
