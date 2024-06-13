FROM python:3.9-alpine

RUN apk update
RUN apk add curl

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app/

CMD [ "python3", "./app.py" ]