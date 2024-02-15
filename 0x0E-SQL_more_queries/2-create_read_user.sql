-- create a database for the 2 users
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create the user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED by 'user_0d_2_pwd';
-- gives privileges to the user
GRANT SELECT ON hbtn_0d_2.* to user_0d_2@localhost;

