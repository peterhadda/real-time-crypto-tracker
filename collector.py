import datetime
from config import DB_DIR,SYMBOLS,BASE_URL,POLL_INTERVAL
from tornado.gen import sleep
import requests

from storage import DataBaseManager


class PriceCollector:



    def __init__(self,symbols,poll_interval,api_url,db):


        self.symbols = symbols
        self.poll_interval = poll_interval
        self.api_url = api_url
        self.db = db


    def fetch_price(self,symbol):
        try:
            symbol=symbol.strip().upper()
            api_request = requests.get(self.api_url,params={'symbol':symbol},timeout=5)

            if api_request.status_code == 200:
                JSON = api_request.json()
                price = float(JSON["price"])
                return price
            else:
                return None
        except Exception as e:
            print("Request failed",e)
            return None

    def run(self):

       for symbol in self.symbols:
           price = self.fetch_price(symbol)
           timestamp=datetime.datetime.now(datetime.UTC).isoformat()
           if price is not None:
               self.db.insert_db(timestamp,symbol,price)
           sleep(self.poll_interval)

if __name__ == "__main__":
    db=DataBaseManager(DB_DIR)
    db.init_db()
    collector=PriceCollector(SYMBOLS,POLL_INTERVAL,BASE_URL,db)
    collector.run()