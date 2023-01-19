from app_config.settings import Settings
from app_config.db_config import DBContext
from app_config.task import Task
import os
from pathlib import Path
global parent_dir
parent_dir = Path('.').absolute()

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print("m", parent_dir)
    settings = Settings()
    exit()
    source_db = DBContext().get_db(settings.get('databases.postgres'))
    rules_folder= settings.get('application_conig.rules.folder')
    rules_files = settings.get('application_conig.rules.files')

    task_list = []
    for rule_file in rules_files:
        file_path = f'{working_directory}{rules_folder}/{rule_file})'
        print("curr ", file_path)
        task_list.append(Task(file_path))
    #
    # for task in task_list:
    #     print(task.load_rules())

    # print(source_db.get_engine())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
