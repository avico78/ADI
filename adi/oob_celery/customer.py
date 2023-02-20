from typing import Dict, List, Optional
from states import State
from task import Task

import asyncio




        
class Customer:

    def __init__(self ,id:int ) -> None:
        self.id = id
        self.tasks: List["Task"] = []
        self.starting_tasks: List["Task"] = []
        self.executed_tasks: List["Task"] = []
        self.result = None
        self.state = State.SCHEDULED


    # async def print_lines(self):
    #     for i in range(1, 11):
    #         await asyncio.sleep(0.5)
    #         print(f'Line {i}')    

    def load_tasks(self , configs: List[Dict] ,db_connections:Dict):

        self.tasks = [ Task(config=config, db_connections=db_connections) for config in configs ]        
        self._initialize_customer_tasks()

    async def run(self):

        execute_task = asyncio.create_task(self.task_exec())
        monitor_progresss = asyncio.create_task(self.monitor_progress())

        await execute_task
        # print(len(self.executed_tasks))

        await monitor_progresss
        
        # for task in self.starting_tasks:
        #     await task.run()

     
    async def monitor_progress(self):
        import time
        print("In Monitor")
        failure_flag = False
        count_success = 0

        i = 0

        while True:
           
            state = self.executed_tasks[i].task_run.state 

            if state == 'SUCCESS':
                count_success += 1   
                print(f'***Main_ID:{self.id}*****\nRule_ID:{self.executed_tasks[i].rule_id} \
                        \nCelery_UUID:{self.executed_tasks[i].task_celery_id}\
                        \nstatus - {self.executed_tasks[i].task_run.state}')   
                i += 1

            if state == 'FAILURE':
                print(f'***Main_ID:{self.id}*****\nRule_ID:{self.executed_tasks[i].rule_id} \
                     \nCelery_UUID:{self.executed_tasks[i].task_celery_id}\
                      \nstatus - {self.executed_tasks[i].task_run.state}')
                failure_flag = True
                i += 1

            if i >= len(self.executed_tasks) -1:
                if failure_flag:
                    self.state = State.FAILED
                elif count_success == len(self.executed_tasks) :
                    self.state = State.FINISHED
                break;
            

            await asyncio.sleep(1)                        
            
            

    
    async def task_exec(self):
        for task in self.starting_tasks:
            task.run()     

    def find_task(self, task_id: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def _initialize_customer_tasks(self):
        for task in self.tasks:
            task.customer = self
            """ tasks passed sorted - case more sorting , or running bulk (group1,group2 ...) - to consider"""
            self.starting_tasks.append(task)
            task.initialize_task()