from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class DBType(str, Enum):
    POSTGRES = "postgres"
    SQLITE = "sqlite"


class DBFactory(ABC):

    @staticmethod
    @abstractmethod
    def get_db(config: Dict):
        pass

    @staticmethod
    @abstractmethod
    def initialize_db(config: Dict):
        pass


class PostgresFactory(DBFactory):

    @staticmethod
    def initialize_db(config: Dict):
        # note that this can be split into classes or separate methods
        # here you can do al preparations, make sure all libraries are imported
        # if you want to import some libs only if a given task type is used etc.
        pass

        # if config.get('source') == 'csv':
        #     if not os.path.isfile(config.get('task_params').get('path')):
        #         raise FileNotExists("File with given path does not exists!")

    @staticmethod
    def get_db(config: Dict):
        # here you actually return the task
        print("Postgres DB")
        # DataLoadFactory.initialize_task(config)
        # return Task(config=config)


class SqlLiteFactory(DBFactory):

    @staticmethod
    def initialize_db(config: Dict):
        pass

    @staticmethod
    def get_db(config: Dict):
        print("get DB")

        # return Task(config=config)

class DBContext:
    available_factories = {
        DBType.POSTGRES: PostgresFactory,
        DBType.SQLITE: SqlLiteFactory
    }

    @staticmethod
    def get_db(config: Dict) -> "DbSettings":
        db_type = config.get('DB_TYPE')
        factory = DBContext.available_factories.get(db_type)
        if factory is None:
            raise ValueError(f"No factory for task type: {db_type}")
        return factory

# db_test = { 'DB_TYPE': 'Postgres'}
#
# test = DBContext()
# test.get_db(db_test)





# class DbSettings(metaclass=SingletonMeta):
#     pass
#
#     def __init__(self, *args, **kwargs):
#         self.kwargs = kwargs
#     def testkwargs(self):
#         return self.kwargs
    #
    #     self.db_session = db_session
    #     self.query = query
    # async def execute_query(self):
    #     return await database.fetch_all(query=self.query)
