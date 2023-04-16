-- Write an SQL query to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
-- Return the result table ordered by visit_date in ascending order.
-- QUERY (Works with HumanTrafficOfStadiumSchema.sql and HumanTrafficOfStadium.db)

-- Inspired by https://leetcode.com/problems/human-traffic-of-stadium/solutions/700476/mysql-solution/

with stadiumTable as (SELECT *, 
                        id - row_number() OVER(ORDER BY id) as grp
                        FROM Stadium 
                        where people >= 100)

SELECT stadiumTable.id, stadiumTable.visit_date, stadiumTable.people 
FROM stadiumTable
WHERE grp in (SELECT grp from stadiumTable 
                GROUP BY grp having count(*) >= 3)