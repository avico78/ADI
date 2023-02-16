from app_config.settings import Settings
# from app_config.db_config import DBContext
from pathlib import Path
# from loadCsv.tasks import CustomerTable,AddTask,load_csv
# from loadCsv.client import LoadCsv
# from loadCsv.tasks_2 import test_load
config_file = Path('app_config', 'config.yaml')
from loadCsv.tasks import is_celery_working,get_celery_worker_status

rules = 'application_conig.rules.'


def main(name):
    print(get_celery_worker_status())
    # Use a breakpoint in the code line below to debug your script.
    # settings = Settings(config_file=config_file)
    # a=is_celery_working.delay()
    # print(a.get())
  
if __name__ == '__main__':

    main('ADI')
 
