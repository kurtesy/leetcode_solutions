# Write your MySQL query statement below
SELECT c.name as customers
FROM Customers AS c
WHERE id NOT IN (SELECT customerId from Orders);