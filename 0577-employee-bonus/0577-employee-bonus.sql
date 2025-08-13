-- Write your PostgreSQL query statement below
SELECT name, bonus
FROM Employee e
LEFT JOIN Bonus b
USING (empId)
WHERE b.bonus < 1000 OR b.bonus IS NULL;