-- Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.
-- Note that you must write a single update statement, do not write any select statement for this problem.
-- QUERY (Works with SwapSalarySchema.sql and SwapSalary.db)

UPDATE Salary
SET sex =
    CASE 
        WHEN sex = 'f'
        THEN 'm'
        WHEN sex = 'm'
        THEN 'f'
    END