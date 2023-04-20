-- Write an SQL query to find all the authors that viewed at least one of their own articles.
-- Return the result table sorted by id in ascending order.
-- QUERY (Works with ArticleViewsISchema.sql and ArticleViewsI.db)

SELECT DISTINCT author_id as id
FROM Views 
WHERE author_id = viewer_id
ORDER BY author_id