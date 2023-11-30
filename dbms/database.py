import mysql.connector
import streamlit as st
import bcrypt
from datetime import datetime
import random


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nidhi$1004@blr23",
    database="mini_project"
)
c = mydb.cursor()

def add_customer(email, password, role):
    try:
        c.execute('INSERT INTO customer (email, password, role) VALUES (%s, %s, %s)', (email, password, role))
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Connector Error: {e}")

def add_data_seller(email, password):
    try:
        existing_ids = set()

        c.execute("SELECT seller_id FROM seller")
        existing_orders = c.fetchall()

        for order in existing_orders:
            existing_ids.add(order[0])

        while True:
            new_order_id = random.randint(10000000, 99999999)  # Random 8-digit number
            if new_order_id not in existing_ids:
                c.execute('INSERT INTO seller (seller_id, email, password) VALUES (%s, %s, %s)',
                  (str(new_order_id), email, password))
                mydb.commit()
                break
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Connector Error: {e}")

def add_data_product(product_id, seller_id, product_name, discount_coupon, size, price, quantity, brand, description, discount_id):
    try:
        c.execute('INSERT INTO product (product_id,seller_id,product_name,discount_coupon,size,price,quantity,brand,description,discount_id) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)',
                  (product_id, seller_id, product_name, discount_coupon, size, price, quantity, brand, description, discount_id))
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Connector Error: {e}")

def edit_product_data(price, quantity, product_id):
    try:
        c.execute("UPDATE product SET price=%s, quantity=%s WHERE product_id=%s", (price, quantity, product_id))
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Connector Error: {e}")

def edit_order_data(status, order_id):
    try:
        c.execute("UPDATE orders SET order_status=%s WHERE order_id=%s", (status, order_id))
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Connector Error: {e}")

def delete_products(pid):
    try:
        c.execute('DELETE FROM product WHERE product_id=%s', (pid,))
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Connector Error: {e}")

def add_data_cart(product_id):
    try:
        c.execute('INSERT INTO cart (product_id, customer_id) VALUES (%s, %s)', (product_id, st.session_state['customer_id']))
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Connector Error: {e}")

def view_cart():
    c.execute('SELECT p.product_id, p.seller_id, p.product_name, p.discount_coupon, p.size, p.price, c.quantity, p.brand, p.description FROM cart as c JOIN product as p where p.product_id = c.product_id AND c.customer_id=%s',(st.session_state['customer_id'],))
    data = c.fetchall()
    return data

def view_order():
    c.execute('SELECT * from orders WHERE customer_id=%s',(st.session_state['customer_id'],))
    data = c.fetchall()
    return data

def view_all_order():
    c.execute('SELECT order_id, product_id, order_status,customer_id from orders')
    data = c.fetchall()
    return data

def get_total():
    c.execute("SELECT SUM(p.price * c.quantity) AS total_cost FROM cart c JOIN product p ON c.product_id = p.product_id where c.customer_id = %s;", (st.session_state['customer_id'],))
    amount = c.fetchall()
    mydb.commit()
    integer_value = int(amount[0][0]) 
    return integer_value

def order(result):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    existing_ids = set()

    c.execute("SELECT order_id FROM orders")
    existing_orders = c.fetchall()

    for order in existing_orders:
        existing_ids.add(order[0])
    integer_value = get_total()    

    while True:
        new_order_id = random.randint(10000000, 99999999)  # Random 8-digit number
        if new_order_id not in existing_ids:
            for i in result:
                c.execute('INSERT INTO orders (order_id, customer_id, product_id, quantity, order_status, order_date) VALUES (%s, %s, %s, %s, %s, %s)', (new_order_id, st.session_state['customer_id'], i[0], i[6], 'out for delivery', formatted_date))
                mydb.commit()
            break

    c.execute('INSERT INTO payment (order_id, customer_id, payment_date, payment_type, amount) VALUES (%s, %s, %s, %s, %s)', (new_order_id, st.session_state['customer_id'], formatted_date, 'COD', integer_value))
    mydb.commit()

def login_user(email, password):
    c.execute("SELECT email, password, customer_id, role FROM customer WHERE email = %s", (email,))
    user = c.fetchone()
    mydb.commit()
    if user == None:
        c.execute("SELECT email, password, seller_id FROM seller WHERE email = %s", (email,))
        seller = c.fetchone()
        if seller and seller[1] == password:
            st.success("Login successful!")
            st.session_state['customer_id'] = seller[2]
            st.session_state['role'] = 'seller'
            return 'seller', seller[2]
        else:
            st.error("Invalid username or password")
    else:
        if user and user[1] == password:
            st.success("Login successful!")
            st.session_state['customer_id'] = user[2]
            st.session_state['role'] = user[3]
            return user[3], user[2]  # Return both role and customer_id
        else:
            st.error("Invalid username or password")

def register_user(email, password, role):
    try:
        c.execute("CALL AddNewCustomer(%s, %s, %s);", (email, password, role))
        mydb.commit()
        st.success("Registration successful!")
    except mysql.connector.Error as err:
        st.error(f"Failed to register: {err}")

def view_products(): 
    c.execute('SELECT p.product_id, p.seller_id, p.product_name, p.discount_coupon, p.size, p.price, p.quantity, p.brand, p.description, p.discount_id, CalculateAverageReview(p.product_id)  FROM product p')
    data = c.fetchall()
    return data

def seller_view_products(): 
    c.execute('SELECT p.product_id, p.seller_id, p.product_name, p.discount_coupon, p.size, p.price, p.quantity, p.brand, p.description, p.discount_id, CalculateAverageReview(p.product_id)  FROM product p where p.seller_id = %s',(st.session_state['customer_id'],))
    data = c.fetchall()
    return data


