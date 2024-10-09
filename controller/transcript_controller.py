import sqlite3
from tkinter import END
from connection import Connection

from utils.enums import EOrderType, EOrderStatus
from view.transcript_view import TranscriptView

class TranscriptController:
    def __init__(self, root_controller):
        self.view = TranscriptView(self, root_controller.view)
        self.conn = Connection.get()
        self.holdings_repository = root_controller.holdings_repository
    def submit_order(self):
        self.conn.execute("DROP TABLE orders")
        self.conn.execute(f"""CREATE TABLE IF NOT EXISTS orders (
                      order_id integer PRIMARY KEY AUTOINCREMENT NOT NULL, 
                      date text,
                      order_type text,
                      ticker_symbol text,
                      quantity real,
                      price real,
                      value real,
                      remaining real
                  )""")

        info = {
            "date": self.view.date_entry.get(),
            "order_type": self.view.order_type.get(),
            "ticker_symbol": self.view.sym_entry.get(),
            "quantity": float(self.view.qnty_entry.get()),
            "price": self.view.price_entry.get(),
            "value": float(self.view.qnty_entry.get()) * float(self.view.price_entry.get()),
            "remaining": float(self.view.qnty_entry.get())
        }

        self.conn.execute("INSERT INTO orders VALUES (:date, :order_type,"
                       " :ticker_symbol, :quantity, :price, :value, :remaining)", info)


        self.update_holdings(info)

        self.empty_feilds()

    def update_holdings(self, dict):


        holding = self.conn.execute("SELECT oid, quantity FROM holdings WHERE ticker_symbol = ?",
                       [dict["ticker_symbol"]]).fetchone()
        if holding == None:
            self.holdings_repository.insert(dict["ticker_symbol"], dict["quantity"])

        else:
            if dict["order_type"] == EOrderType.BUY:
                quantity = holding[1] + dict["quantity"]
            else:
                quantity = holding[1] - dict["quantity"]

            self.holdings_repository.update_quantity(holding[0], quantity)

        print(f"HOLDING: {holding}")

        self.conn.execute("SELECT oid FROM holdings")


    def empty_feilds(self):
        self.view.date_entry.delete(0, END)
        self.view.sym_entry.delete(0, END)
        self.view.qnty_entry.delete(0, END)
        self.view.price_entry.delete(0, END)

    def delete_order(self):

        self.conn.execute("DELETE from orders WHERE oid= " + self.view.id_entry.get())

#        self.conn.execute("""
 #           UPDATE orders
  #          SET id = (
   #             SELECT COUNT(*) + 1
    #            FROM orders AS t2
     #           WHERE t2.id <= orders.id
      #      )
       # """)

        self.view.id_entry.delete(0, END)

        self.view.render_tables()


    def edit_order(self):
        """Edits an order"""
        pass

    def calc_gains_losses(self):
        """Calculates current capital gains/losses for year"""

        self.conn.execute("SELECT order_type, value FROM orders")




