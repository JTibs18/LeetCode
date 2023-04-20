-- Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:
-- The employee's name is missing, or
-- The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.
-- QUERY (Works with EmployeesWithMissingInformationSchema.sql and EmployeesWithMissingInformation.db)
-- References: https://www.sqlitetutorial.net/sqlite-full-outer-join/

SELECT e.employee_id
FROM Employees e
LEFT JOIN Salaries s
USING (employee_id)
WHERE s.salary IS NULL
UNION ALL 
SELECT s.employee_id
FROM Salaries s
LEFT JOIN Employees e
USING (employee_id)
WHERE e.employee_id IS NULL 
ORDER BY employee_id