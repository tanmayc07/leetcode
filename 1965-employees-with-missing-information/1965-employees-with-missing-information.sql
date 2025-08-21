-- Write your PostgreSQL query statement below
SELECT employee_id
FROM Employees e
FULL OUTER JOIN Salaries s
USING (employee_id)
WHERE name IS null OR salary IS null
ORDER BY employee_id;