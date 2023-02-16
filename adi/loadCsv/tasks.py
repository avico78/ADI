
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from loadCsv.worker import app

def is_celery_working():
    result = app.control.broadcast('ping', reply=True, limit=1)
    return bool(result)  # True if at least one result



def get_celery_worker_status():
    i = app.control.inspect()
    availability = i.ping()
    stats = i.stats()
    registered_tasks = i.registered()
    active_tasks = i.active()
    scheduled_tasks = i.scheduled()
    result = {
        'availability': availability,
        'stats': stats,
        'registered_tasks': registered_tasks,
        'active_tasks': active_tasks,
        'scheduled_tasks': scheduled_tasks
    }
    return result

# print(is_celery_working())
# print(get_celery_worker_status())



# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent))
# from loadCsv.worker import app
# import time
# from celery import group,chord,chain

# from threading import Thread

# import logging
# logger = logging.getLogger(__name__)

# @app.task(bind=True, name='jpr')  
# def jpr(self):  
#     print("Hellow from jpr")

# @app.task(bind=True, name='load_csv')  
# def load_csv(self, x):
#         print("Hi", x)
#         return "load_csv_" + str(x)

# @app.task(bind=True, name='avi')  
# def avi(self, customer):  
#     return load_customer(customer) 


# @app.task(bind=True, name='load_customer')  
# def load_customer(self, customer):
#         if customer % 2 == 0:
#             return evennum(customer)
#         else:
#             return oddnum(customer)

# @app.task(bind=True , name='evennum')
# def evennum(self,num):
#     # time.sleep(5)
#     return "even_customer" + str(num)

# @app.task(bind=True , name='oddnum')
# def oddnum(self,num):
#     # time.sleep(5)    
#     t1 = Thread(target=jpr)
#     t2 = Thread(target=jpr)
#     t1.start()
#     time.sleep(3)
#     t2.start()
#     t1.join()
#     t2.join()
#     return "odd_customer" + str(num)

# @app.task(bind=True , name='read_input_csv')
# def proccess_customers(self,customers, mapping_rules):
#     return group([load_data.delay(customer, mapping_rules) for customer in customers])

# @app.task(bind=True , name='load_data')
# def load_data(self,customer,mapping_rules: dict):
#     for rule in mapping_rules:
#         rule.update({'key':customer})
#         print(rule['rules']['db_connection_source'])
#         time.sleep(10)
   
#     # return group([load_data.delay(customer, mapping_rule) for customer in customers])


# # class LoadManager(app.Task):
# #     name = "LoadManager"
# #     ignore_result = False
# #     def __call__(self, *args, **kwargs):
# #         """In celery task this function call the run method, here you can
# #         set some environment variable before the run of the task"""
# #         # oddnum.delay(1).get()
# #         self.loadconfigurator = None
# #         self.keys = kwargs.get('keys',[1,2])
# #         self.mapping_rules = kwargs.get('mapping_rules',[{'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM customer1 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '1'}}, {'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM rental1 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '1'}}, {'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM customer2 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '3'}}, {'key': '', 'rules': {'db_connection_source': 'source_ps', 'sql': 'SELECT * FROM rental2 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '3'}}])
# #         proccess_customers.delay(self.keys ,self.mapping_rules)

# #         return self.run(*args, **kwargs)

# #     def after_return(self, status, retval, task_id, args, kwargs, einfo):
# #         #exit point of the task whatever is the state
# #         print("AFTEr")
# #         pass

# # class AddTask(LoadManager):

# #     def run(self,*args, **kwargs):
# #         logger.info(f'AddTask = {kwargs}')
# #         # logger.error('No x or y in arguments')

# # app.register_task(AddTask())








# # class CustomerTable(app.Task):
# #     name = "CustomerTable"
# #     ignore_result = False
    

# #     def run(self, *args, **kwargs):
# #         self.row_num = None
# #         self.source_db_connection = None
# #         self.source_table = None
# #         self.query = None
# #         return self.generate_file(kwargs['a'])

# #     def generate_file(self, data):
# #         return data.capitalize()
    
# #     def collect_data(self):
# #         data = "avi celery"
# #         return data

# # app.register_task(CustomerTable())


# # #a = AddTask().delay("Hello")

# # # class CustomerData(app.Task):
    

    
# # # app.register_task(CustomerTable())

