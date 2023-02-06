from app_config.settings import Settings
# from app_config.db_config import DBContext
from pathlib import Path
# from loadCsv.tasks import CustomerTable,AddTask,load_csv
# from loadCsv.client import LoadCsv
# from loadCsv.tasks_2 import test_load
config_file = Path('app_config', 'config.yaml')

rules = 'application_conig.rules.'


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    settings = Settings(config_file=config_file)
    print(settings.__new__)
  
if __name__ == '__main__':

    main('ADI')
 
