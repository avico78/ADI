from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost/%2f')

@app.task
def add(x, y):
    return x + y