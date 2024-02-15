from api import app
# from api import celery_worker

if __name__ == '__main__':
    app.run(debug=True)
    # with app.app_context():
    #     worker = celery_worker.Worker()
    #     worker.start()