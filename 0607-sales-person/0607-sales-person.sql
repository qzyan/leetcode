# Write your MySQL query statement below
SELECT name 
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id 
    FROM Orders
    LEFT JOIN Company
    ON Company.com_id = Orders.com_id
    WHERE Company.name = 'RED'
)
