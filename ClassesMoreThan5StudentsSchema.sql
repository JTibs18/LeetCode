-- Write an SQL query to report all the classes that have at least five students.
-- Return the result table in any order.
-- The query result format is in the following example.
-- SCHEMACreate table If Not Exists Courses (student varchar(255), class varchar(255))

BEGIN TRANSACTION; 

DROP TABLE IF EXISTS Courses; 

Create table If Not Exists Courses (student varchar(255), class varchar(255));

insert into Courses (student, class) values ('A', 'Math');
insert into Courses (student, class) values ('B', 'English');
insert into Courses (student, class) values ('C', 'Math');
insert into Courses (student, class) values ('D', 'Biology');
insert into Courses (student, class) values ('E', 'Math');
insert into Courses (student, class) values ('F', 'Computer');
insert into Courses (student, class) values ('G', 'Math');
insert into Courses (student, class) values ('H', 'Math');
insert into Courses (student, class) values ('I', 'Math');

COMMIT; 