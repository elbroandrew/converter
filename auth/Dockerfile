FROM python:3.9-alpine

RUN apk update
RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN apk del .build-deps

COPY /auth .

EXPOSE 5005

CMD [ "python3", "./auth.py" ]
# CMD [ "uwsgi", "--ini", "./uwsgi.ini" ]