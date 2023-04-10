-- A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
-- Write an SQL query to find the employees who are high earners in each of the departments.
-- Return the result table in any order.
-- QUERY (Works with DepartmentTopThreeSalariesSchema.sql and DepartmentTopThreeSalaries.db)

-- help from: https://leetcode.com/problems/department-top-three-salaries/solutions/3214925/185-solution-with-step-by-step-explanation/

SELECT d.Name as Department, e.Name as Employee, e.Salary as Salary
FROM Department d, Employee e 
WHERE (
    SELECT COUNT(DISTINCT Salary)
    FROM Employee
    Where Salary > e.Salary and DepartmentId = d.Id)
< 3 AND e.DepartmentId = d.id
ORDER BY d.id, e.salary DESC 