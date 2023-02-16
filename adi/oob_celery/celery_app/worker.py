import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from celery import Celery
import celery_app.celeryconfig as celeryconfig

app = Celery('adi')

app.config_from_object(celeryconfig)


# Optional configuration, see the application user guide.
# app.conf.update(
#     result_expires=3600,
# )



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