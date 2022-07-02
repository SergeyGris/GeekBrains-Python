/* Задание 1. 
 Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от
текущего времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с
12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый
вечер", с 00:00 до 6:00 — "Доброй ночи". */ 


DROP PROCEDURE IF EXISTS hello;
DELIMITER //

CREATE PROCEDURE hello()
BEGIN
	SET @time = HOUR(NOW());
	IF (@time > 0 AND @time <= 6) THEN SELECT 'Доброй ночи'; 
	ELSEIF (@time > 6 AND @time <= 12) THEN SELECT 'Доброе утро';
	ELSEIF (@time > 12 AND @time <= 18) THEN SELECT 'Добрый день';
	ELSE SELECT 'Добрый вечер';
	END IF;
END //
DELIMITER ;



/* Задание 2
В таблице products есть два текстовых поля: name с названием товара и description с его
описанием. Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля
принимают неопределенное значение NULL неприемлема. Используя триггеры, добейтесь
того, чтобы одно из этих полей или оба поля были заполнены. При попытке присвоить полям
NULL-значение необходимо отменить операцию.*/

DROP TRIGGER IF EXISTS check_null;
DELIMITER //

CREATE TRIGGER check_null BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL AND NEW.description IS NULL) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled';
	END IF;
END //
DELIMITER ;


/* Задание 3. (по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи.
Числами Фибоначчи называется последовательность в которой число равно сумме двух
предыдущих чисел. Вызов функции FIBONACCI(10) должен возвращать число 55.*/

DROP FUNCTION IF EXISTS FIBONACCI;
DELIMITER //

CREATE FUNCTION FIBONACCI(value INT)
RETURNS INT DETERMINISTIC
BEGIN
	DECLARE x,y,z,i INT DEFAULT 0;
	WHILE i<value DO
		-- SELECT value;
		IF(i=0) THEN SET x=x+1;
	ELSEIF(i>0) THEN 
				SET z=y;
				SET y=x;
	END IF;
		SET x=x+z;
		SET i=i+1;
	END WHILE;
	RETURN x;
END //
DELIMITER ;

