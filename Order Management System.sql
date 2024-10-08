create database OrderManagementSystem;
use OrderManagementSystem;

create table Product(
product_id INT PRIMARY KEY,
product_name VARCHAR(20) NOT NULL,
description VARCHAR(30) NOT NULL,
price decimal NOT NULL,
quantity_in_stock INT NOT NULL,
type VARCHAR(15) );

CREATE TABLE Electronics (
product_id int primary key,
brand VARCHAR(30),
warranty_period INT,
FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE
);


create table Clothing(
product_id int primary key,
size varchar(50),
color varchar(10),
FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE
);



create table UserDetail(
user_id INT PRIMARY KEY,
username VARCHAR(20) NOT NULL,
password VARCHAR(10) NOT NULL,
role VARCHAR(10) NOT NULL);

CREATE TABLE Orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES UserDetail(user_id),
    order_date DATETIME DEFAULT GETDATE()
);

drop table Orders;

CREATE TABLE OrderProduct (
    orderDetailId INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES Orders(order_id),
    product_id INT FOREIGN KEY REFERENCES Product(product_id),
    quantity INT NOT NULL
);
