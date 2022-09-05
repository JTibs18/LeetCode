-- Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".
-- Return the result table in any order.
-- QUERY (Works with SalesPersonSchema.sql and SalesPerson.db)

SELECT SalesPerson.name
FROM SalesPerson
LEFT JOIN Orders
ON Orders.sales_id=SalesPerson.sales_id
LEFT JOIN Company
ON Orders.com_id=company.com_id
GROUP BY SalesPerson.name
HAVING SUM(company.name = "RED") = 0 OR COUNT(orders.order_id) = 0;
