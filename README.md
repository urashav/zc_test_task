### Реализовать на Django Rest Framework RESTful API, позволяющее:

- Осуществлять create, read, delete операции с сообщениями
- Проставлять флаг "прочитано" сообщению

При создании сообщения запускать celery задачу, которая проставит сообщению флаг "отправлено" (иммитация отправки в сторонний сервис).
Ограничить количество допустимых запросов на создание сообщение в 10 запросов в минуту.

Структура сообщения (перечислены только критичные поля):
- заголовок
- тело сообщения
- флаг отправки
- флаг прочтения

Ограничения:
- Необходимо использовать Django Rest Framework
- По СУБД ограничений нет. Можно даже SQLite
- Аутентификация с авторизацией - необязательно, по желанию
- Брокер сообщений - любой. RabbitMQ будет плюсом
- Тесты - будут плюсом