-- Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
-- Return the result table in any order.
-- SCHEMA

BEGIN TRANSACTION; 

Create table If Not Exists Products (product_id int, store1 int, store2 int, store3 int);
insert into Products (product_id, store1, store2, store3) values ('0', '95', '100', '105');
insert into Products (product_id, store1, store2, store3) values ('1', '70', NULL, '80');

COMMIT; 