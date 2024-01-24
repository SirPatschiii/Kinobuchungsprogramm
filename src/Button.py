import sys


class Button:
    def __init__(self):
        print("Button works!")

    def get_buttons(self, gui_status):
        if gui_status == "main":
            return self.__buttons_for_main_menu()
        elif gui_status == "cinema":
            return self.__buttons_for_cinema_menu()
        elif gui_status == "movie":
            return self.__buttons_for_movie_menu()
        elif gui_status == "event":
            return self.__buttons_for_event_menu()
        elif gui_status == "booking":
            return self.__buttons_for_booking_menu()
        elif gui_status == "booking_sum":
            return self.__buttons_for_booking_summary()
        else:
            return sys.exit(-1)

    def __buttons_for_main_menu(self):
        buttons = []
        # TODO Buttons erstellen für Hauptmenü
        return buttons

    def __buttons_for_cinema_menu(self):
        buttons = []
        # TODO Buttons erstellen für Kinomenü
        return buttons

    def __buttons_for_movie_menu(self):
        buttons = []
        # TODO Buttons erstellen für Filmmenü
        return buttons

    def __buttons_for_event_menu(self):
        buttons = []
        # TODO Buttons erstellen für Eventmenü
        return buttons

    def __buttons_for_booking_menu(self):
        buttons = []
        # TODO Buttons erstellen für Buchungsmenü
        return buttons

    def __buttons_for_booking_summary(self):
        buttons = []
        # TODO Buttons erstellen für Buchungszusammenfassung
        return buttons
