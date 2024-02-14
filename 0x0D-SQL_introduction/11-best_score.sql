--list * scores where score >= 10
--record in orber by desc
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
