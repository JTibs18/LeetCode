-- Write an SQL query to find the employees who earn more than their managers.
-- Return the result table in any order.
-- The query result format is in the following example.
-- QUERY (Works with EmployeesEarningMoreThanTheirManagersQuery.sql and EmployeesEarningMoreThanTheirManagersQuery.db)

SELECT Employee.name as Employee
FROM Employee 
JOIN Employee as Manager 
ON Manager.id=Employee.managerId
WHERE Employee.salary > Manager.salary

