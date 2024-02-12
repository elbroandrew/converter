## - Run script from the work dir in 'Win-10':
## activate venv (start CMD with admin privileges), then:
`.\venv\Scripts\activate`

## Set up FLASK_APP variable for Win10:

`$env:FLASK_APP="app.py"`

## Run the Flask app:

`py -m app`

## Go to:

`http://127.0.0.1:5000`

## - For Ubuntu just run the app in the dir `/converter`:

`python3 app.py`

## celery run command in the dir `/container`:

1) frirst thing first run docker container with redis

then:

2) `celery -A app.celery worker --loglevel=info`