-- Write an SQL query to find employees who have the highest salary in each of the departments.
-- Return the result table in any order.
-- The query result format is in the following example.
-- QUERY (Works with DepartmentHighestSalaryQuery.sql and DepartmentHighestSalary.db)

SELECT Department.name as Department, Employee.name as Employee, Employee.salary as Salary 
FROM Employee join Department on Employee.departmentId = Department.id 
WHERE (departmentId, salary) IN 
(SELECT departmentId, MAX(salary) from Employee
GROUP BY departmentId) 
