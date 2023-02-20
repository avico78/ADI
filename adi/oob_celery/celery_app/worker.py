import logging
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from celery import Celery
from celery.signals import after_setup_logger
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



for f in ['celery_app/broker/out', 'celery_app/broker/processed']:
    if not os.path.exists(f):
        os.makedirs(f)

@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add filehandler
    fh = logging.FileHandler('celery_app/celery.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)