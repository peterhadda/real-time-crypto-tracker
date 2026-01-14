import sqlite3






class DataBaseManager:

    def __init__(self, db_dir):
        self.db_dir = db_dir

    def init_db(self):
        conn = sqlite3.connect(self.db_dir)
        cursor = conn.cursor()

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS prices(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT,
            symbol TEXT,
            PRICE REAL)
            '''
        )
        conn.commit()
        conn.close()
        return self.db_dir

    def insert_db(self,ts,symbol,price):
        conn = sqlite3.connect(self.db_dir)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO prices(ts,symbol,price) VALUES (?,?,?)
        ''',(ts,symbol,price))


        conn.commit()
        conn.close()

    def fetch_last_price(self, symbol):
        conn = sqlite3.connect(self.db_dir)
        cursor = conn.cursor()

        cursor.execute(
            'SELECT ts, PRICE FROM prices WHERE symbol=? ORDER BY id DESC LIMIT 1',
            (symbol,)
        )

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None

        ts, price = row
        return ts, price

    def fetch_latest_price(self, symbol, limit):
        limit = int(limit)
        if limit <= 0:
            return []

        conn = sqlite3.connect(self.db_dir)
        cursor = conn.cursor()

        cursor.execute(
            f'''
            SELECT ts, PRICE
            FROM prices
            WHERE symbol=?
            ORDER BY id DESC
            LIMIT {limit}
            ''',
            (symbol,)
        )

        rows = cursor.fetchall()
        conn.close()
        return rows

    def fetch_ticker(self, symbol):
        return self.fetch_last_price(symbol)

    def fetch_latest(self, symbol, limit=500):
        return self.fetch_latest_price(symbol, limit)


