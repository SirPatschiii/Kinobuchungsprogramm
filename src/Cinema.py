import sqlite3


class Cinema:
    def __init__(self):
        self.cursor_db = None
        print("Cinema Works!")

    def connect_db(self):
        connect = None

        try:
            connect = sqlite3.connect("src/cinemadata.db")
        except sqlite3.OperationalError as e:
            print(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")

        try:
            connect = sqlite3.connect("../src/cinemadata.db")
        except sqlite3.OperationalError as e:
            print(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")

        self.cursor_db = connect.cursor()

    def title(self):
        self.cursor_db.execute("SELECT name FROM cinema WHERE hallID='1'")
        user_data = self.cursor_db.fetchall()
        return user_data
