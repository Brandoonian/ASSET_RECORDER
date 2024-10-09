import sqlite3

class Connection:
    __conn = None

    def get():
        if Connection.__conn == None:
            print("CONNECTING.....")
            Connection.__conn = sqlite3.connect("asset_records.db")
        else:
            print("Already connected")

        return Connection.__conn

    def cursor():
        return Connection.get().cursor()