import sqlite3


class Event:
    def __init__(self):
        self.cursor_db = None
        print("Event works!")

    def connect_db(self):
        connect = None

        try:
            connect = sqlite3.connect("src/cinemadata.db")
            print("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            print(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")

        try:
            connect = sqlite3.connect("../src/cinemadata.db")
            print("Connection to the database successful!")
        except sqlite3.OperationalError as e:
            print(f"Error connecting to the database: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")

        self.cursor_db = connect.cursor()

    def title(self, event_id):
        self.cursor_db.execute(f"SELECT date FROM events WHERE eventID='{event_id}'")
        event = self.cursor_db.fetchone()
        return event[0] if event else None
