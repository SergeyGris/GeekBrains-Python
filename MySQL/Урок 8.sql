/* Необязательное задание с 8 вебинара*/

SELECT 
	m.filename,
	COUNT(l.id) AS total_likes,
	CONCAT(u.firstname, ' ', u.lastname) AS owner
	FROM media m
	LEFT JOIN likes l ON l.media_id = m.id
	JOIN users u ON u.id=m.user_id
	GROUP BY m.id
ORDER BY total_likes desc;

/* Задание 1. 
 Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека,
 который больше всех общался с нашим пользователем.*/

	
SELECT from_user_id AS 'user id', count(from_user_id) AS `total messages`
FROM messages m
JOIN friend_requests fr 
ON (fr.initiator_user_id = m.from_user_id AND fr.target_user_id =1)
    	OR 
    	(fr.target_user_id = m.from_user_id AND fr.initiator_user_id =1) 
  	WHERE fr.status = 'approved' AND m.to_user_id=1
GROUP BY from_user_id 
ORDER BY `total messages` desc 
LIMIT 1
	


/*Задание 2
 Подсчитать общее количество лайков, которые получили пользователи младше 11 лет.*/

SELECT COUNT(*) AS 'total likes'
FROM media m 
RIGHT JOIN profiles p ON p.user_id =m.user_id
JOIN likes l ON l.media_id=m.id
WHERE TIMESTAMPDIFF(YEAR, p.birthday, NOW())<11



/* неверное решение 
 SELECT count(l.id) AS 'total likes'
FROM profiles p
JOIN likes l ON l.user_id =p.user_id 
WHERE TIMESTAMPDIFF(YEAR, p.birthday, NOW())<=11*/




/* Задание 3 
 
 Определить кто больше поставил лайков (всего): мужчины или женщины.*/

SELECT CASE(gender)
	WHEN 'f' THEN 'female'
	ELSE 'male'
END AS gender, count(p.user_id) AS `total likes`
FROM profiles p 
JOIN likes l ON l.user_id=p.user_id 
GROUP BY gender 
ORDER BY `total likes` DESC 
LIMIT 1;