## 1. Create redis instance:

`sudo docker run -d --name redis-server -p 6379:6379 --restart unless-stopped redis:latest`

## 2. For Ubuntu just run the app from dir `/converter`:

`python3 app.py`

## 3. Run celery command from dir `/container`:

1) if redis instance is running - go to step 2, else:

`sudo docker start redis-server`

run this celery command in another terminal:

2) `celery -A celeryapp.celery_worker worker --loglevel=info`

## Tests:

`pytest -v`