-- Each node in the tree can be one of three types:
-- "Leaf": if the node is a leaf node.
-- "Root": if the node is the root of the tree.
-- "Inner": If the node is neither a leaf node nor a root node.
-- Write an SQL query to report the type of each node in the tree.
-- Return the result table in any order.
-- QUERY (Works with TreeNodeSchema.sql and TreeNode.db)
-- Help from Phind.com: https://www.phind.com/search?cache=1fd07ee9-4f28-4063-a084-8cd7fc6257cd

SELECT id, 
CASE 
    WHEN p_id IS NULL THEN 'Root'
    WHEN (SELECT COUNT(*) FROM Tree WHERE p_id = t.id) = 0 THEN 'Leaf'
    ELSE 'Inner' 
END AS type 
FROM Tree t