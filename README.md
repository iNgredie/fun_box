Запуск проекта.
 - Скопировать проект с помощью ``` git clone https://github.com/iNgredie/fun_box.git ```
 - ```docker-compose up --build ```  собрать приложение и сделать его первоначальный запуск
 - ```docker-compose down -v``` – остановить работу приложения
 - ```docker-compose run web python manage.py migrate``` – сделать необходимые миграции
 - ```docker-compose up``` – окончательно запустить приложение.

Стек технологий и требований к ним для реализации веб-приложения 

- Python 3
- Django 
- Django-rest-framework

``` http://localhost:8000/api/visited_links/``` Ресурс загрузки посещений Method POST

Запрос 1
 ``` 
{
    "links": [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "funbox.ru",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
    ]
}
 ```
Ответ 1
```
{
    "status": "ok"
}
```
Ресурс получения статистики Method GET

Запрос 2  
``` http://localhost:8000/api/visited_domains?from=1545221231&to=1545217638```    

Ответ 2
```
{
    "domains": [
        "ya.ru",
        "funbox.ru",
        "stackoverflow.com"
    ],
    "status": "ok"
}
```

• Первый ресурс служит для передачи в сервис массива ссылок в POST-запросе. Временем их посещения считается время получения запроса сервисом.   
• Второй ресурс служит для получения GET-запросом списка уникальных доменов,
посещенных за переданный интервал времени.  
• Поле status ответа служит для передачи любых возникающих при обработке запроса
ошибок.  
• Для хранения данных сервис должен использовать БД Redis