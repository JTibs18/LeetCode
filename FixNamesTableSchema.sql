-- Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.
-- Return the result table ordered by user_id.
-- SCHEMA 

BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Users;
Create table If Not Exists Users (user_id int, name varchar(40));

insert into Users (user_id, name) values ('1', 'aLice');
insert into Users (user_id, name) values ('2', 'bOB');

COMMIT; 
