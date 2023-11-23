-- Write a solution to find the ids of products that are both low fat and recyclable.
-- Return the result table in any order.
-- SCHEMA

BEGIN TRANSACTION;

DROP TABLE IF EXISTS Products;

Create table If Not Exists Products (product_id int, low_fats varchar(255), recyclable varchar(255));

insert into Products (product_id, low_fats, recyclable) values ('0', 'Y', 'N');
insert into Products (product_id, low_fats, recyclable) values ('1', 'Y', 'Y');
insert into Products (product_id, low_fats, recyclable) values ('2', 'N', 'Y');
insert into Products (product_id, low_fats, recyclable) values ('3', 'Y', 'Y');
insert into Products (product_id, low_fats, recyclable) values ('4', 'N', 'N');

COMMIT; 