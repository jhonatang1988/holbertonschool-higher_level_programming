-- display row and average row ordered by average row in db
SELECT city,
AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
