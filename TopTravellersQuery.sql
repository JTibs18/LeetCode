-- Write an SQL query to report the distance traveled by each user.
-- Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.
-- QUERY (Works with TopTravellersSchema.sql and TopTravellers.db)

SELECT Users.name, IFNULL(sum(Rides.distance), 0) AS travelled_distance
FROM Users
LEFT JOIN Rides
ON Users.id = Rides.user_id
GROUP BY Users.id
ORDER BY sum(Rides.distance) DESC, Users.name 