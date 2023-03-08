-- Write an SQL query that will, for each date_id and make_name, return the number of distinct lead_id's and distinct partner_id's.
-- Return the result table in any order.
-- The query result format is in the following example.
-- QUERY (Works with DailyLeadsAndPartnersSchema.sql and DailyLeadsAndPartners.db)

SELECT date_id, make_name, count(DISTINCT lead_id) as unique_leads, count(DISTINCT partner_id) as unique_partners 
From DailySales
GROUP BY date_id, make_name