```
docker-compose up --build
```
Команда соберёт образы и запустит все сервисы:
web
db
redis
celery
celery_beat

http://localhost:8000
```
docker-compose logs -f celery
### -> [INFO/MainProcess] Connected to redis://redis:6379//
```
```
docker-compose logs -f celery_beat
### -> [INFO/MainProcess] beat: Starting...
```
```
docker exec -it <имя_контейнера_db> psql -U <user> -d <db_name>
### Или через pgAdmin/IDE.
```

Удалить данные из бд и томов.
```
docker-compose down -v
docker-compose up --build
```