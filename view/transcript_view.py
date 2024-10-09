import sqlite3
from tkinter import *
from datetime import date

class TranscriptView(Toplevel):
    def __init__(self, controller, rootview):
        super().__init__(rootview)
        self.title("Tax Transcript")
        self.controller = controller
        self.row = 10
        self.render_widgets()
        self.render_gains_losses()
        self.render_labels()
        self.render_tables()
        self.render_options()

    def render_widgets(self):
        self.date_label = Label(self, text="Date:")
        self.date_label.grid(row=0, column=0)
        self.date_entry = Entry(self, width=12)
        self.date_entry.grid(row=0, column=1)
        self.date_entry.insert(0, date.today().strftime("%m/%d/%Y"))

        self.order_type = StringVar()
        self.order_type.set("buy")
        self.buy = Radiobutton(self, text="Buy", variable=self.order_type,
                               value="buy")
        self.buy.grid(row=1, column=1)
        self.sell = Radiobutton(self, text="Sell", variable=self.order_type,
                                value="sell")
        self.sell.grid(row=1, column=2)

        self.sym_label = Label(self, text="Ticker Symbol:")
        self.sym_label.grid(row=2, column=0)
        self.sym_entry = Entry(self, width=10)
        self.sym_entry.grid(row=2, column=1)

        self.qnty_label = Label(self, text="Quantity: ")
        self.qnty_label.grid(row=3, column=0)
        self.qnty_entry = Entry(self, width=5)
        self.qnty_entry.grid(row=3, column=1)

        self.price_label = Label(self, text="Price per Share:    $")
        self.price_label.grid(row=3, column=2)
        self.price_entry = Entry(self, width=10)
        self.price_entry.grid(row=3, column=3)

        submit = Button(self, text="Submit", width=15, command=self.confirm_entries)
        submit.grid(row=4, column=2)

    def confirm_entries(self):
        all_entries = (self.date_entry.get(), self.order_type.get(),
                       self.sym_entry.get(), self.qnty_entry.get(),
                       self.price_entry.get())
        for entry in all_entries:
            if entry == "" or entry == "{}":
                error_label = Label(self, text="Please Fill Out All Fields")
                error_label.grid(row=5, column=4)
            else:
                self.controller.submit_order()

    def render_gains_losses(self):
        gainloss_label = Label(self, text="Gains/Losses: ", font=("Arial", 25))
        gainloss_label.grid(row=7, column=2)


    def render_labels(self):
        labels = ("ID", "Date", "Order Type", "Ticker Symbol", "Quantity", "Price/Share", "Value")
        column = 0
        for label in labels:
            category = Label(self, text=label)
            category.grid(row=9, column=column)
            column += 1

    def render_tables(self):
        connect = sqlite3.connect("asset_records.db")
        cursor = connect.cursor()

        categories = "oid", "date", "order_type", "ticker_symbol", "quantity", "price", "value"
        column = 0
        for category in categories:
            cursor.execute(f"SELECT {category} FROM orders")
            tables = cursor.fetchall()
            print(tables)

            self.row = 10
            for table in tables:
                transcript = Label(self, text=table)
                transcript.grid(row=self.row, column=column)
                self.row += 1

            column += 1

        connect.commit()
        connect.close()

    def render_options(self):
        id_label = Label(self, text="Enter an order ID and select an option:")
        id_label.grid(row=(self.row + 1), column=1, columnspan=2)
        self.id_entry = Entry(self, width=10)
        self.id_entry.grid(row=(self.row + 1), column=3)

        edit_button = Button(self, text="Edit Order")
        edit_button.grid(row=(self.row + 2), column=1)

        delete_button = Button(self, text="Delete Order", command=self.controller.delete_order)
        delete_button.grid(row=(self.row + 2), column=3)

    def render_edit_fields(self):
        """Renders entry boxes if edit button is pressed"""
        pass
