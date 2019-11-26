-- display rows with no null value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL;
