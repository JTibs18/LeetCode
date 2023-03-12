-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.
-- After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
-- The query result format is in the following example.
-- SCHEMA

BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Person; 

Create table If Not Exists Person (Id int, Email varchar(255)); 
insert into Person (id, email) values ('1', 'abc@efg.com');
insert into Person (id, email) values ('2', 'test@gmail.com');
insert into Person (id, email) values ('3', 'abcd@efg.com');

COMMIT; 