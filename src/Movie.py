import sqlite3


class Movie:
    def __init__(self):
        print("Movie works!")

    @staticmethod
    def connect_db():
        connect = sqlite3.connect("cinemadata.db")
        cursor_db = connect.cursor()

    @staticmethod
    def test_connect(cursor_db):
        cursor_db.execute("SELECT * FROM movie")
        user_data = cursor_db.fetchall()
        print(user_data)



