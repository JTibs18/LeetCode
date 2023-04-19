-- Write an SQL query to find for each date the number of different products sold and their names.
-- The sold products names for each date should be sorted lexicographically.
-- Return the result table ordered by sell_date.
-- QUERY (Works with GroupSoldProductsByTheDateSchema.sql and GroupSoldProductsByTheDate.db)

SELECT sell_date, count(DISTINCT product) as num_sold, GROUP_CONCAT(DISTINCT product) as products
FROM Activities
GROUP BY sell_date