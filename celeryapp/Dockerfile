FROM python:3.9-alpine

WORKDIR /app

RUN pip install celery==5.3.6 redis==5.0.1
RUN pip install pillow==10.2.0 kombu==5.3.5

COPY ./celeryapp ./celeryapp
COPY ./converter ./converter
COPY ./start-celery.sh ./
RUN chmod +x ./start-celery.sh
USER nobody
# RUN adduser --disabled-password andrew
# USER andrew

# CMD [ celery -A celeryapp.celery_worker worker --loglevel=info ]