-- updates a column based on another columd in db
UPDATE `second_table`
SET
`score` = 10
WHERE `second_table`.`name` = "Bob";
