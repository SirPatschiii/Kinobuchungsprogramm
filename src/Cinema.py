import sqlite3


class Cinema:
    def __init__(self):
        self.cursor_db=None
        print("Cinema Works!")

    def connect_db(self):
        connect = sqlite3.connect("cinemadata.db")
        self.cursor_db = connect.cursor()

    def title(self):
        self.cursor_db.execute("SELECT name FROM cinema WHERE hallID='1'")
        user_data = self.cursor_db.fetchall()
        return user_data


