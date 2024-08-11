# Write your MySQL query statement below
SELECT w2.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate = DATE_sub(w2.recordDate, INTERVAL 1 DAY) where w1.temperature<w2.temperature