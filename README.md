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
![img1](https://github.com/elbroandrew/converter/blob/8241fde49002457d6bb0390c1c68dd5c275454f8/examples/Screenshot%202024-08-05%20at%2013-04-00%20BLP%20to%20PNG%20image%20converter%20App.png)

![img2](https://github.com/elbroandrew/converter/blob/4ac18bc801a02552d49fdad74427149ac6e60743/examples/Screenshot%202024-08-05%20at%2013-00-44%20BLP%20to%20PNG%20image%20converter%20App.png)

![Flower](https://github.com/elbroandrew/converter/blob/098d9cacaf314ee1729c6c3059e66c02355ecf76/examples/Screenshot%202024-08-05%20at%2013-01-20%20Flower.png)
