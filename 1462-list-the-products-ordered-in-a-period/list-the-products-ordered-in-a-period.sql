# Write your MySQL query statement below
select p.product_name,sum(unit) as unit from
(select * from orders where order_date>'2020-02-00' and order_date<'2020-03-01') as m
left join
products p on m.product_id=p.product_id
group by m.product_id having sum(unit)>99
