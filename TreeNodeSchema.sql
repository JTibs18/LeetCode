-- Each node in the tree can be one of three types:
-- "Leaf": if the node is a leaf node.
-- "Root": if the node is the root of the tree.
-- "Inner": If the node is neither a leaf node nor a root node.
-- Write an SQL query to report the type of each node in the tree.
-- Return the result table in any order.
-- SCHEMA

BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Tree; 

Create table If Not Exists Tree (id int, p_id int);
insert into Tree (id, p_id) values ('1', 'None');
insert into Tree (id, p_id) values ('2', '1');
insert into Tree (id, p_id) values ('3', '1');
insert into Tree (id, p_id) values ('4', '2');
insert into Tree (id, p_id) values ('5', '2');

COMMIT; 