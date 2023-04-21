-- Write an SQL query that reports the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.
-- Return the result table in any order.
-- QUERY (Works with SalesAnalysisIIISchema.sql and SalesAnalysisIII.db)

SELECT Product.product_id, product_name
FROM Product
JOIN Sales 
ON Product.product_id = Sales.product_id
GROUP BY Sales.product_id 
HAVING max(Sales.sale_date) <= '2019-03-31' and min(Sales.sale_date) >= '2019-01-01'