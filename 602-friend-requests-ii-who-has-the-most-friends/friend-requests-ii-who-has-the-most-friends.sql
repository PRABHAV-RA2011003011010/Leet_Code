# Write your MySQL query statement below
select total as id,count(*) as num from
((select requester_id as total from RequestAccepted) 
union all
(select accepter_id as total  from RequestAccepted)) as m 
group by total order by num desc
limit 1
