-- Write an SQL query that will, for each user, return the number of followers.
-- Return the result table ordered by user_id in ascending order.
-- QUERY (Works with FindFollowersCountSchema.sql and FindFollowersCount.db)

SELECT user_id, count(*) as followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id