-- create user and grant of permissions
CREATE USER IF NOT EXISTS
       'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT PROXY
ON root
TO user_0d_1@localhost;
FLUSH PRIVILEGES;
