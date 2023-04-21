-- Write a SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
-- Return the result table in any order.
-- Query (Works with ActorsAndDirectorsWhoCooperatedAtLeastThreeTimesSchema.sql and ActorsAndDirectorsWhoCooperatedAtLeastThreeTimes.db)

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id 
HAVING count(actor_id) >= 3