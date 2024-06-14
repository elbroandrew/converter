FROM python:3.9-alpine

RUN apk update
RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN apk del .build-deps

COPY . /app/

EXPOSE 5000

# CMD [ "python3", "./app.py" ]
CMD [ "uwsgi", "--ini", "./uwsgi.ini" ]