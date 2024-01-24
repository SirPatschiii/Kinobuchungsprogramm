import sys


class Radiobox:
    def __init__(self):
        print("Radiobox works!")

    def get_radio_boxes(self, gui_status):
        if gui_status == "event":
            return self.__radio_boxes_for_event_menu()
        else:
            sys.exit(-1)

    def __radio_boxes_for_event_menu(self):
        radio_boxes = []
        # TODO Radio boxes erstellen für Eventmenü
        return radio_boxes
