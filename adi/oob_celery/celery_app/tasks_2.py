
import sys
import logging
import time
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from celery import group,Task
from celery_app.worker import app
from celery.utils.log import get_task_logger      
from db_config.config import DBContext




from celery_app.celery_param_base import CeleryParams  


logger = get_task_logger(__name__)


with open('celery_app/config_load.py') as f:
    db_connections = json.load(f)


# db_connections = {'postgres': {'connection_details': {'DB_TYPE': 'postgres', 'ENGINE': 'postgres', 'NAME': 'dvdrental', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': '192.168.1.113', 'PORT': 5432}, 'engine': ''}, 'target': {'connection_details': {'DB_TYPE': 'postgres', 'ENGINE': 'postgres', 'NAME': 'target', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': '192.168.1.113', 'PORT': 5432}, 'engine': ''}}

class Test:
    _avi='Avi'

    @property
    def avi(self):
        return self._avi.upper()


class DatabaseTask(Test,Task):
    _db = {}
    _all_customers = []
    _all_state = []
    _all_rules = []
    _init_ind = False
    
    @property
    def is_init(self):    
        if self._init_ind is False:
            self._init_ind = True
        return self._init_ind
        
    

    @property
    def all_rules(self):
        if self._all_rules == []:
            print("Initiate rules list - ONCE")
            self._all_rules = "Test"
        return self._all_rules



    @property
    def all_customers(self):
        if self._all_customers == []:
            print("Initiate Customer list - ONCE")
            self._all_customers = [1,2,3]
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




@app.task(bind=True, base=DatabaseTask, name='init_db_connections2')
def init_db_connections2(self, **kwargs):
    print("sel" ,self.db['postgres'])

    return "ok"


@app.task(bind=True, base=DatabaseTask, name='init_db_connections')
def init_db_connections(self, **kwargs):

    import celery_app.utils as utl
    utl.init_config(base=self,**kwargs)
    logger.info('InitDB Completed ')    
    return "init completed"


@app.task(bind=True ,base=DatabaseTask,  name='proccess_rule')
#rule_id=self.rule_id, source_type=self.source_type,
                                                # db_connection_name=self.db_connection_name, target_type=self.target_type,
                                                # order=self.order
def proccess_rule(self, *args, **kwargs):
    from celery_app.utils import load_operation,operators,init_config
    from sqlalchemy.sql import text
    from sqlalchemy.exc import OperationalError,ProgrammingError
    import pandas as pd
    import time
    import random
    rule_id = kwargs.get('rule_id')
    main_id = kwargs.get('main_id')
    source_type = kwargs.get('source_type')
    source_name = kwargs.get('source_name')
    source_object_name = kwargs.get('source_object_name')
    sql = kwargs.get('sql')
    target_name = kwargs.get('target_name')
    target_object_name = kwargs.get('target_object_name')
    target_type = kwargs.get('target_type')
    order = kwargs.get('order')


    df_source = None
    db_connection = None
    print("type db!!!!!!!" , target_type)
    if source_type == 'db':
        db_connection = self.db[source_name]
        df = load_operation.load_table_from_db(conn=db_connection, sql=sql)
        print("source",db_connection)
    if target_type.strip() == 'db':
        print("Back from Load!!!!!!", df_source)
        db_connection = self.db[target_name]       
        print("source",db_connection)
        load_operation.df_to_table(conn=db_connection, table_name=target_object_name ,df=df ,if_exists='append')


    #time.sleep(random.randint(0,7))
    return 1


   # customer_id = kwargs.get('customer_id')
#    time.sleep(1)
    # table_name = kwargs.get('table_name')
    # conn = kwargs.get('conn_target')  
     


    # conn_source = self.db['postgres']
    # conn_target = self.db['target']

    # sql = text('SELECT * from customer')
    # query = conn_source.execute(sql)


    # df = pd.DataFrame(query.fetchall())
    # utl.df_to_table(base=self, df=df, table_name='aaaa', conn_target=conn_target ,params="replace")
    # print("All good",self._all_state)
    # # try:
        
    # #     res = df.to_sql('target_test', conn_source, if_exists= 'replace')
    # #     print("Trying" , res , self.__name__)
    # #     conn_source.commit()
   
    # # except (sqlaclchemy.exc.ProgrammingError, sqlalchemy.exc.OperationalError) as e:
    # #     logger.Info('Error occured while executing a query {}'.format(e.args))

    # return "Ok"





# init_db_connections2.delay()



# @app.task(bind=True , name='read_input_csv')
# def proccess_rules(self,customers, mapping_rules):
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

