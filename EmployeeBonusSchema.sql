-- Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.
-- Return the result table in any order.
-- The query result format is in the following example.
-- SCHEMA 

BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Employee; 
DROP TABLE IF EXISTS Bonus; 

Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int);
Create table If Not Exists Bonus (empId int, bonus int);
insert into Employee (empId, name, supervisor, salary) values ('3', 'Brad', 'None', '4000');
insert into Employee (empId, name, supervisor, salary) values ('1', 'John', '3', '1000');
insert into Employee (empId, name, supervisor, salary) values ('2', 'Dan', '3', '2000');
insert into Employee (empId, name, supervisor, salary) values ('4', 'Thomas', '3', '4000');
insert into Bonus (empId, bonus) values ('2', '500');
insert into Bonus (empId, bonus) values ('4', '2000');

COMMIT