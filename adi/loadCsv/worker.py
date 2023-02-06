from celery import Celery

app = Celery('proj',
             broker='amqp://guest:guest@localhost/%2f',
             backend='db+postgresql://admin:admin@192.168.1.113:5432/celery',
             include=['loadCsv.tasks', 'loadCsv.tasks_2' ,'loadCsv.load_manager'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


##avi@desktop-hili:~/Dev/adi/ADI/adi$ watchmedo auto-restart --directory=./loadCsv --pattern=*.py --recursive -- celery -A loadCsv.worker worker -l INFO

# app.autodiscover_tasks([
#    'loadCsv'
# ] ,force=True)


# if __name__ == '__main__':
#     app.start()