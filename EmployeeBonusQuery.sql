-- Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.
-- Return the result table in any order.
-- The query result format is in the following example.
-- QUERY (Works with EmployeeBonusSchema.sql and EmployeeBonus.db)
 
 SELECT Employee.name, Bonus.bonus 
 FROM Employee 
 LEFT JOIN Bonus 
 ON Employee.empId = Bonus.empId
 WHERE Bonus.bonus < 1000 or Bonus.bonus is null 