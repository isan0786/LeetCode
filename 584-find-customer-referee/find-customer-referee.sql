# Write your MySQL query statement below
Select name from customer where referee_id <> 2 OR COALESCE(referee_id,0)=0