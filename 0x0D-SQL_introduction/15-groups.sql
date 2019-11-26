-- display number of records with same value in a column in db
SELECT score,
COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
