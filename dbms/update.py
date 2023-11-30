import pandas as pd
import streamlit as st
from database import view_products, edit_product_data, view_all_order, edit_order_data


def update():
    result = view_products()
    df = pd.DataFrame(result, columns=['product_id', 'seller_id', 'product_name', 'discount_coupon', 'size', 'price', 'quantity', 'brand', 'description', 'discount_id','rating'])
    
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_product_id = st.text_input("Product ID")
        with col2:
            new_price = st.text_input("New Price:")
            new_quantity = st.text_input("New Quantity:")

        if st.button("Update Product"):
            edit_product_data(new_price, new_quantity, up_product_id)
            st.success("Product information successfully updated")

    result2 = view_products()
    df2 = pd.DataFrame(result2, columns=['product_id', 'seller_id', 'product_name', 'discount_coupon', 'size', 'price', 'quantity', 'brand', 'description', 'discount_id','rating'])
    
    with st.expander("Updated data"):
        for product in result2:
            product_id, seller_id, product_name, discount_coupon, size, price, quantity, brand, description, discount_id,rating = product

            # Use st.columns to create columns for a card-like layout
            col1, col2 = st.columns(2)

            # Display product information in a card-like format
            with col1:
                st.title(product_name)
                st.write(f"Product ID: {product_id}")
                st.write(f"Seller ID: {seller_id}")
                st.write(f"Discount Coupon: {discount_coupon}")
                st.write(f"Size: {size}")

            with col2:
                st.write(f"Price: {price}")
                st.write(f"Quantity: {quantity}")
                st.write(f"Brand: {brand}")
                st.write(f"Description: {description}")
                st.write(f"Discount ID: {discount_id}")
                st.write(f"Ratings: {rating}")

    if st.session_state['role'] != 'seller':
        with st.expander('Update Order Status'):
            orders = view_all_order()

            for i in orders:
                order_id, product_id , status ,customer_id= i[0], i[1], i[2], i[3]
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader(f"Order ID : {order_id}")
                    st.write(f"Product ID : {product_id}")
                with col2:
                    st.write(f"Current Status : {status}")
                    st.write(f"Ordered by: {customer_id}")

            col1, col2 = st.columns(2)
            with col1:
                order_id = st.text_input("Order ID")
            with col2:
                status = st.selectbox("Order Status", ["Out for Delivery", "Delivered"])

            if st.button("Update Order Status"):
                edit_order_data(status, order_id)
                st.success("Order information successfully updated")


        
