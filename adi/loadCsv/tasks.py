
from .worker import app
import logging
logger = logging.getLogger(__name__)

@app.task(bind=True, name='load_csv')  
def load_csv(self, x):
        print("Hi", x)
        return x


class MyCoolTask(app.Task):
    name = "MyCoolTask"
    ignore_result = False
    def __call__(self, *args, **kwargs):
        """In celery task this function call the run method, here you can
        set some environment variable before the run of the task"""
        self.test = 8
        return self.run(*args, **kwargs)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        #exit point of the task whatever is the state
        print("AFTEr")
        pass

class AddTask(MyCoolTask):

    def run(self,x,y):
        if x and y:
            result= x + y + self.test
            logger.info('result = %d' % result)
            print("Heeeeere", self.test)
            return result
        else:
            logger.error('No x or y in arguments')

app.register_task(AddTask())

class CustomerTable(app.Task):
    name = "CustomerTable"
    ignore_result = False
    

    def run(self, *args, **kwargs):
        self.row_num = None
        self.source_db_connection = None
        self.source_table = None
        self.query = None
        return self.generate_file(kwargs['a'])

    def generate_file(self, data):
        return data.capitalize()
    
    def collect_data(self):
        data = "avi celery"
        return data

app.register_task(CustomerTable())


# class CustomerData(app.Task):
    

    
# app.register_task(CustomerTable())

