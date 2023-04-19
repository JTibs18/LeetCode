-- Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.
-- Return the result table ordered by user_id.
-- QUERY (Works with FixNamesTableSchema.sql and FixNamesTable.db)

-- FOR SQLITE3
SELECT user_id, UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2, LENGTH(name) - 1)) as name
FROM Users 
ORDER BY user_id 

-- FOR MySQL 
SELECT user_id, CONCAT(UPPER(substr(name,1,1)),LOWER(substr(name,2))) as name 
FROM users  
ORDER BY user_id