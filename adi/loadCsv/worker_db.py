from celery import Celery

app = Celery('proj',
             broker='amqp://guest:guest@localhost:5672',
             backend='db+postgresql://admin:admin@192.168.1.113:5432/celery
            #  ,
            #  include=['loadCsv.tasks','loadCsv.load_manager' ,'loadCsv.tasks_2
              ],
             broker_pool_limit=0)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

task_routes = {'loadCsv.tasks_2.load_from_db': {'queue': 'db'}}
app.conf.task_routes = task_routes

try:
    app.broker_connection().ensure_connection(max_retries=3)
except Exception as ex:
    raise RuntimeError("Failed to connect to celery broker, {}".format(str(ex)))

##avi@desktop-hili:~/Dev/adi/ADI/adi$ watchmedo auto-restart --directory=./loadCsv --pattern=*.py --recursive -- celery -A loadCsv.worker worker -l INFO

# app.autodiscover_tasks([
#    'loadCsv'
# ] ,force=True)


# if __name__ == '__main__':
#     app.start()