-- Write your PostgreSQL query statement below
SELECT product_name, year, price
FROM Sales s
INNER JOIN Product p
USING (product_id);
