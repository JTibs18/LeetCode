-- Write an SQL query to report the first login date for each player.
-- Return the result table in any order.
-- QUERY (Works with GamePlayAnalysisISchema.sql and GamePlayAnalysisI.db)

SELECT player_id, min(event_date) as first_login 
FROM Activity
GROUP BY player_id