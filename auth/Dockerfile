FROM python:3.9-alpine

RUN apk update
RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN apk del .build-deps

COPY /auth .

RUN chmod u+x sql_init.sh

EXPOSE 5005
# ENTRYPOINT [ "./sql_init.sh" ]
CMD [ "python3", "./auth.py" ]
# CMD [ "uwsgi", "--ini", "./uwsgi.ini" ]