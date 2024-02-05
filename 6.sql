-- 1. Написать функцию, которая удаляет всю информацию об указанном пользователе из БД vk. Пользователь задается по id. Удалить нужно все сообщения, 
-- лайки, медиа записи, профиль и запись из таблицы users. Функция должна возвращать номер пользователя.
use vk;

DELIMITER //

CREATE FUNCTION delete_user_by_id(user_id INT) RETURNS INT
BEGIN
    DECLARE user_exists INT;

    -- Проверяем, существует ли пользователь с указанным ID
    SELECT COUNT(*) INTO user_exists FROM users WHERE id = user_id;
    IF user_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Пользователь с указанным ID не найден';
    END IF;

    -- Удаляем сообщения
    DELETE FROM messages WHERE from_user_id = user_id OR to_user_id = user_id;

    -- Удаляем лайки
    DELETE FROM likes WHERE user_id = user_id;

    -- Удаляем медиа записи
    DELETE FROM media WHERE user_id = user_id;

    -- Удаляем профиль
    DELETE FROM profiles WHERE user_id = user_id;

    -- Удаляем запись из таблицы users
    DELETE FROM users WHERE id = user_id;

    -- Возвращаем номер пользователя
    RETURN user_id;
END //

DELIMITER ;
-- Предыдущую задачу решить с помощью процедуры и обернуть используемые команды в транзакцию внутри процедуры.
DELIMITER //

CREATE FUNCTION delete_user_by_id(user_id INT) RETURNS INT
BEGIN
    DECLARE user_exists INT;

    -- Проверяем, существует ли пользователь с указанным ID
    SELECT COUNT(*) INTO user_exists FROM users WHERE id = user_id;
    IF user_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Пользователь с указанным ID не найден';
    END IF;

    -- Начинаем транзакцию
    START TRANSACTION;

    -- Удаляем сообщения
    DELETE FROM messages WHERE from_user_id = user_id OR to_user_id = user_id;

    -- Удаляем лайки
    DELETE FROM likes WHERE user_id = user_id;

    -- Удаляем медиа записи
    DELETE FROM media WHERE user_id = user_id;

    -- Удаляем профиль
    DELETE FROM profiles WHERE user_id = user_id;

    -- Удаляем запись из таблицы users
    DELETE FROM users WHERE id = user_id;

    -- Завершаем транзакцию
    COMMIT;

    -- Возвращаем номер пользователя
    RETURN user_id;
END //

DELIMITER ;

-- 3.Написать триггер, который проверяет новое появляющееся сообщество. Длина названия сообщества (поле name) должна быть не менее 5 символов. 
-- Если требование не выполнено, то выбрасывать исключение с пояснением.
CREATE TRIGGER check_community_name_length
BEFORE INSERT ON communities
FOR EACH ROW
BEGIN
    IF LENGTH(NEW.name) < 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Длина названия сообщества должна быть не менее 5 символов';
    END IF;
END;