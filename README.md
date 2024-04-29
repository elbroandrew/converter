## - Run script from the work dir in 'Win-10':
## activate venv (start CMD with admin privileges), then:
`.\venv\Scripts\activate`

## Run the Flask app:

`py -m app`

## Go to:

`http://127.0.0.1:5000`

## - For Ubuntu just run the app in the dir `/converter`:

`python3 app.py`

## Run celery command in the dir `/container`:

1) frirst thing first run docker container with redis

## then run this celery command in another terminal:

2) `celery -A celeryapp.celery_worker worker --loglevel=info`