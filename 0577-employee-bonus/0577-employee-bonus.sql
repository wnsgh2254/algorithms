SELECT E.name,B.bonus 
FROM Employee E 
LEFT JOIN Bonus B 
ON E.empID = B.empID
WHERE bonus < 1000 OR Bonus IS NULL ;