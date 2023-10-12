-- use oracle-pseudo-column row id
-- add each column within group_by-function

-- test
DELETE FROM your_table
WHERE rowid not in
(SELECT MIN(rowid)
FROM your_table
GROUP BY column1, column2, column3);
