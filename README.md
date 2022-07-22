### Inside
[Задание](https://cloud.mail.ru/public/8Zje/V1dgCCM44) 

[Файл с CURL запросами](https://cloud.mail.ru/public/twMx/uHbLEGubY)

[dockerhub](https://hub.docker.com/repository/docker/abramtsevfv/inside_task_web)
## Управление ##
### Запуск Docker ###
1) Выполняем команду: 
```
  docker-compose up -d
 ```
2) Для получения токена отправляем POST запрос:
    ````
   http://0.0.0.0:8000/api/v1/users/login/
    ````
   - в теле передаём JSON:
   ````
   {
        "username": "fedor",
        "email": "fedor@admn.ru",
        "password": "12345678"
    }
   ````
   > usename - строка, email - адрес, password - 8 символов. 
   - в ответ получаем:
   ````
   {
    "token": "<token>"
    }
    ````
3) Для работы с сообщениями отправляем POST запрос:
    ````
   http://0.0.0.0:8000/api/v1/message/
   ````
   - В Headers передаём строку:
   ````
   Authorization:Bearer_<toeken>
   ````
   - в теле запроса JSON для сохранения сообщения:
   ````
   {
    "user":"имя пользователя",
    "message": "текст сообщения"
    }
   ````
   - В ответ получим такой же JSON статус код 201.
   - Для получения отправленных:
   ````
   {
    "user":"имя пользователя",
    "message": "history <чило последних сообщений>"
    }
    ````
   > history - ключевое слово - число должно быть целое и положительное.
    - Ответ список:
   ````
   [
    {
        "user": "имя пользователя",
        "message": "сообщение"
    },
    {
        "user": "имя пользователя",
        "message": "сообщение"
    }
   ]
   ````
   ### Запуск Тестов из Docker ###
1. Выполняем команду
```
  docker-compose run --rm web ./manage.py test