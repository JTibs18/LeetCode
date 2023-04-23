-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
-- Return the result table in any order.
-- Query (Works with RisingTemperatureSchema.sql and RisingTemperature.db)

-- MySQL
SELECT w1.id 
FROM Weather w1
JOIN Weather w2
ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY 
WHERE w1.temperature > w2.temperature 

-- Sqlite3
SELECT w1.Id
FROM Weather w1
JOIN Weather w2
ON w1.RecordDate = date(w2.RecordDate, '+1 day')
WHERE w1.Temperature > w2.Temperature;