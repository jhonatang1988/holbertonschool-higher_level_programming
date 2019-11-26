-- create user and grant of permissions
CREATE USER IF NOT EXISTS
       'user_0d_1'@'localhost'
IDENTIFIED BY
	   'user_0d_1_pwd';
GRANT PROXY
ON root
TO user_0d_1@localhost;
