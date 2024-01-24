import sys


class Spinbox:
    def __init__(self):
        print("Spinbox works!")

    def get_spin_boxes(self, gui_status):
        if gui_status == "booking":
            return self.__spin_boxes_for_booking_menu()
        else:
            sys.exit(-1)

    def __spin_boxes_for_booking_menu(self):
        spin_boxes = []
        # TODO Spin boxes erstellen für Buchungsmenü
        return spin_boxes
