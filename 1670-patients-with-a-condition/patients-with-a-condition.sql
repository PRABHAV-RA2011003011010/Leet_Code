# Write your MySQL query statement below
select * from patients where conditions regexp '^DIAB1' or conditions like '% DIAB1%'