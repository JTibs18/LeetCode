-- Write an SQL query to find employees who have the highest salary in each of the departments.
-- Return the result table in any order.
-- The query result format is in the following example.
-- SCHEMA
 
BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Employee; 
DROP TABLE IF EXISTS Department; 

Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));

insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Jim', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('3', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('5', 'Max', '90000', '1');

insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');

COMMIT; 