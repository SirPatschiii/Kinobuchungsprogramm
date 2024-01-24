import sys


class Label:
    def __init__(self):
        print("Label works")

    def get_labels(self, gui_status):
        if gui_status == "main":
            return self.__labels_for_main_menu()
        elif gui_status == "cinema":
            return self.__labels_for_cinema_menu()
        elif gui_status == "movie":
            return self.__labels_for_movie_menu()
        elif gui_status == "event":
            return self.__labels_for_event_menu()
        elif gui_status == "booking":
            return self.__labels_for_booking_menu()
        elif gui_status == "booking_sum":
            return self.__labels_for_booking_summary()
        else:
            sys.exit(-1)

    def __labels_for_main_menu(self):
        labels = []
        # TODO Labels erstellen für Hauptmenü
        return labels

    def __labels_for_cinema_menu(self):
        labels = []
        # TODO Labels erstellen für Kinomenü
        return labels

    def __labels_for_movie_menu(self):
        labels = []
        # TODO Labels erstellen für Filmmenü
        return labels

    def __labels_for_event_menu(self):
        labels = []
        # TODO Labels erstellen für Eventmenü
        return labels

    def __labels_for_booking_menu(self):
        labels = []
        # TODO Labels erstellen für Buchungsmenü
        return labels

    def __labels_for_booking_summary(self):
        labels = []
        # TODO Labels erstellen für Buchungszusammenfassung
        return labels
