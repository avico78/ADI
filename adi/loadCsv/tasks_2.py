
import sys
import logging
import time
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from celery import group,Task
from loadCsv.worker import app

from app_config.db_config import DBContext
from loadCsv.client import load_config

logger = logging.getLogger(__name__)


db_connections = {'postgres': {'connection_details': {'DB_TYPE': 'postgres', 'ENGINE': 'postgres', 'NAME': 'dvdrental', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': '192.168.1.113', 'PORT': 5432}, 'engine': ''}, 'target': {'connection_details': {'DB_TYPE': 'postgres', 'ENGINE': 'postgres', 'NAME': 'target', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': '192.168.1.113', 'PORT': 5432}, 'engine': ''}}



class DatabaseTask(Task):
    _db = {}
    _all_customers = []
    _all_state = []
    _all_rules = []

    @property
    def all_rules(self):
        if self._all_rules == []:
            print("Initiate rules list - ONCE")
            self._all_rules = load_config.csv2dict
        return self._all_rules



    @property
    def all_customers(self):
        if self._all_customers == []:
            print("Initiate Customer list - ONCE")
            self._all_customers = load_config.customers_list
        return self._all_customers


    @property
    def db(self):
        if self._db == {}:
            print("Initiate Db connection - ONCE")
            for db_name,db_details in db_connections.items():
               # print("Init with",db_name, db_details['connection_details'])
                db_engine =  DBContext().get_db(db_details['connection_details']) 
                if db_engine:
                    self._db[db_name] = db_engine.get_engine()
                   
        return self._db
     

@app.task(bind=True ,base=DatabaseTask,  name='test_db')
def proccess_customer(self, *args, **kwargs):
    import loadCsv.utils as utl
    from sqlalchemy.sql import text
    from sqlalchemy.exc import OperationalError,ProgrammingError
    import pandas as pd

    customer_id = kwargs.get('customer_id')
    
    return "Test"


    table_name = kwargs.get('table_name')
    conn = kwargs.get('conn_target')  
    utl.init_customer()


    conn_source = self.db['postgres']
    conn_target = self.db['target']

    sql = text('SELECT * from customer')
    query = conn_source.execute(sql)


    df = pd.DataFrame(query.fetchall())
    utl.df_to_table(base=self, df=df, table_name='aaaa', conn_target=conn_target ,params="replace")
    print("All good",self._all_state)
    # try:
        
    #     res = df.to_sql('target_test', conn_source, if_exists= 'replace')
    #     print("Trying" , res , self.__name__)
    #     conn_source.commit()
   
    # except (sqlaclchemy.exc.ProgrammingError, sqlalchemy.exc.OperationalError) as e:
    #     logger.Info('Error occured while executing a query {}'.format(e.args))

    return "Ok"








# @app.task(bind=True , name='read_input_csv')
# def proccess_customers(self,customers, mapping_rules):
#     return group([load_data.delay(customer, mapping_rules) for customer in customers])











# @app.task(bind=True , name='route_load_type')
# def route_load_type(self,*args,**kwargs):
#     curr_customer = args[0]
#     mapping_rules = kwargs['mapping_rules']
#     # print("mapping_rules", mapping_rules)
#     print("Proccess customer:" , curr_customer  )
#     for rule in mapping_rules:

#         if rule['rules']['source_type'] == 'db':
#             sql = rule['rules']['sql']
#             sql = sql.replace("&1",str(curr_customer))
#             time.sleep(4)
#             print("DB proccess for ", sql)
#             load_from_db.delay(k="Sending ->" + str(curr_customer))
#             # rule.update({'key':curr_customer})
#             # print(rule['rules']['db_connection_source'])
#             time.sleep(3)



# @app.task(bind=True , name='load_from_db')
# def load_from_db(self,*args,**kwargs):
#     time.sleep(4)
#     print(kwargs['k'])
#     return "Last"
#     # return group([load_data.delay(customer, mapping_rule) for customer in customers])
