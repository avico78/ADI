
import sys
import logging
import time
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from celery import group,chord,chain
from loadCsv.worker import app

logger = logging.getLogger(__name__)

@app.task(bind=True , name='test_load')
def test_load(*args,**kwargs):
        print("TesT Load !!!", kwargs['a'])  
        return 100

@app.task(bind=True , name='read_input_csv')
def proccess_customers(self,customers, mapping_rules):
    return group([load_data.delay(customer, mapping_rules) for customer in customers])

@app.task(bind=True , name='load_data')
def load_data(self,customer,mapping_rules: dict):
    print("in func")
    for rule in mapping_rules:
        rule.update({'key':customer})
        print(rule['rules']['db_connection_source'])
        time.sleep(10)
   
    # return group([load_data.delay(customer, mapping_rule) for customer in customers])