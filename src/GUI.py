import tkinter as tk


class GUI:
    def __init__(self):
        print("GUI works!")
        self.window = tk.Tk()
        self.gui_status = "main"

    def create_gui(self):
        self.window.geometry("1000x700")
        self.window.resizable(False, False)
        self.window.title("Kinobuchungsprogramm")
        self.window.mainloop()

    def update_gui(self, gui_status):
        # TODO hier müssen die fertigen Buttons, Labels etc. ankommen
        pass

    def get_gui_status(self):
        return self.gui_status
