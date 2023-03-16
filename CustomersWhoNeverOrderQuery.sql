-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
-- The query result format is in the following example.
-- QUERY (Works with CustomersWhoNeverOrderSchemal.sql and CustomersWhoNeverOrder.db)

Select Customers.name as Customers
from Customers left outer join Orders on Customers.id = Orders.customerId  
Where Orders.id is null