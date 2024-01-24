import sys


class Entry:
    def __init__(self):
        print("Entry works!")

    def get_entries(self, gui_status):
        if gui_status == "signup":
            return self.__entries_for_signup_menu()
        elif gui_status == "signin":
            return self.__entries_for_signin_menu()
        else:
            sys.exit(-1)

    def __entries_for_signup_menu(self):
        entries = []
        # TODO !!Optional!! Entries erstellen für Signup-Menü
        return entries

    def __entries_for_signin_menu(self):
        entries = []
        # TODO !!Optional!! Entries erstellen für Signin-Menü
        return entries
