-- select max from group and display both columns
SELECT state,
MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
