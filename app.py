import pandas as pd
import streamlit as st
import plotly.express as px

from config import DB_DIR, SYMBOLS
from storage import DataBaseManager


class DashBoard:
    def __init__(self,db,symbols,refresh_seconds=2):
        self.db = db
        self.symbols = symbols

    def render(self):
        symbol=st.selectbox(
            "Select Symbol",
            self.symbols
        )
        last=self.db.fetch_ticker(symbol)
        if last is None:
            st.info('Waiting for data... Start the collector first')
            return

        last_ts,last_price=last
        st.metric(label=f"{symbol} last price",value=last_price)
        st.caption(f"Last Update: {last_ts}")

        rows=self.db.fetch_latest(symbol,limit=500)

        if not rows:
            st.info('No data to display')
            return

        timestamps=[row[0] for row in rows]
        prices=[row[1] for row in rows]
        data=sorted(zip(timestamps,prices),key=lambda x: x[0])
        timestamps,prices=zip(*data)

        df = pd.DataFrame({
            "ts": timestamps,
            "price": prices
        })

        fig = px.line(df, x="ts", y="price", title=f"{symbol} Price Over Time")
        st.plotly_chart(fig,use_container_width=True)

        min_price=min(prices)
        max_price=max(prices)
        avg_price=sum(prices) / len(prices)

        first_price=prices[0]
        last_price=prices[-1]

        change_pct=((last_price-first_price)/first_price)*100 if first_price!=0 else 0

        col1, col2 ,col3 ,col4 =st.columns(4)

        col1.metric("Min",f"{min_price:.4f}")
        col2.metric("Max", f"{max_price:.4f}")
        col3.metric("Average", f"{avg_price:.4f}")
        col4.metric("Change", f"{change_pct:.4f}")


        if st.button("Refresh"):

           st.rerun()


db=DataBaseManager(DB_DIR)
db.init_db()
DashBoard(db=db,symbols=SYMBOLS,refresh_seconds=2).render()

