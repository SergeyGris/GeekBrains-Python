/* 
Задание 1. 
Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался при установке.

MySQL установлена, файл .my.cnf создан с наполнением:
[client]
user=root
password=****
*/

/*
Задание 2
Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.
 */

CREATE DATABASE IF NOT EXISTS example;
USE example;
CREATE Table users ( 
	id INT PRIMARY KEY,
	name VARCHAR(255)
);


/*
Задание 3
Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.
*/
 
mysqldump example > example.sql
mysql sample < example.sql

/* 
 Задание 4 (по желанию) 
 Ознакомьтесь более подробно с документацией утилиты mysqldump. 
 Создайте дамп единственной таблицы help_keyword базы данных mysql. 
Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
*/
mysqldump --where="true limit 100" mysql help_keyword > my_database.sql
 
 