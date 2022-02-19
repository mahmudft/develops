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

Postman Collections Link
```sh
https://www.postman.com/avionics-cosmonaut-58754428/workspace/developstoday/api/d1b639d4-ead4-4579-9fa5-e10a45476059
```