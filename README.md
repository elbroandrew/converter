## inside `converter/` directory run:

`sudo docker-compose up -d`

или если надо сбилдить образы сначала:

`sudo docker-compose up -d --build`


## Затем перейти на:

App port: `http://127.0.0.1/80`

Flower port: `http://0.0.0.0:5555/`


## Tests:

`pytest -v`

## Чтобы принты попали в консоль, надо добавить флаг -s:

`pytest -v -s`

## Скриншоты приложения и Flower с Celery воркером

![(examples/Screenshot 2024-08-05 at 13-00-44 BLP to PNG image converter App.png)]
