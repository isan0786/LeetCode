# Write your MySQL query statement below
SELECT DISTINCT author_id as id
FROM views
where author_id = viewer_id
order by id