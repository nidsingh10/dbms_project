import pandas as pd
import streamlit as st
from database import view_products,add_data_cart, seller_view_products

def read():
    with st.expander("View Products"):
        if st.session_state['role'] == "seller":
            result = seller_view_products()
        else:
            result = view_products()
        for product in result:
            product_id, seller_id, product_name, discount_coupon, size, price, quantity, brand, description, discount_id, rating = product
            col1, col2 = st.columns(2)
            with col1:
                st.title(product_name)
                st.write(f"Product ID: {product_id}")
                st.write(f"Seller ID: {seller_id}")
                st.write(f"Discount Coupon: {discount_coupon}")
                st.write(f"Size: {size}")
                st.button(label='Add to Cart',on_click=add_data_cart, args=(product_id,), key=product_id)

                

            with col2:
                st.write(f"Price: {price}")
                st.write(f"Quantity: {quantity}")
                st.write(f"Brand: {brand}")
                st.write(f"Description: {description}")
                st.write(f"Discount ID: {discount_id}")
                st.write(f"Ratings: {rating}")

    
    
