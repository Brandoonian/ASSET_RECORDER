import sqlite3
from tkinter import *
from connection import Connection
conn = Connection.get()

class HoldingsView(Toplevel):
    def __init__(self, controller, rootview):
        super().__init__(rootview)
        self.title("Holdings")
        self.controller = controller
        self.render_labels()
        self.render_holdings()

    def render_labels(self):
        ID_label = Label(self, text="ID")
        ID_label.grid(row=0, column=0)
        ticker_label = Label(self, text="Ticker Symbol")
        ticker_label.grid(row=0, column=1)
        quantity_label = Label(self, text="Qnty")
        quantity_label.grid(row=0, column=2)


    def render_holdings(self):
        """Renders table showing current asset ticker symbols and quantities."""
        items = self.controller.data_to_table()
        row = 1
        for item in items:
            for i, value in enumerate(item):
                transcript = Label(self, text=value)
                transcript.grid(row=row, column=i)
            row += 1
        # categories = "oid", "ticker_symbol"
        # column = 0
        # for category in categories:
        #     tables = conn.execute(f"SELECT {category} FROM holdings").fetchall()
        #     print(tables)
        #
        #     self.row = 1
        #     for table in tables:
        #         transcript = Label(self, text=table)
        #         transcript.grid(row=self.row, column=column)
        #         self.row += 1
        #
        #     column += 1