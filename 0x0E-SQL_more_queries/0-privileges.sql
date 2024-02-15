-- script that grants privileges
-- of users_0d_1 and 2.
SELECT *
FROM mysql.user
WHERE user IN ("user_0d_1", "user_0d_2");
