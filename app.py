from api import app
from celery import Celery


celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)

if __name__ == '__main__':
    app.run(debug=True)