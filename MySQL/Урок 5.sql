/*Практическое задание по теме «Операторы,
фильтрация, сортировка и ограничение»*/

/* Задание 1
 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их
текущими датой и временем.
*/

USE GeekBrains;

UPDATE geekbrains.users
	SET created_at=current_timestamp(), 
	updated_at=current_timestamp();

/* Задание 2
Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы
типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10.
Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.
*/
/*Изменю столбцы created_at и updated_at как по условию и добавлю новую строку*/
ALTER TABLE geekbrains.users MODIFY created_at VARCHAR(255);
ALTER TABLE geekbrains.users MODIFY updated_at VARCHAR(255);

INSERT INTO geekbrains.users (name, created_at, updated_at)
VALUES('Дарья','20.10.2017 8:10','20.10.2017 8:10');


/*Не нашел в методичке, как заменить дату, поэтому воспользовался функцией STR_TO_DATE и регулярным выражением*/
UPDATE geekbrains.users 
	SET created_at=STR_TO_DATE(created_at, '%d.%m.%Y %H:%i'), 
	updated_at=STR_TO_DATE(updated_at, '%d.%m.%Y %H:%i')
	WHERE created_at REGEXP '[0-9]{2}\\.[0-9]{2}';

ALTER TABLE geekbrains.users 
	MODIFY created_at DATETIME,
	MODIFY updated_at DATETIME;

/*. Задание 3
В таблице складских запасов storehouses_products в поле value могут встречаться самые
разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы.
Необходимо отсортировать записи таким образом, чтобы они выводились в порядке
увеличения значения value. Однако нулевые запасы должны выводиться в конце, после всех
записей */
INSERT INTO geekbrains.storehouses_products (value)
VALUES(0),(2500),(0),(30),(500),(1);

SELECT 
	value 
FROM 
	geekbrains.storehouses_products
ORDER BY
	IF(value>0,0,1),value;

/* Задание 4
 (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. 
 Месяцы заданы в виде списка английских названий (may, august)
 */
SELECT 
	name AS name, birthday_at AS birthday_date
FROM 
	geekbrains.users
WHERE MONTH(users.birthday_at)=5 OR MONTH(users.birthday_at)=8;

/*. Задание 5
(по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM
catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN
*/
SELECT * FROM catalogs 
WHERE id IN (5, 1, 2)
ORDER BY FIELD(id, 5,1,2);

/*Практическое задание теме «Агрегация данных»*/

/*. Задание 1
Подсчитайте средний возраст пользователей в таблице users.*/

SELECT AVG(DATEDIFF(NOW(),users.birthday_at)/365) AS `Average age` 
FROM users;

/* Задание 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели.
Следует учесть, что необходимы дни недели текущего года, а не года рождения.*/

SELECT DAYNAME(concat('2022','-',SUBSTRING(birthday_at,6,5))) AS BirthDay, COUNT(id) AS `Person`
FROM users
GROUP BY BirthDay;

/* Задание 3. (по желанию) Подсчитайте произведение чисел в столбце таблицы*/

DROP TABLE IF EXISTS `EX3`;
CREATE TABLE `EX3` (`Value` INT);

INSERT INTO geekbrains.ex3 
VALUES (1),(2),(3),(4),(5);

/*Я честно, подсмотрел это решение. был спортивный интерес дорешать все до конца. Немного вспомнил математику=)*/
SELECT Value, EXP(SUM(LN(Value))) AS `result`
FROM ex3;


