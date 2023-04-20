-- Write a SQL query to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.
-- Return the result table sorted in any order.
-- QUERY (Works with CustomerWhoVisitedButDidNotMakeAnyTransactionsSchema.sql and CustomerWhoVisitedButDidNotMakeAnyTransactions.db)

SELECT Visits.customer_id, count(Visits.customer_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.amount IS NULL
GROUP BY Visits.customer_id