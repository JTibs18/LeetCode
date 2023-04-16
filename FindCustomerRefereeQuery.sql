-- Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
-- Return the result table in any order.
-- QUERY (Works with FindCustomerRefereeSchema.sql and FindCustomerReferee.db)

SELECT Customer.name
FROM Customer 
WHERE Customer.referee_id != 2 or customer.referee_id is null