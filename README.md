# Dockerized Django+Celery+POstgres
## First create volume . it will let u pass permission errors on Database folder
```sh
docker volume create db_volume
```

Now time to start up whole project
```sh
docker compose up
```
Now you can test it on Postman 
```sh
localhost:8000
```

Deployed version on heroku

```sh
https://dynooo.herokuapp.com/
```