-- creates a table
-- fill description of table
-- add records
CREATE TABLE IF NOT EXISTS second_table (id INT);
ALTER TABLE second_table ADD name VARCHAR(256);
ALTER TABLE second_table ADD score INT;
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
