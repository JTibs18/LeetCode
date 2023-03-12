-- Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.
-- Return the result table ordered by id in ascending order.
-- The query result format is in the following example.
-- SCHEMA

BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Seat; 

Create table If Not Exists Seat (id int, student varchar(255));

insert into Seat (id, student) values ('1', 'Abbot');
insert into Seat (id, student) values ('2', 'Doris');
insert into Seat (id, student) values ('3', 'Emerson');
insert into Seat (id, student) values ('4', 'Green');
insert into Seat (id, student) values ('5', 'Jeames');


COMMIT; 