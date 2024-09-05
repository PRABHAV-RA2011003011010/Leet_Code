# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary 
from employee e left join department d on e.departmentid=d.id
where 3 > (select count(distinct(salary)) from employee e1 where e1.salary>e.salary and e.departmentid=e1.departmentid )