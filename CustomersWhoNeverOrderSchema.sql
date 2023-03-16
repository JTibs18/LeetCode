-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
-- The query result format is in the following example.
-- SCHEMA 

BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Customers; 
DROP TABLE IF EXISTS Orders; 

Create table If Not Exists Customers (id int, name varchar(255));
Create table If Not Exists Orders (id int, customerId int);

insert into Customers (id, name) values ('1', 'Joe');
insert into Customers (id, name) values ('2', 'Henry');
insert into Customers (id, name) values ('3', 'Sam');
insert into Customers (id, name) values ('4', 'Max');

insert into Orders (id, customerId) values ('1', '3');
insert into Orders (id, customerId) values ('2', '1');

COMMIT; 