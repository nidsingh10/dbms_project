import pandas as pd
import streamlit as st
from database import view_cart, order

def cart():
    with st.expander("Cart"):
        result = view_cart()

        for product in result:
            product_id,seller_id,product_name,discount_coupon,size,price,quantity,brand,description = product
            col1, col2 = st.columns(2)
            with col1:
                st.title(product_name)
                st.write(f"Product ID: {product_id}")
                st.write(f"Seller ID: {seller_id}")
                st.write(f"Size: {size}")
                
            with col2:
                st.write(f"Price: {price}")
                st.write(f"Quantity: {quantity}")
                st.write(f"Brand: {brand}")
                st.write(f"Description: {description}")


    st.button(label='Order',on_click=order, args=(result,))

    
    
