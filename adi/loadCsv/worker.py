from celery import Celery

app = Celery('proj',
             broker='amqp://guest:guest@localhost/%2f',
             backend='db+postgresql://admin:admin@192.168.1.113:5432/celery',
             include=['loadCsv.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()