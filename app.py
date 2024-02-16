from api import app
from celeryapp.celery_worker import celery_app



if __name__ == '__main__':

    app.run(debug=True)

    celery_app.main = app.name
    with app.app_context():
        worker = celery_app.Worker()
        worker.start()