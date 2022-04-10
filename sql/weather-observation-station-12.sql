SELECT DISTINCT CITY 
FROM STATION 
WHERE NOT (city LIKE '%A' OR city LIKE '%E' OR city LIKE '%I' OR city LIKE '%O' OR city LIKE '%U')
AND NOT (city LIKE 'A%' OR city LIKE 'E%' OR city LIKE 'I%' OR city LIKE 'O%' OR city LIKE 'U%');