FROM mher/flower:latest

WORKDIR /app

RUN pip install celery==5.3.6 redis==5.0.1
RUN pip install pillow==10.2.0 kombu==5.3.5

COPY ./celeryapp ./celeryapp
COPY ./converter ./converter
