
import time
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app_config.db_config import DBContext
from celery import group

from loadCsv.worker import app
from loadCsv.tasks_2 import route_load_type


import logging
logger = logging.getLogger(__name__)



@app.task(bind=True , name='route_load_type')
def route_load_type(self,*args,**kwargs):
    curr_customer = args[0]
    mapping_rules = kwargs['mapping_rules']
    print("Proccessing customer:" , curr_customer  )
    print("DB",self._db_connections)
    """ Go thought each line and check if required fetch data from DB"""
    for rule in mapping_rules:
        if rule['rules']['source_type'] == 'db':
            sql = rule['rules']['sql']
            # assign current customer to sql
            sql = sql.replace("&1",str(curr_customer))
            
            """
            Here will call other function to fetch the query:
            1.How to share DB connection
            2.this function called as async ,so the question should I continue call load_from_db with "delay"
            
            """

            load_from_db()
        elif rule['rules']['source_type'] == 'file':
            pass
        elif rule['rules']['source_type'] == 'other_type':
            pass
        


@app.task(bind=True , name='route_load_type')
def load_from_db(self,*args,**kwargs):
    pass


class LoadManager(app.Task):
    name = "LoadManager"
    ignore_result = False
    _db_connections = {}

    def __call__(self, *args, **kwargs):
        """Main Task which load setting as db conenction  and also he csv with rules
          It first scan all required details as what db_connection involved 
          """
        self.config = json.loads(kwargs.get('config'))
        """ Setting all required db connection"""
        for db in self.config['db_connections']:
            """DBcontext can return either Engine or Session if needed and store all 
            in _db_connection """
            db_engine =  DBContext().get_db(self.config['db_connections'][db]['connection_details'])
            LoadManager._db_connections[db] = db_engine
        # saving csv file ( rules)
        self.mapping_rules = self.config['csvdict']
        # all customers
        self.customers_list = self.config['customers_list']
        kwargs = { 'mapping_rules': self.mapping_rules }
        return self.run(*args, **kwargs)
        
    def run(self,*args, **kwargs):
        # This would be the main/manager proccess which exeucte task for each customer
        return group([ route_load_type.delay(customer, **kwargs) for customer in self.customers_list])

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
         """Maybe here it would be right place to check if task completed successfully - if yes it required to check
         all other tasks (probably with wait till complete mechansize OR if any task failed)
         """
         pass
  
        

app.register_task(LoadManager())


if __name__ == "__main__":
    import json
    settings = json.dumps({"csvdict": [{"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM customer1 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "1"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM rental1 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "1"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM customer2 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "3"}}, {"key": "", "rules": {"source_type": "db", "source_name": "postgres", "db_connection_name": "source_ps", "sql": "SELECT * FROM rental2 where customer=&1 ", "target_type": "df ", "db_connection_target": " file ", "order": "3"}}], "customers_list": [1, 2, 3, 4, 5, 6, 7], "db_connections": {"postgres": {"connection_details": {"DB_TYPE": "postgres", "ENGINE": "postgres", "NAME": "dvdrental", "USER": "admin", "PASSWORD": "admin", "HOST": "192.168.1.113", "PORT": 5432}, "engine": ""}}})
    a = LoadManager().delay(config=settings)
    print(a)



