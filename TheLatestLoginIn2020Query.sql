-- Write an SQL query to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.
-- Return the result table in any order.
-- QUERY (Works with TheLatestLoginIn2020Schema.sql and TheLatestLoginIn2020.db)

SELECT user_id, max(time_stamp) as last_stamp 
FROM Logins
WHERE time_stamp like "%2020%"
GROUP BY user_id