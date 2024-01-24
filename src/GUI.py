import tkinter as tk


class GUI:
    def __init__(self):
        print("GUI works!")
        self.window = tk.Tk()
        self.gui_status = "main"

    def update_gui(self):
        # TODO hier müssen die fertigen Buttons, Labels etc. ankommen
        pass

    def get_gui_status(self):
        return self.gui_status
