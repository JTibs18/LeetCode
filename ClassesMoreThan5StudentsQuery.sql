-- Write an SQL query to report all the classes that have at least five students.
-- Return the result table in any order.
-- The query result format is in the following example.
-- QUERY (Works with ClassesMoreThan5StudentsSchema.sql and ClassesMoreThan5StudentsSchema.db)

 SELECT class 
 FROM Courses
 GROUP BY class
 HAVING count(class) >= 5 