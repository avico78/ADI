from app_config.settings import Settings
from app_config.db_config import DBContext
def main(name):
    # Use a breakpoint in the code line below to debug your script.
    settings = Settings()
    print(settings.get('databases.postgres'))
    exit()
    source_db = DBContext().get_db(settings.get('databases.postgres'))
    print(source_db.get_db())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
