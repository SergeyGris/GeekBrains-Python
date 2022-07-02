/* Скрипты выборок*/

/*Задача 1 
Назначить деканами факультета произвольных преподавателей этого факультета.
*/
-- Для этого добавим в таблицу faculties столбец dean_id и назначим его внешним ключом
ALTER TABLE faculties ADD COLUMN dean_id BIGINT UNSIGNED;
ALTER TABLE faculties ADD CONSTRAINT dean_id
    FOREIGN KEY (dean_id) REFERENCES professors(id)
    ON UPDATE CASCADE ON DELETE CASCADE;
    
-- Назначим деканами факультета произвольных преподавателейэтого факультета.
   
UPDATE faculties 
SET dean_id=(
	SELECT id 
	FROM professors 
	WHERE professors.faculties_id=faculties.id 
	ORDER BY rand() 
	LIMIT 1
	)
;

/*Задача 2
Сколько девушек получили оценку выше 70 по биологии.
*/

SELECT COUNT(mark) AS total
FROM marks m 
RIGHT JOIN profiles p ON p.student_id=m.student_id AND p.gender='f'
WHERE m.mark>=70 AND m.subject_id = (SELECT id FROM subjects s WHERE s.name='Biology');

/*Задача 3
Выбрать всех парней из группы 26-447.
*/

SELECT CONCAT(s.firstname,' ', s.lastname) AS name
FROM students s 
JOIN `groups` g ON g.name='26-447'
JOIN students_group sg ON sg.student_id=s.id AND sg.group_id=g.id  
JOIN profiles p ON p.student_id=s.id AND p.gender='m';

/*Задача 4
Посчитать сколько оценок поставил каждый профессор.
*/

SELECT CONCAT(firstname,' ', lastname) AS name, COUNT(*) AS total
FROM professors p
JOIN marks m ON m.professor_id=p.id
GROUP BY name;

/* Задача 5
 Посчитать общее количество студентов в каждой группе Химического института им. Александра Бутлерова
 */


SELECT g.name AS 'Group name', count(*) AS 'Total' 
FROM `groups` g 
JOIN students_group sg ON sg.group_id =g.id 
JOIN students s ON s.id =sg.student_id 
WHERE g.faculty_id =(SELECT id FROM faculties f WHERE f.name='Alexander Butlerov Institute of Chemistry')
GROUP BY g.name;


/*Задача 6
Посчитать средний балл по каждому предмету студентов у всех факультетов.
*/

SELECT f.abbreviation  AS 'Faculty', s.name AS 'Subject', AVG(m.mark) AS `Average mark` 
FROM subjects s 
JOIN marks m ON m.subject_id =s.id
JOIN students s2 ON s2.id=m.student_id 
JOIN students_group sg ON sg.student_id =s2.id
JOIN `groups` g ON  g.id=sg.group_id 
JOIN faculties f ON f.id=g.faculty_id 
GROUP BY s.name, f.name
ORDER BY f.name ASC, `Average mark` ASC  

/* Скрипты представлений*/

/* Представление 1
 * Соотнести факультет и студентов
 */
DROP VIEW IF EXISTS faculties_students;
CREATE VIEW faculties_students AS
SELECT f.abbreviation  AS 'Faculty', CONCAT(s.firstname,' ', s.lastname) AS name, g.name AS 'Group'
FROM faculties f 
JOIN `groups` g ON  g.faculty_id=f.id 
JOIN students_group sg ON sg.group_id=g.id
JOIN students s ON s.id=sg.student_id 
ORDER BY f.name ASC;

/* Представление 2
 * Таблица среднего балла по каждому предмету студентов каждого факультета.
 */
DROP VIEW IF EXISTS average_marks;
CREATE VIEW average_marks AS
SELECT f.abbreviation  AS 'Faculty', s.name AS 'Subject', AVG(m.mark) AS `Average mark` 
FROM subjects s 
JOIN marks m ON m.subject_id =s.id
JOIN students s2 ON s2.id=m.student_id 
JOIN students_group sg ON sg.student_id =s2.id
JOIN `groups` g ON  g.id=sg.group_id 
JOIN faculties f ON f.id=g.faculty_id 
GROUP BY s.name, f.name
ORDER BY f.name ASC, `Average mark` ASC;

/* Триггер 1
 * Триггер проверки пустого имени
*/

DROP TRIGGER IF EXISTS check_null;
DELIMITER //

CREATE TRIGGER check_null BEFORE INSERT ON students
FOR EACH ROW
BEGIN
	IF (NEW.firstname IS NULL OR NEW.lastname IS NULL) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled';
	END IF;
END //
DELIMITER ;

-- Вставим нового пользователя, триггер должен запретить вставку и вывести ошибку 45000 'INSERT canceled'
INSERT INTO `students` (`firstname`, `email`, `phone`) 
VALUES ('Eliezer', 'xxx@example.net', '9614545764');


/* Триггер 2
 * Триггер подсчета возраста
*/

ALTER TABLE profiles ADD COLUMN age INT UNSIGNED ;

DROP TRIGGER IF EXISTS check_age;
DELIMITER //

CREATE TRIGGER check_age AFTER INSERT ON profiles
FOR EACH ROW
BEGIN
	IF (NEW.age IS NULL) THEN 
		SET NEW.age=YEAR(NOW())-YEAR(NEW.birthday);
	END IF;
END //
DELIMITER ;

-- Вставим нового пользователя, автоматчески подсчитается возраст
INSERT INTO `students` (`firstname`, `lastname`, `email`, `phone`) 
VALUES ('Eliezer', 'Bartoletti', 'xxx@example.net', '9614545764');

INSERT INTO profiles(student_id, gender, birthday, hometown) 
VALUES ('201', 'm', '1995-07-15', 'Lindmouth');

/* Хранимая процедура 1
 * Делает выборку среднего балла по всем предметам по факультетам
 */
DELIMITER //
DROP PROCEDURE IF EXISTS average_mark//
CREATE PROCEDURE average_mark()
BEGIN
	SELECT Faculty, AVG(am.`Average mark`) AS `Average mark` 
	FROM average_marks am
	GROUP BY Faculty
	ORDER BY `Average mark` ASC;
END //
DELIMITER ;

CALL average_mark();

/* Хранимая процедура 2
 * Процедура, которая считает количество парней и девушек
 */
DELIMITER //
DROP PROCEDURE IF EXISTS Select_gender//
CREATE PROCEDURE Select_gender()
BEGIN
	SELECT CASE 
		WHEN p.gender='m' THEN 'male'
		ELSE 'female'
	END AS gender,
	COUNT(*) AS Total
	FROM students s 
	JOIN profiles p ON p.student_id=s.id 
	GROUP BY gender;
END //
DELIMITER ;

CALL Select_gender();

