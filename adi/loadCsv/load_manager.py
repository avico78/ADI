
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))



import json
from app_config.db_config import DBContext
from loadCsv.client import load_config
from celery import group

from loadCsv.worker import app
from loadCsv.tasks_2 import proccess_customer
import time


import logging
logger = logging.getLogger(__name__)



class LoadManager(app.Task):
    name = "LoadManager"
    ignore_result = False
    _db_connections = {}

    def __call__(self, *args, **kwargs):
        """Main Task which load setting as db conenction  and also he csv with rules
          It first scan all required details as what db_connection involved 
          """
        self.config = json.loads(kwargs.get('config'))
        for db in self.config['db_connections']:
            """DBcontext can return either Engine or Session if needed and store all 
            in _db_connection """
            # db_engine =  DBContext().get_db(self.config['db_connections'][db]['connection_details'])
            # LoadManager._db_connections[db] = db_engine
        self.mapping_rules = self.config['csvdict']
        self.customers_list = self.config['customers_list']
        kwargs = { 'mapping_rules': self.mapping_rules }
        return self.run(*args, **kwargs)
        
    def run(self,*args, **kwargs): 
        
        print("RUN!")
        proccess_customer.delay(1,**kwargs)
        # a = load_data.delay(1,2,3,**kwargs)
        # logger.info(f'kwargs Run = {kwargs}')
        # logger.info(f'args Run = {args}')

      #  return group([ proccess_customer.delay(customer, **kwargs) for customer in self.customers_list])
   
      

        # logger.error('No x or y in arguments')

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print("Post Run")
        #exit point of the task whatever is the state
       # print(__name__ + "         AFTER!!!!!!!!!!!!!!!")
        # test_load.delay(**kwargs)

# class AddTask(LoadManager):

#     def run(self,*args, **kwargs):
#         logger.info(f'AddTask = {kwargs}')
#         # logger.error('No x or y in arguments')


app.register_task(LoadManager())


if __name__ == "__main__":
    import json
    load_config.initialize_operation()
    # mapping_rules = json.dumps(load_config.csv2dict)


    a = proccess_customer.delay(customer_id=1, a="Task!!!@#")
    
    # settings = json.dumps({"csvdict": [{"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM customer1 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "1"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM rental1 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "1"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM customer2 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "3"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM rental2 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "3"}}], "customers_list": [1, 2, 3, 4, 5, 6, 7], "db_connections": {"postgres": {"connection_details": {"DB_TYPE": "postgres", "ENGINE": "postgres", "NAME": "dvdrental", "USER": "admin", "PASSWORD": "admin", "HOST": "192.168.1.113", "PORT": 5432}, "engine": ""}}})
    # csv_dict= json.dumps({"csvdict": [{"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM customer1 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "1"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM rental1 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "1"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM customer2 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "3"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM rental2 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "3"}}], "customers_list": [1, 2, 3, 4, 5, 6, 7], "db_connections": {"postgres": {"connection_details": {"DB_TYPE": "postgres", "ENGINE": "postgres", "NAME": "dvdrental", "USER": "admin", "PASSWORD": "admin", "HOST": "192.168.1.113", "PORT": 5432}, "engine": ""}}})
    # a = LoadManager().delay(config=mapping_rules)
    # print(a)



# #test_load.delay(keys=555,x=1,a=1,b=2,c=3)
# a = LoadManager().delay(keys=[1,2,3,4])
# print(a.get())

