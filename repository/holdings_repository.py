from connection import Connection
conn = Connection.get()

class HoldingsRepository:
    def __init__(self):
        self.create_table()

    def create_table(self):
        conn.execute("""CREATE TABLE IF NOT EXISTS holdings (
                                ticker_symbol text,
                                quantity real
                                )""")

    def data_to_table(self, columns):
        statement = f"SELECT {columns} FROM holdings"
        return conn.execute(statement).fetchall()

    def update_quantity(self, oid, quantity):
        statement = "UPDATE holdings SET quantity = ? WHERE oid = ?"
        conn.execute(statement, (quantity, oid)).rowcount

    def insert(self, ticker_symbol, quantity):
        conn.execute("""INSERT INTO holdings (
                                ticker_symbol,
                                quantity)
                                VALUES (
                                ?, ?)""", [
            ticker_symbol,
            quantity
        ])
        conn.commit()
