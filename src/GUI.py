import sys
import logging as log
from pathlib import Path
import time
import tkinter as tk
import tkinter.constants
import tkinter.messagebox as tk_msg_box


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

        self.__btn_exit = None
        self.__btn_back = None

        self.__btn_main_cinema = None

        self.__btn_cinema_cinema1 = None

        self.__lbl_movie_lab1 = None
        self.__lbl_movie_lab2 = None
        self.__lbl_movie_lab3 = None
        self.__btn_movie_mov1 = None
        self.__btn_movie_mov2 = None
        self.__btn_movie_mov3 = None
        self.__txt_movie_txt1 = None
        self.__txt_movie_txt2 = None
        self.__txt_movie_txt3 = None
        self.__scb_movie_scb1 = None
        self.__scb_movie_scb2 = None
        self.__scb_movie_scb3 = None
        self.__fra_movie_fra1 = None
        self.__fra_movie_fra2 = None
        self.__fra_movie_fra3 = None

        self.__lbl_event_lab1 = None
        self.__rad_event_rad1 = None
        self.__rad_event_rad2 = None
        self.__rad_event_rad3 = None
        self.__btn_event_btn1 = None
        self.__event_lab1_var = None

        self.__lbl_booking_lab1 = None
        self.__lbl_booking_lab2 = None
        self.__lbl_booking_lab3 = None
        self.__btn_booking_btn_list = []
        self.__booked_seats = None
        self.__btn_booking_btn1 = None
        self.__selected_seats = set()
        self.__selected_cinema_title = None
        self.__selected_hall_id = None
        self.__cinema_buttons = []

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

        self.__btn_main_cinema = tk.Button(self.__window, text="Kinoauswahl",
                                           command=self.__o_controller.change_gui_cinema, width=40, height=10)
        self.__btn_main_cinema.place(x=340, y=260)
        self.__btn_exit = tk.Button(self.__window, text="Beenden", command=self.__o_controller.exit, width=10, height=2)
        self.__btn_exit.place(x=900, y=640)
        self.__btn_back = tk.Button(self.__window, text="Zurück", command=self.__o_controller.back, width=10, height=2)
        self.__btn_back.place(x=800, y=640)

    def __update_gui_cinema_menu(self):
        self.__clear_gui()

        cinemas = self.__o_controller.get_all_cinemas()
        x_position = 335
        y_position = 165
        for hall_id, cinema_title in cinemas:
            btn_cinema = tk.Button(self.__window, text=cinema_title,
                                   command=lambda hid=hall_id, title=cinema_title: self.select_cinema(hid, title),
                                   width=40, height=10)
            btn_cinema.place(x=x_position, y=y_position)
            self.__cinema_buttons.append(btn_cinema)
            y_position += 180

    def __update_gui_movie_menu(self):
        self.__clear_gui()

        self.__lbl_movie_lab1 = tk.Label(self.__window, text="1", font=("Arial", 20), width=10, height=10)
        self.__lbl_movie_lab1.place(x=0, y=-50)
        self.__lbl_movie_lab2 = tk.Label(self.__window, text="2", font=("Arial", 20), width=10, height=10)
        self.__lbl_movie_lab2.place(x=0, y=175)
        self.__lbl_movie_lab3 = tk.Label(self.__window, text="3", font=("Arial", 20), width=10, height=10)
        self.__lbl_movie_lab3.place(x=0, y=400)

        self.movie_titles = self.__o_controller.movie_titles()

        self.__btn_movie_mov1 = tk.Button(self.__window, text=self.movie_titles[0], command=lambda
                                        movie_title_lbl=self.movie_titles[0]: self.__o_controller.change_movie_event(
                                        movie_title_lbl), width=50, height=5)
        self.__btn_movie_mov1.place(x=150, y=70)
        self.__btn_movie_mov2 = tk.Button(self.__window, text=self.movie_titles[1], command=lambda
                                        movie_title_lbl=self.movie_titles[1]: self.__o_controller.change_movie_event(
                                        movie_title_lbl), width=50, height=5)
        self.__btn_movie_mov2.place(x=150, y=290)
        self.__btn_movie_mov3 = tk.Button(self.__window, text=self.movie_titles[2], command=lambda
                                        movie_title_lbl=self.movie_titles[2]: self.__o_controller.change_movie_event(
                                        movie_title_lbl), width=50, height=5)
        self.__btn_movie_mov3.place(x=150, y=520)

        self.movie_descriptions = self.__o_controller.show_movie_description()

        self.__fra_movie_fra1 = tk.Frame(self.__window, width=55, height=5)
        self.__fra_movie_fra1.place(x=550, y=70)
        self.__txt_movie_txt1 = tk.Text(self.__fra_movie_fra1, width=50, height=5)
        self.__scb_movie_scb1 = tk.Scrollbar(self.__fra_movie_fra1)
        self.__txt_movie_txt1.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.Y)
        self.__scb_movie_scb1.pack(side=tkinter.constants.RIGHT, fill=tkinter.constants.Y)
        self.__scb_movie_scb1.config(command=self.__txt_movie_txt1.yview)
        self.__txt_movie_txt1.config(yscrollcommand=self.__scb_movie_scb1.set)
        self.__txt_movie_txt1.insert(tkinter.END, self.movie_descriptions[0])
        self.__txt_movie_txt1.config(state=tk.DISABLED)

        self.__fra_movie_fra2 = tk.Frame(self.__window, width=55, height=5)
        self.__fra_movie_fra2.place(x=550, y=290)
        self.__txt_movie_txt2 = tk.Text(self.__fra_movie_fra2, width=50, height=5)
        self.__scb_movie_scb2 = tk.Scrollbar(self.__fra_movie_fra2)
        self.__txt_movie_txt2.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.Y)
        self.__scb_movie_scb2.pack(side=tkinter.constants.RIGHT, fill=tkinter.constants.Y)
        self.__scb_movie_scb2.config(command=self.__txt_movie_txt2.yview)
        self.__txt_movie_txt2.config(yscrollcommand=self.__scb_movie_scb2.set)
        self.__txt_movie_txt2.insert(tkinter.END, self.movie_descriptions[1])
        self.__txt_movie_txt2.config(state=tk.DISABLED)

        self.__fra_movie_fra3 = tk.Frame(self.__window, width=55, height=5)
        self.__fra_movie_fra3.place(x=550, y=520)
        self.__txt_movie_txt3 = tk.Text(self.__fra_movie_fra3, width=50, height=5)
        self.__scb_movie_scb3 = tk.Scrollbar(self.__fra_movie_fra3)
        self.__txt_movie_txt3.pack(side=tkinter.constants.LEFT, fill=tk.constants.Y)
        self.__scb_movie_scb3.pack(side=tkinter.constants.LEFT, fill=tk.constants.Y)
        self.__scb_movie_scb3.config(command=self.__txt_movie_txt3.yview)
        self.__txt_movie_txt3.config(yscrollcommand=self.__scb_movie_scb3.set)
        self.__txt_movie_txt3.insert(tkinter.END, self.movie_descriptions[2])
        self.__txt_movie_txt3.config(state=tk.DISABLED)

    def __update_gui_event_menu(self):
        self.__clear_gui()

        self.event_select = self.__o_controller.show_events()
        self.__o_controller.set_selected_event(self.event_select[0])

        self.__lbl_event_lab1 = tk.Label(self.__window, text=self.__event_lab1_var, font=("Arial", 14), width=50, height=2,
                                         anchor="w")
        self.__lbl_event_lab1.place(x=80, y=60)
        self.__rad_event_rad1 = tk.Radiobutton(self.__window, text=self.event_select[0],
                                               value=self.event_select[0], font=("Arial", 12),
                                               command=lambda: self.__o_controller.set_selected_event(
                                             self.event_select[0]))
        self.__rad_event_rad2 = tk.Radiobutton(self.__window, text=self.event_select[1],
                                               value=self.event_select[1], font=("Arial", 12),
                                               command=lambda: self.__o_controller.set_selected_event(
                                             self.event_select[1]))
        self.__rad_event_rad3 = tk.Radiobutton(self.__window, text=self.event_select[2],
                                               value=self.event_select[2], font=("Arial", 12),
                                               command=lambda: self.__o_controller.set_selected_event(
                                             self.event_select[2]))
        self.__rad_event_rad1.select()
        self.__rad_event_rad1.place(x=150, y=150)
        self.__rad_event_rad2.place(x=150, y=200)
        self.__rad_event_rad3.place(x=150, y=250)
        self.__btn_event_btn1 = tk.Button(self.__window, text="Weiter",
                                          command=self.__o_controller.change_event_booking, width=10, height=2)
        self.__btn_event_btn1.place(x=700, y=640)

    def __update_gui_booking_menu(self):
        self.__clear_gui()

        self.__selected_seats = set()

        self.__lbl_booking_lab1 = tk.Label(self.__window, text=self.__o_controller.get_selected_movie(),
                                           font=("Arial", 14), width=50, height=2, anchor="w")
        self.__lbl_booking_lab1.place(x=80, y=60)
        self.__lbl_booking_lab2 = tk.Label(self.__window, text=self.__o_controller.get_selected_cinema(),
                                           font=("Arial", 14), width=50, height=2, anchor="w")
        self.__lbl_booking_lab2.place(x=80, y=110)
        self.__lbl_booking_lab3 = tk.Label(self.__window, text=self.__o_controller.get_selected_event(),
                                           font=("Arial", 14), width=20, height=2, anchor="e")
        self.__lbl_booking_lab3.place(x=680, y=60)

        total_seats_tuple = self.__o_controller.get_total_seats()
        total_seats = total_seats_tuple[0]

        booked_seats = self.__o_controller.get_booked_seats()

        rows = 5
        cols = total_seats // rows

        # Festlegen der Anfangsposition des ersten Buttons
        start_x = 300
        start_y = 300
        button_width = 60
        button_height = 40
        padding_x = 15
        padding_y = 15

    # Erstellen Sie eine Schleife, um Buttons für jeden Sitzplatz zu erstellen und sie zu platzieren
        for row in range(rows):
            for col in range(cols):
                seat_number = row * cols + col + 1
                button_x = start_x + col * (button_width + padding_x)
                button_y = start_y + row * (button_height + padding_y)
                color = booked_seats[seat_number - 1]
                button = tk.Button(self.__window, text=str(seat_number),
                                   command=lambda num=seat_number: self.set_seats_clicked(num),
                                   width=5, height=2, bg=color)
                button.place(x=button_x, y=button_y)
                if button.cget("bg") == "red":
                    button.config(state="disabled")
                self.__btn_booking_btn_list.append(button)

        self.__btn_booking_btn1 = tk.Button(self.__window, text="Buchen", command=self.book_seats, width=10, height=2)
        self.__btn_booking_btn1.place(x=700, y=640)

    def booking_pop_up(self, booking_id, cinema_title, selected_movie, selected_event, selected_seats):
        message = (f"Buchungs-ID: {booking_id}\nAusgewähltes Kino: {cinema_title}\nAusgewählter Film: "
                   f"{selected_movie}\nAusgewähltes Event: {selected_event}\nAusgewählte Sitze: {selected_seats}")
        tk_msg_box.showinfo("Buchungszusammenfassung", message)

    def __clear_gui(self):
        # This method hides all elements on the current GUI to ensure only the correct widgets for the current
        # GUI state get displayed

        try:
            self.__btn_main_cinema.place_forget()

            self.__lbl_movie_lab1.place_forget()
            self.__lbl_movie_lab2.place_forget()
            self.__lbl_movie_lab3.place_forget()
            self.__btn_movie_mov1.place_forget()
            self.__btn_movie_mov2.place_forget()
            self.__btn_movie_mov3.place_forget()
            self.__txt_movie_txt1.place_forget()
            self.__txt_movie_txt2.place_forget()
            self.__txt_movie_txt3.place_forget()
            self.__scb_movie_scb1.place_forget()
            self.__scb_movie_scb2.place_forget()
            self.__scb_movie_scb3.place_forget()
            self.__fra_movie_fra1.place_forget()
            self.__fra_movie_fra2.place_forget()
            self.__fra_movie_fra3.place_forget()

            self.__lbl_event_lab1.place_forget()
            self.__rad_event_rad1.place_forget()
            self.__rad_event_rad2.place_forget()
            self.__rad_event_rad3.place_forget()
            self.__btn_event_btn1.place_forget()

            self.__lbl_booking_lab1.place_forget()
            self.__lbl_booking_lab2.place_forget()
            self.__lbl_booking_lab3.place_forget()
            self.__btn_booking_btn1.place_forget()
        except AttributeError as e:
            log.exception(f"AttributeError: {e}")
        except tk.TclError as e:
            log.exception(f"Error while destroying widgets: {e}")

        for button in self.__btn_booking_btn_list:
            try:
                button.place_forget()
            except AttributeError as e:
                log.exception(f"AttributeError: {e}")
            except tk.TclError as e:
                log.exception(f"Error while destroying widgets: {e}")

        for button in self.__cinema_buttons:
            try:
                button.place_forget()
            except AttributeError as e:
                log.exception(f"AttributeError: {e}")
            except tk.TclError as e:
                log.exception(f"Error while destroying widgets: {e}")

    def book_seats(self):
        seat_list = self.get_seat_list()
        selected_seats = self.get_selected_seats()
        self.__o_controller.book_seats(seat_list, selected_seats)

    def select_cinema(self, hall_id, cinema_title):
        self.__selected_cinema_title = cinema_title
        self.__selected_hall_id = hall_id
        self.__o_controller.set_selected_cinema(cinema_title, hall_id)
        self.__o_controller.change_cinema_movie()

    def get_gui_status(self):
        return self.__gui_status

    def get_booked_seats(self):
        return self.__booked_seats

    def get_seat_list(self):
        seat_list = []
        for button in self.__btn_booking_btn_list:
            if button.cget('bg') == 'red':
                seat_list.append('1')
            else:
                seat_list.append('0')
        return ''.join(seat_list)

    def get_selected_seats(self):
        return self.__selected_seats

    def set_gui_status(self, p_gui_status):
        self.__gui_status = p_gui_status
        return

    def set_event_lab1_var(self, p_event_lbl1_var):
        self.__event_lab1_var = p_event_lbl1_var
        return

    def set_booked_seats(self, booked_seats):
        for button in self.__btn_booking_btn_list:
            seat_number = int(button.cget('text'))
            color = booked_seats[seat_number - 1]  # Get color from booked seats list
            button.config(bg=color)

    def set_seats_clicked(self, seat_number):
        if seat_number in self.__selected_seats:
            # If seat is already selected, deselect it
            self.__selected_seats.remove(seat_number)
            color = 'green'  # Set color back to green
        else:
            # If seat is not selected, select it
            self.__selected_seats.add(seat_number)
            color = 'red'  # Set color to red

        # Change background color of the clicked button
        for button in self.__btn_booking_btn_list:
            if int(button.cget('text')) == seat_number:
                button.config(bg=color, relief=tkinter.constants.SOLID if color == 'red' else tkinter.constants.RAISED)
