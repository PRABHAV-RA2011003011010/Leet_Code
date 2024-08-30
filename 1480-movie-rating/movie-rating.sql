# Write your MySQL query statement below
(select u.name as results from
(select user_id, count(*) as num from MovieRating group by user_id) as m
left join
users u on m.user_id=u.user_id
order by num desc,u.name limit 1)

union all

(select title as results from (
select m.title, avg(rating) as havg from
(select * from MovieRating where created_at>'2020-02-00' and created_at<'2020-03-00') as k
left join
movies m on k.movie_id=m.movie_id

group by k.movie_id order by havg desc,m.title 
) as final limit 1)

