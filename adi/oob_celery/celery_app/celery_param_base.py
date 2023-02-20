
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from celery_app.worker import app
from celery.utils.log import get_task_logger  
#import celery_app.celeryconfig as celeryconfig



logger = get_task_logger(__name__)

class CeleryParams(app.Task):
    # name = "CeleryParams"
    # ignore_result = False
    # def __call__(self, *args, **kwargs):
    #     """Set local config file"""
    #     import json
    #    # print(__name__ + "CeleryParams")
    #     f = open('celery_app/config_load.py','w')
    #     f.write(json.dumps(kwargs.get('db_connections')))
    #     f.close()
    #     logger.info('!!!!!!!!!!!!!!!!!!!!!!!Found addition')
       
    def run(self,*args, **kwargs): 
        import json
        print(__name__ + "CeleryParams")
        f = open('celery_app/config_load.py','w')
        f.write(json.dumps(kwargs.get('db_connections')))
        f.close()
        logger.info('Found addition')

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        logger.info(__name__ + 'Init completed  addition')



app.register_task(CeleryParams())

