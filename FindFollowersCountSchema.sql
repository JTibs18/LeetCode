-- Write an SQL query that will, for each user, return the number of followers.
-- Return the result table ordered by user_id in ascending order.
-- SCHEMA 

BEGIN TRANSACTION; 

Create table If Not Exists Followers(user_id int, follower_id int);
insert into Followers (user_id, follower_id) values ('0', '1');
insert into Followers (user_id, follower_id) values ('1', '0');
insert into Followers (user_id, follower_id) values ('2', '0');
insert into Followers (user_id, follower_id) values ('2', '1');

COMMIT; 