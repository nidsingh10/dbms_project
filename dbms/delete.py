import pandas as pd
import streamlit as st
from database import view_products, delete_products


def delete():
    result = view_products()
    df = pd.DataFrame(result, columns=['product_id', 'seller_id', 'product_name', 'discount_coupon', 'size', 'price', 'quantity', 'brand', 'description', 'discount_id','rating'])
    
    with st.expander("Current data"):
        st.dataframe(df)

    selected_product = st.text_input("product_id")

    st.warning("Do you want to delete ::{}".format(selected_product))
    
    if st.button("Delete Product"):
        delete_products(selected_product)
        st.success("Product has been deleted successfully")

    new_result = view_products()
    df2 = pd.DataFrame(new_result, columns=['product_id', 'seller_id', 'product_name', 'discount_coupon', 'size', 'price', 'quantity', 'brand', 'description', 'discount_id','rating'])

    with st.expander("Updated data"):
        for product in new_result:
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
