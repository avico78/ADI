
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from celery import group,chord,chain

from loadCsv.tasks_2 import test_load,load_data
from loadCsv.worker import app
import time


import logging
logger = logging.getLogger(__name__)


# def run_LoadManager(*args ,**kwargs):



class LoadManager(app.Task):
    name = "LoadManager"
    ignore_result = False
    def __call__(self, *args, **kwargs):
        """In celery task this function call the run method, here you can
        set some environment variable before the run of the task"""

        self.keys = kwargs.get('keys',[1,2])
        self.mapping_rules = kwargs.get('mapping_rules',[{'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM customer1 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '1'}}, {'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM rental1 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '1'}}, {'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM customer2 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '3'}}, {'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM rental2 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '3'}}])
        # test_load.delay(**kwargs)
       # proccess_customers.delay(self.keys ,self.mapping_rules)

        # return self.run(*args, **kwargs)

    def run(self,*args, **kwargs):
        logger.info(f'On Run = {kwargs}')
        return group([load_data.delay(key, self.mapping_rules) for key in self.keys])

        # logger.error('No x or y in arguments')

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        #exit point of the task whatever is the state
        print(__name__ + "         AFTER!!!!!!!!!!!!!!!")
        # test_load.delay(**kwargs)

# class AddTask(LoadManager):

#     def run(self,*args, **kwargs):
#         logger.info(f'AddTask = {kwargs}')
#         # logger.error('No x or y in arguments')

app.register_task(LoadManager())





#test_load.delay(keys=555,x=1,a=1,b=2,c=3)
a = LoadManager().delay(keys=[1,2,3,4])
print(a.get())

