-- Write an SQL query to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.
-- Return the result table in any order.
-- QUERY (Works with BankAccountSummaryIISchema.sql and BankAccountSummaryII.db)

SELECT name, SUM(Transactions.amount) as balance 
FROM Users
JOIN Transactions
ON Users.account = Transactions.account 
GROUP BY Users.account
HAVING SUM(Transactions.amount) > 10000