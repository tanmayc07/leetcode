-- Write your PostgreSQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e
INNER JOIN Department d
ON e.departmentId = d.id
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = d.id
)
ORDER BY e.salary DESC;