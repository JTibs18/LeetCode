-- Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.
-- Return the result table in any order.
-- QUERY (Works with MarketAnalysisISchema.sql and MarketAnalysisI.db)
-- With help from: https://leetcode.com/problems/market-analysis-i/solutions/3280910/mysql-solution/

SELECT user_id as buyer_id, Users.join_date, IFNULL(count(order_id), 0) as orders_in_2019
FROM Users
LEFT JOIN Orders 
ON Users.user_id = Orders.buyer_id
AND order_date >= '2019-01-01' AND order_date <= '2019-12-31' 
GROUP BY user_id