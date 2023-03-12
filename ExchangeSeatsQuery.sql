-- Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.
-- Return the result table ordered by id in ascending order.
-- The query result format is in the following example.
-- QUERY (Works with ExchangeSeatsSchema.sql and ExchangeSeatsSchema.db)

SELECT  
CASE 
    WHEN id % 2 = 0 THEN id - 1 
    WHEN id = (select max(id) from Seat) THEN id 
    ELSE id + 1 
END as id, 
student 
FROM Seat
ORDER BY id