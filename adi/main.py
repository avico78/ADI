from app_config.settings import Settings
from app_config.db_config import DBContext
from pathlib import Path
from loadCsv.tasks import CustomerTable,AddTask,load_csv
from loadCsv.client import LoadConfig
from loadCsv.tasks_2 import test_load
config_file = Path('app_config', 'config.yaml')

rules = 'application_conig.rules.'


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    settings = Settings(config_file=config_file)

    customers_list = settings.get(f'{rules}customers_list')
    files = settings.get(f'{rules}files')
    folder_path = settings.get(f'{rules}folder')
    source_db = DBContext().get_db(settings.get('databases.postgres'))
    print(source_db)
    exit()
    # a = LoadConfig(setting=settings, files=files, customers_list=customers_list, path=folder_path))
    res = AddTask().delay(1,2)
    print(res.get())
    # LoadCsv(setting=settings)
    # a = CustomerTable().delay(a="aaaaaaaaa")
    # print(a.get())
    exit()
    source_db = DBContext().get_db(settings.get('databases.postgres'))
    rules_folder= settings.get(f'{rules}folder')
    rules_files = settings.get(f'{rules}files')

    task_list = []
    # for rule_file in rules_files:
    #     file_path = f'{working_directory}{rules_folder}/{rule_file})'
    #     print("curr ", file_path)
    #     task_list.append(Task(file_path))
    #
    # for task in task_list:
    #     print(task.load_rules())

    # print(source_db.get_engine())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main('ADI')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
