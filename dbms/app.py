
# import streamlit as st
# import pymysql
# from create import create
# from delete import delete
# from read import read
# from update import update
# from cart import cart
# from orders import orders
# from database import login_user, register_user, view_products, add_data_cart


# def main():
#     st.title("OMNI E-COMMERCE")
#     role = ' '

#     reg = st.sidebar.selectbox("Login/Register", ["Login", "Register"])
#     if reg == "Login":
#         st.subheader("Login")
#         login_email = st.text_input("Email")
#         login_password = st.text_input("Password", type="password")
#         if st.button("Login"):
#             role, customer_id = login_user(login_email, login_password)
#             st.session_state['role'] = role
#             st.session_state['customer_id'] = customer_id

#     if reg == "Register":
#         st.subheader("Register")
#         login_email = st.text_input("Email")
#         login_password = st.text_input("Password", type="password")
#         role = st.selectbox("Select Role", ["user", "admin", "seller"])
#         if st.button("Register"):
#             register_user(login_email, login_password, role)

#     choice1 = ''  # Initialize choice1 here to ensure it's defined in all scenarios

#     if st.session_state.get('role') == 'admin':
#         choice1 = st.sidebar.selectbox("Admin", ["About", "View", "Add", "Update", "Delete"])
#     elif st.session_state.get('role') == 'user':
#         choice1 = st.sidebar.selectbox("Customer", ["About", "View", "Cart", "Orders"])
#     elif st.session_state.get('role') == 'seller':
#         choice1 = st.sidebar.selectbox("Seller", ["About", "View", "Add", "Update", "Delete"])

#     if choice1 == "About":
#         st.image('a.png', channels="RGB", output_format="auto")
#         """
#         Presenting you guys, OMNI, an e-commerce website for clothing. This website is built by Nidhi Singh & Omkar Jois.
#         """
#     elif choice1 == "View":
#         st.subheader("View Products")
#         read()
#     elif choice1 == "Cart" and st.session_state.get('role') == 'user':
#         cart()
#     elif choice1 == "Orders" and st.session_state.get('role') == 'user':
#         orders()
#     elif choice1 == "Add" and (st.session_state.get('role') == 'admin' or st.session_state.get('role') == 'seller'):
#         create()
#     elif choice1 == "Update" and (st.session_state.get('role') == 'admin' or st.session_state.get('role') == 'seller'):
#         st.subheader("Update Products details")
#         update()
#     elif choice1 == "Delete" and (st.session_state.get('role') == 'admin' or st.session_state.get('role') == 'seller'):
#         st.subheader("Delete Products")
#         delete()

# if __name__ == '__main__':
#     main()



import streamlit as st
import pymysql
from create import create
from delete import delete
from read import read
from update import update
from cart import cart
from orders import orders
from database import login_user, register_user, view_products, add_data_cart, add_data_seller


def main():
    st.title("OMNI E-COMMERCE")
    with st.expander("Login"):
        role = ' '

        reg = st.sidebar.selectbox("Login/Register", ["Login", "Register"])
        if reg == "Login":
            st.subheader("Login")
            login_email = st.text_input("Email")
            login_password = st.text_input("Password", type="password")
            if st.button("Login"):
                role, customer_id = login_user(login_email, login_password)
                st.session_state['role'] = role
                st.session_state['customer_id'] = customer_id

        if reg == "Register":
            st.subheader("Register")
            login_email = st.text_input("Email")
            login_password = st.text_input("Password", type="password")
            role = st.selectbox("Select Role", ["user", "admin", "seller"])
            if st.button("Register"):
                if role == 'seller':
                    add_data_seller(login_email, login_password)
                else:
                    register_user(login_email, login_password, role)

    choice1 = ''  # Initialize choice1 here to ensure it's defined in all scenarios

    if st.session_state.get('role') == 'admin':
        choice1 = st.sidebar.selectbox("Admin", ["About", "View", "Add", "Update", "Delete"])
    elif st.session_state.get('role') == 'user':
        choice1 = st.sidebar.selectbox("Customer", ["About", "View", "Cart", "Orders"])
    elif st.session_state.get('role') == 'seller':
        choice1 = st.sidebar.selectbox("Seller", ["About", "View", "Add", "Update", "Delete"])

    if choice1 == "About":
        st.image('a.png', channels="RGB", output_format="auto")
        """
        Presenting you guys, OMNI, an e-commerce website for clothing. This website is built by Nidhi Singh & Omkar Jois.
        """
    elif choice1 == "View":
        st.subheader("View Products")
        read()
    elif choice1 == "Cart" and st.session_state.get('role') == 'user':
        cart()
    elif choice1 == "Orders" and st.session_state.get('role') == 'user':
        orders()
    elif choice1 == "Add" and (st.session_state.get('role') == 'admin' or st.session_state.get('role') == 'seller'):
        create()
    elif choice1 == "Update" and (st.session_state.get('role') == 'admin' or st.session_state.get('role') == 'seller'):
        st.subheader("Update Products details")
        update()
    elif choice1 == "Delete" and (st.session_state.get('role') == 'admin' or st.session_state.get('role') == 'seller'):
        st.subheader("Delete Products")
        delete()

if __name__ == '__main__':
    main()
