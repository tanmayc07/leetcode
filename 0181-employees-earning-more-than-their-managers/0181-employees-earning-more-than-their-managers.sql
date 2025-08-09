-- Write your PostgreSQL query statement below
SELECT e.name as "Employee"
FROM Employee as e 
INNER JOIN Employee as p
ON e.managerId = p.id
WHERE e.salary > p.salary;