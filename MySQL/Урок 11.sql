/*Задание 1) Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, 
catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы, 
идентификатор первичного ключа и содержимое поля name.*/

USE shop;

-- Для начала создадим таблицу logs
DROP TABLE IF EXISTS logs;
CREATE TABLE logs(
	date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
	table_name VARCHAR(255),
	key_id BIGINT UNSIGNED,
	name_field varchar(255)
) ENGINE=Archive ;

-- Сделаем вспомогательную процедуру logs_insert

DROP PROCEDURE IF EXISTS logs_insert;

DELIMITER //
CREATE PROCEDURE logs_insert (table_name_var VARCHAR (255), id_var BIGINT, name_field_var VARCHAR (255))
BEGIN
	INSERT INTO logs (table_name, key_id, name_field) VALUES (table_name_var, id_var, name_field_var);
END //
DELIMITER ;

/*Создадим триггер. я не нашел переменной, отвечающей за имя столбца. 
Поэтому надо создать 3 триггера?*/

-- Для catalogs
DROP TRIGGER IF EXISTS logs_catalogs;

DELIMITER //
CREATE TRIGGER logs_catalogs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN 
	CALL logs_insert('catalogs', NEW.id, NEW.name);
END//
DELIMITER ;

-- Для products
DROP TRIGGER IF EXISTS logs_products;

DELIMITER //
CREATE TRIGGER logs_products AFTER INSERT ON products
FOR EACH ROW
BEGIN 
	CALL logs_insert('products', NEW.id, NEW.name);
END//
DELIMITER ;

-- Для users
DROP TRIGGER IF EXISTS logs_users;

DELIMITER //
CREATE TRIGGER logs_users AFTER INSERT ON users
FOR EACH ROW
BEGIN 
	CALL logs_insert('users', NEW.id, NEW.name);
END//
DELIMITER ;

/*Проверим работоспособность. В случае таблицы products нужно еще добавить
 * столбец description из-за наличия триггера с прошлого урока, запрещающего оставлять поле пустым.
*/
INSERT INTO catalogs(name) VALUES ('Адаптеры');
INSERT INTO products(name, description) VALUES ('USB', 'USB');
INSERT INTO users(name) VALUES ('Виталий');


/*Задание 2) Создайте SQL-запрос, который помещает в таблицу users миллион записей.*/


-- Буду использовать таблицу orders

DROP PROCEDURE IF EXISTS insert_billion ;

DELIMITER //
CREATE PROCEDURE insert_billion ()
BEGIN
	DECLARE i INT DEFAULT 0;
	WHILE i < 1000000 DO
		INSERT INTO orders(user_id) VALUES (FLOOR(rand()*10));
		SET i = i + 1;
	END WHILE;
END //
DELIMITER ;

-- Взял DDL из свойств таблицы orders, чтобы пересоздать таблицу

-- shop.orders definition

DROP TABLE IF EXISTS orders;
CREATE TABLE `orders` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `index_of_user_id` (`user_id`)
) ENGINE=InnoDB COMMENT='Заказы';


CALL insert_billion();

-- Я тестировал на 100. на миллионе компьютер завис=) 

DROP PROCEDURE IF EXISTS insert_hundred ;
DELIMITER //
CREATE PROCEDURE insert_hundred ()
BEGIN
	DECLARE i INT DEFAULT 0;
	WHILE i < 100 DO
		INSERT INTO orders(user_id) VALUES (FLOOR(rand()*10));
		SET i = i + 1;
	END WHILE;
END //
DELIMITER ;

CALL insert_hundred();
