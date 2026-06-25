-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM Orders;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM Orders;

-- Top Customers
SELECT Customer_Name,
       SUM(Sales) AS Revenue
FROM Orders
GROUP BY Customer_Name
ORDER BY Revenue DESC
LIMIT 10;

-- Top Products
SELECT Product_Name,
       SUM(Sales) AS Revenue
FROM Orders
GROUP BY Product_Name
ORDER BY Revenue DESC
LIMIT 10;

-- Top States
SELECT State,
       SUM(Sales) AS Revenue
FROM Orders
GROUP BY State
ORDER BY Revenue DESC
LIMIT 10;