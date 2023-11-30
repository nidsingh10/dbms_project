import pandas as pd
import streamlit as st
from database import view_order

def orders():
    with st.expander("Order"):
        result = view_order()

        for product in result:
            order_id, product_id, quantity,status = product[0], product[2], product[3],product[4]

            col1, col2 = st.columns(2)
            with col1:
                st.title(order_id)
                st.write(f"Product ID: {product_id}")
                st.write(f"Seller ID: {quantity}")
                st.write(f"Order Status: {status}")