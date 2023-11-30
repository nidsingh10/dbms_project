DROP DATABASE mini_project;
create database if not exists mini_project;
use mini_project;



SET SQL_SAFE_UPDATES = 0;

# CUSTOMER
create table if not exists customer (
    customer_id int auto_increment,
    email varchar(50) not null,
	password varchar(100) not null,
    role enum('admin', 'user'),
    primary key (customer_id)
);

# SELLER
create table if not exists seller (
    seller_id varchar(10) not null,
    name varchar(20) not null,
    email varchar(50) not null,
    contact_no varchar(15) not null,
    address varchar(50) not null,
    primary key (seller_id)
);

# SELLER_NUMBER
create table if not exists seller_phone_num (
    phone_num varchar(10) not null,
    seller_id varchar(10) not null,
    primary key (phone_num, seller_id),
    foreign key (seller_id) references seller(seller_id) on delete cascade
);
# DISCOUNT
create table if not exists discount (
    discount_id varchar(10) not null,
    discount_amount numeric(5),
    discount_coupon varchar(15),
    primary key (discount_id)
);

# PRODUCT
create table if not exists product (
    product_id varchar(10) not null,
    seller_id varchar(10),
    product_name varchar(50) not null,
    discount_coupon varchar(15),
    size varchar(10) not null,
    price numeric(10, 2) not null,
    quantity integer not null,
    brand varchar(30) not null,
    description text,
    discount_id varchar(10),
    primary key (product_id),
    foreign key (seller_id) references seller(seller_id) on delete set null,
    foreign key (discount_id) references discount(discount_id) on delete set null
);

# CART
create table if not exists cart (
    customer_id int not null,
    product_id varchar(10) not null,
    quantity int default 1,
    primary key (product_id, customer_id),
    foreign key (product_id) references product(product_id),
    foreign key (customer_id) references customer(customer_id)
);

# ORDER
create table if not exists orders (
    order_id int not null,
    customer_id int,
    product_id varchar(10) not null,
    quantity int default 1,
    order_status enum('out for delivery', 'delivered'),
    order_date date not null,
    primary key (order_id, customer_id, product_id),
    foreign key (product_id) references product(product_id),
    foreign key (customer_id) references customer(customer_id)
);

# PAYMENT
create table if not exists payment (
    payment_id int auto_increment,
    order_id int,
    customer_id int,
    payment_date date not null,
    payment_type enum('UPI', 'COD', "Credit Card", "Net Banking"),
    amount int,
    primary key (payment_id),
    foreign key (customer_id) references customer(customer_id),
    foreign key (order_id) references orders(order_id)
);

# CATEGORIES
create table if not exists categories (
    product_id varchar(10) not null,
    category_id varchar(10) not null,
    category_name varchar(30) not null,
    primary key (product_id, category_id),
    foreign key (product_id) references product(product_id)
);

# SHIPMENT
create table if not exists shipment (
    shipment_id varchar(10) not null,
    shipping_details text,
    invoices varchar(50) not null,
    primary key (shipment_id)
);

# REVIEWS
create table if not exists reviews (
    review_id varchar(12) not null,
    product_id varchar(10) not null,
    customer_id int not null,
    review int,
    review_date date,
    primary key (review_id),
    foreign key (product_id) references product(product_id),
    foreign key (customer_id) references customer(customer_id)
);

#POPULATING THE TABLES

#SELLER
INSERT INTO seller (seller_id, name, email, contact_no, address) VALUES
('SELL001', 'Fashion Empire', 'info@fashionempire.com', '1234567890', '123 Fashion Ave'),
('SELL002', 'TrendyWear Co.', 'contact@trendywear.com', '2345678901', '456 Style St'),
('SELL003', 'Chic Trends', 'support@chictrends.com', '3456789012', '789 Fashion Blvd'),
('SELL004', 'StyleHub Inc.', 'info@stylehub.com', '4567890123', '567 Trendy Rd'),
('SELL005', 'Fashionista World', 'hello@fashionista.com', '5678901234', '901 Glam St'),
('SELL006', 'TrendyThreads', 'info@trendythreads.com', '6789012345', '345 Vogue Ave'),
('SELL007', 'ModishWardrobe', 'support@modishwardrobe.com', '7890123456', '678 Stylish St'),
('SELL008', 'UrbanStyle Co.', 'contact@urbanstyle.com', '8901234567', '234 Chic Blvd'),
('SELL009', 'Glamorous Attire', 'info@glamorous.com', '9012345678', '789 Trendy Rd'),
('SELL010', 'FashionFusion', 'hello@fashionfusion.com', '1234567891', '456 Vogue Ave');

#SELLER_NUMBER
INSERT INTO seller_phone_num (phone_num, seller_id) VALUES
('1234567890', 'SELL001'),
('2345678901', 'SELL002'),
('3456789012', 'SELL003'),
('4567890123', 'SELL004'),
('5678901234', 'SELL005'),
('6789012345', 'SELL006'),
('7890123456', 'SELL007'),
('8901234567', 'SELL008'),
('9012345678', 'SELL009'),
('1234567891', 'SELL010');


#DISCOUNT
INSERT INTO discount (discount_id, discount_amount, discount_coupon) VALUES
('DISC001', 10, 'SALE10'),
('DISC002', 15, 'TRENDY15'),
('DISC003', 20, 'CASUAL20'),
('DISC004', 12, 'SUMMER12'),
('DISC005', 25, 'SPORTS25'),
('DISC006', 18, 'FASHION18'),
('DISC007', 30, 'WINTER30'),
('DISC008', 22, 'COZY22'),
('DISC009', 10, 'CLASSIC10'),
('DISC010', 17, 'FORMAL17');

UPDATE product
SET discount_coupon = (
    SELECT discount_coupon
    FROM discount
    WHERE discount.discount_id = product.discount_id
);

#PRODUCT
INSERT INTO product (product_id, seller_id, product_name, discount_coupon, size, price, quantity, brand, description, discount_id) VALUES
('PROD001', 'SELL001', 'T-Shirt', 'SALE10', 'M', 19.99, 50, 'Brand A', 'Comfortable t-shirt', 'DISC001'),
('PROD002', 'SELL002', 'Dress', 'TRENDY15', 'S', 39.99, 30, 'Brand B', 'Elegant dress', 'DISC002'),
('PROD003', 'SELL003', 'Jeans', 'CASUAL20', 'L', 29.99, 40, 'Brand C', 'Classic jeans', 'DISC003'),
('PROD004', 'SELL004', 'Sneakers', 'SPORTS25', '9', 49.99, 60, 'Brand D', 'Sporty sneakers', 'DISC005'),
('PROD005', 'SELL005', 'Coat', 'WINTER30', 'M', 79.99, 20, 'Brand E', 'Warm winter coat', 'DISC007'),
('PROD006', 'SELL006', 'Scarf', 'FASHION18', 'One Size', 15.99, 70, 'Brand F', 'Stylish scarf', 'DISC006'),
('PROD007', 'SELL007', 'Hat', 'SUMMER12', 'One Size', 12.99, 80, 'Brand G', 'Casual hat', 'DISC004'),
('PROD008', 'SELL008', 'Gloves', 'WINTER30', 'One Size', 9.99, 100, 'Brand H', 'Winter gloves', 'DISC007'),
('PROD009', 'SELL009', 'Shirt', 'CLASSIC10', 'L', 22.99, 45, 'Brand I', 'Formal shirt', 'DISC009'),
('PROD010', 'SELL010', 'Suit', 'FORMAL17', 'XL', 199.99, 10, 'Brand J', 'Elegant suit', 'DISC010');

#CATEGORIES
INSERT INTO categories (product_id, category_id, category_name) VALUES
('PROD001', 'CAT001', 'Shirts'),
('PROD001', 'CAT002', 'Casual Wear'),
('PROD002', 'CAT003', 'Dresses'),
('PROD002', 'CAT004', 'Formal Wear'),
('PROD003', 'CAT001', 'Shirts'),
('PROD003', 'CAT005', 'Jeans'),
('PROD004', 'CAT006', 'Shoes'),
('PROD004', 'CAT007', 'Sneakers'),
('PROD005', 'CAT008', 'Accessories'),
('PROD005', 'CAT009', 'Bags');

#QUERIES
#PROCEDURES
DELIMITER //

CREATE PROCEDURE AddNewCustomer(
    IN email_param VARCHAR(50),
    IN password_param VARCHAR(100),
    IN role_param ENUM('admin', 'user')
)
BEGIN
    INSERT INTO customer (email, password, role)
    VALUES (email_param, password_param, role_param);
END //

DELIMITER ;

#TRIGGERS
DELIMITER //

CREATE TRIGGER delete_cart_elements
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DELETE FROM cart WHERE customer_id = NEW.customer_id AND product_id = NEW.product_id;
END;
//

DELIMITER ;



SET GLOBAL log_bin_trust_function_creators = 1;

INSERT INTO reviews (review_id, product_id, customer_id, review, review_date)
VALUES
('R001', 'PROD004', 1, 4, '2023-11-01'),
('R002', 'PROD007', 1, 5, '2023-11-02'),
('R003', 'PROD003', 1, 4, '2023-11-01'),
('R004', 'PROD002', 1, 5, '2023-11-02'),
('R005', 'PROD001', 1, 3, '2023-11-03'),
('R006', 'PROD006', 1, 4, '2023-11-01'),
('R007', 'PROD007', 1, 5, '2023-11-02'),
('R008', 'PROD008', 1, 3, '2023-11-03'),
('R009', 'PROD005', 1, 3, '2023-11-03'),
('R0010', 'PROD001', 1, 4, '2023-11-03'),
('R0011', 'PROD005', 1, 3, '2023-11-03');


#FUNCTION
DELIMITER //

CREATE FUNCTION CalculateAverageReview(productId varchar(10))
RETURNS DECIMAL(3,2)
BEGIN
    DECLARE avgReview DECIMAL(3,2);
    
    SELECT AVG(review) INTO avgReview
    FROM reviews
    WHERE product_id = productId;
    
    RETURN IFNULL(avgReview, 0); -- Return 0 if there are no reviews for the product
END //

DELIMITER ;

select CalculateAverageReview(product_id) from product;

SELECT p.product_id, p.seller_id, p.product_name, p.discount_coupon, p.size, p.price, p.quantity, p.brand, p.description, p.discount_id, CalculateAverageReview(p.product_id)  FROM product p;

#JOINS
# 1.Finding Products and Their Categories Using Joins:
select p.product_id, p.product_name, c.category_id, c.category_name
from product p
inner join categories c on p.product_id = c.product_id;

# 2.Matching Customer Orders with Their Payments:
select o.order_id, o.order_date, p.payment_id, p.payment_date, p.total_amount
from orders o
inner join payment p on o.order_id = p.order_id;

#Set Operations:
# 1.UNION
select product_id, product_name from product union select product_id, product_name from orders;

#Aggregate Functions:
# 1.Calculating Total Payment Amount by Payment Type:
select payment_type, sum(total_amount) as total_payment
from payment
group by payment_type;

# 2.Counting the Number of Reviews per Product:
select product_id, count(review_id) as review_count
from reviews
group by product_id;

#Nested and Complex Queries:
# 1.Subquery to Find Maximum Quantity Product:
select product_id, product_name, quantity
from product
where quantity = (select max(quantity) from product);

# 2.Query to Find Customers Who Made Payments with Credit Cards:
select customer_id, payment_id
from payment
where payment_type = 'Credit Card';




#Function -> to find the total cart amount
delimiter //
create function cart_amount(p_cart_id varchar(7)) returns numeric
reads sql data
begin
    declare total_amount numeric(12, 2);
    select sum(price) into total_amount
    from product
    inner join payment on product.product_id = payment.product_id
    where payment.cart_id = p_cart_id;
    return total_amount;
end//
delimiter ;

#colour&categories(shirt,tshirt)
SELECT p.product_id,p.seller_id,p.product_name,p.discount_coupon,p.size,p.price,c.quantity,p.brand,p.description FROM cart as c JOIN product as p where p.product_id = c.product_id;
select * from cart;

select * from payment;

SELECT SUM(p.price * c.quantity) AS total_cost FROM cart c JOIN product p ON c.product_id = p.product_id where c.customer_id = 1;