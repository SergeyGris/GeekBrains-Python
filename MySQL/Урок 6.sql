/*Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение. Агрегация данных”*/

/* Задание 1. 
 Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека,
 который больше всех общался с нашим пользователем.*/
 

SELECT COUNT(id) AS cnt,
	(SELECT firstname FROM users WHERE id=messages.from_user_id) AS `user`
FROM messages
WHERE to_user_id=1
AND from_user_id IN (SELECT initiator_user_id FROM friend_requests 
WHERE (target_user_id = 1) AND status ='approved'
UNION
SELECT target_user_id FROM friend_requests 
WHERE (initiator_user_id = 1) AND status ='approved')
GROUP BY from_user_id
ORDER BY cnt DESC
LIMIT 1

-- Я пробовал через функцию max(), не получилось. Эту задачу можно так решить?



/*Задание 2
 Подсчитать общее количество лайков, которые получили пользователи младше 11 лет.*/

SELECT COUNT(*) AS 'total likes'
FROM likes
WHERE media_id IN(
	SELECT id FROM media
	WHERE user_id IN (
		SELECT
		user_id FROM profiles
		WHERE TIMESTAMPDIFF(YEAR, birthday, NOW())<=11
		)
	)
;


/* Задание 3 
 
 Определить кто больше поставил лайков (всего): мужчины или женщины.*/
 
-- новое решение
SELECT count(id) AS `likes count`, 
	(SELECT gender FROM profiles
	WHERE profiles.user_id=likes.user_id) AS `gender`
FROM likes
GROUP BY gender
ORDER BY `likes count` DESC
LIMIT 1;


/*-- старое решение (не получилось)
SELECT COUNT(*) AS `count`, gender
FROM profiles
WHERE user_id IN(SELECT user_id FROM likes)
GROUP BY gender 
ORDER BY `count` DESC 
LIMIT 1

-- Как сделать, чтобы select брал все значения из вложенного запроса (3 строка), а не только уникальные?*/