-- A script that creats a second table with values
CREATE TABLE IF NOT EXISTS `second_table`(`id` INT, `name` VARCHAR(256), `score` INT)
INSERT INTO `second_table`
 VALUES ((1, 2, 3, 4), ("John", "Alex", "Bob", "George"), (10, 3, 14,8));
