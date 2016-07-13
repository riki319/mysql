# Python Mysql

## Install

```shell
	$ ./install.sh
```

## Enter mysql command line

```shell
	$ mysql -u root -p
```

## Create user

```sql
	CREATE USER 'pwaqo'@'localhost' IDENTIFIED BY 'pwaqo';
	GRANT ALL PRIVILEGES ON * . * TO 'pwaqo'@'localhost';
	FLUSH PRIVILEGES;
```
