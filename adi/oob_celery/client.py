from settings import Settings
from pathlib import Path
import json
import sys
from pathlib import Path

from loader_config import LoadConfig
from customer import Customer

import asyncio

config_file = Path('app_config', 'config.yaml')





""" setting class holds all required parameters deails as db details , customer list , files path,
it based on dot notation and has get method support get nested level as get('param1.param2.param3)   """

settings = Settings(config_file=config_file)

""" just a direct path to rules in yaml"""
rules = 'application_conig.rules.'


""" LoadConfig load mapping rules (source1.csv) , prepare config (mapping rules based the csv) also db connection 
(check all rules and prepare list of required db's) ,  customer list and etc """

config = LoadConfig(settings=settings)
config.initialize_operation()


rules = config.load_config['csvdict']

#required db connections
db_connections = config.load_config['db_connections']


f = open('celery_app/config_load.py','w')
f.write(json.dumps(db_connections))
f.close()

# print(json.dumps(rules[0]))

# exit()
# import time
# time.sleep(1)
# a = init_db_connections()
# print("From main" ,a)
# time.sleep(11)


customers = [111,222,333]


async def main():
    for customer in customers:

        cust = Customer(id=customer)    
        cust.load_tasks(configs=rules ,db_connections=db_connections)
        asyncio.run(cust.run())
        for task in cust.executed_tasks:
            print(task.task_run.state)
        print(cust.state)
        
asyncio.run(main())





#######['TimeoutError', '__class__', '__copy__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_args__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cache', '_get_task_meta', '_ignored', '_iter_meta', '_maybe_reraise_parent_error', '_maybe_set_cache', '_on_fulfilled', '_parents', '_set_cache', '_to_remote_traceback', 'app', 'args', 'as_list', 'as_tuple', 'backend', 'build_graph', 'children', 'collect', 'date_done', 'failed', 'forget', 'get', 'get_leaf', 'graph', 'id', 'ignored', 'info', 'iterdeps', 'kwargs', 'maybe_reraise', 'maybe_throw', 'name', 'on_ready', 'parent', 'queue', 'ready', 'result', 'retries', 'revoke', 'state', 'status', 'successful', 'supports_native_join', 'task_id', 'then', 'throw', 'traceback', 'wait', 'worker']