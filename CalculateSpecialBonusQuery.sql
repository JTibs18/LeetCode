-- Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
-- Return the result table ordered by employee_id.
-- QUERY (Works with CalculateSpecialBonusSchema.sql and CalculateSpecialBonus.db)

SELECT Employees.employee_id, 
CASE WHEN Employees.employee_id % 2 = 0 or name LIKE "M%"
    THEN 0
    ELSE salary
    END AS bonus
FROM Employees
ORDER BY Employees.employee_id