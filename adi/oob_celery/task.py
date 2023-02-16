from typing import Dict, List
from states import State
from celery_app.tasks_2 import proccess_rule

class Task:
#rule_id,source_type,source_name,sql,target_type,target_name,order
    def __init__(self , config:Dict, db_connections:Dict  ) :

        self.customer = None
        self.rule_id =  config.get('rule_id')
        self.source_type = config['rules'].get('source_type')
        self.source_name = config['rules'].get('source_name')
        self.sql =  config['rules'].get('sql')
        self.sql_render = None        
        self.target_type =  config['rules'].get('target_type')
        self.target_name=  config['rules'].get('target_name')
        self.order =  config['rules'].get('order')
        self.state = State.SCHEDULED
        self.result = None
        self.task_run = None
        self.task_celery_id = None
    def initialize_task(self):
        self.sql_render = self.sql.replace("&1",str(self.customer.id))        
        
    def run(self):
        self.task_run = proccess_rule.delay(rule_id=self.rule_id, main_id=self.customer.id,source_type=self.source_type,source_name=self.source_name,sql=self.sql_render,
                                               target_type=self.target_type,target_name=self.target_name,   order=self.order)
        self.task_celery_id = self.task_run.task_id

        self._update_customer()
        

    def _update_customer(self):
        self.customer.executed_tasks.append(self)

