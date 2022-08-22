# Проект API FINAL YATUBE

### Описание проекта:
Сайт Yatube - это соцсеть, где можно делать публикации на различные темы. Подписываться на авторов, а так же оставлять комментарии. Это API для сайта. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone https://github.com/AlexanderAvrov/api_final_yatube.git
```

```sh
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```sh
python -m venv venv
```

```sh
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```sh
python -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

Выполнить миграции:

```sh
python manage.py migrate
```

Запустить проект:

```sh
python manage.py runserver
```

### Примеры запросов API к сайту
Запрос:
```
POST http://127.0.0.1:8000/api/v1/posts/
```
Ответ: 
```sh
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Запрос:
```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Ответ: 
```sh
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```