# import streamlit as st
# from database import add_customer
# from database import add_data_seller
# from database import add_data_product



# def create():
#    with st.expander("Add Customer"):
#       email = st.text_input("Email:")
#       password = st.text_input("Password:", type="password")
#       role = st.selectbox("Role:", ["admin", "user"])

#       if st.button("Add Customer"):
#          add_customer(email,password,role)
#          st.success("Customer added successfully!")
         
#    with st.expander("Add Seller"):
#       name = st.text_input("Name:")
#       email = st.text_input("Email_Id:")
#       contact_no = st.text_input("Contact:")
#       address = st.text_input("Address:")


      

#       if st.button("Add Seller"):
#          add_data_seller(name,email,contact_no,address)
#          st.success("Seller added successfully!")

#    with st.expander("Add Product"):
#       product_id = st.text_input("Product_Id:")
#       seller_id = st.text_input("Seller_Id:")
#       product_name = st.text_input("Product_Name:")
#       discount_coupon=st.text_input("Discount Coupon:")
#       size=st.selectbox("Sizes:", ["S", "M","L","XL","Free size"])
#       price=st.text_input("Price:")
#       quantity=st.text_input("Quantity:")
#       brand=st.text_input("Brand:")
#       description=st.text_input("Description:")
#       discount_id=st.text_input("Discount_Id:")
      


      

#       if st.button("Add Product Details"):
#          add_data_product(product_id,seller_id,product_name,discount_coupon,size,price,quantity,brand,description,discount_id)
#          st.success("Product added successfully!")

import streamlit as st
from database import add_customer, add_data_seller, add_data_product

def create():
    if st.session_state['role'] != 'seller':
        with st.expander("Add Customer"):
            email = st.text_input("Email:")
            password = st.text_input("Password:", type="password")
            role = st.selectbox("Role:", ["admin", "user"])

            if st.button("Add Customer"):
                add_customer(email, password, role)
                st.success("Customer added successfully!")

        with st.expander("Add Seller"):
            email = st.text_input("Email_Id:")
            password = st.text_input("Password:")

            if st.button("Add Seller"):
                add_data_seller(email, password)
                st.success("Seller added successfully!")

    with st.expander("Add Product"):
        product_id = st.text_input("Product_Id:")
        if st.session_state['role'] == 'seller':
            seller_id = st.session_state['customer_id']
        else:
            seller_id = st.text_input("Seller_Id:")
        product_name = st.text_input("Product_Name:")
        discount_coupon = st.text_input("Discount Coupon:")
        size = st.selectbox("Sizes:", ["S", "M", "L", "XL", "Free size"])
        price = st.text_input("Price:")
        quantity = st.text_input("Quantity:")
        brand = st.text_input("Brand:")
        description = st.text_input("Description:")
        discount_id = st.text_input("Discount_Id:")

        if st.button("Add Product Details"):
            add_data_product(product_id, seller_id, product_name, discount_coupon, size, price, quantity, brand, description, discount_id)
            st.success("Product added successfully!")

