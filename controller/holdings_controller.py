import sqlite3

from view.holdings_view import HoldingsView

class HoldingsController:
    def __init__(self, root_controller):
        self.repository = root_controller.holdings_repository
        self.view = HoldingsView(self, root_controller.view)
        print(self.repository)

    def calc_holdings(self):
        connect = sqlite3.connect("asset_records.db")
        cursor = connect.cursor()

        cursor.execute("SELECT ticker_symbol, order_type, value FROM orders")

    def data_to_table(self):
        columns = "oid, ticker_symbol, quantity"
        return self.repository.data_to_table(columns)