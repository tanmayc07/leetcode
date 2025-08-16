-- Write your PostgreSQL query statement below
SELECT MAX(num) FILTER(WHERE cnt = 1) AS num
FROM (
    SELECT num, COUNT(*) AS cnt
    FROM MyNumbers
    GROUP BY num
) t;