import sqlite3
from pathlib import Path

SYMBOLS=["BTCUSDT","ETHUSDT"]

BASE_URL="https://api.binance.com/api/v3/ticker/price"


BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

DB_DIR = DATA_DIR / "data.db"

POLL_INTERVAL = 2

