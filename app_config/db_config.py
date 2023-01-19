from app_config.settings import SingletonMeta
from typing import Dict
from enum import Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.sql import text

class DBType(str, Enum):
    POSTGRES = "postgres"
    SQLITE = "sqlite"



class PostgresFactory(metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):

        self.db_type = kwargs['DB_TYPE']
        self.name = kwargs['NAME']
        self.user = kwargs['USER']
        self.password = kwargs['PASSWORD']
        self.host = kwargs['HOST']
        self.port = kwargs['PORT']
        self.engine = None
        self.postgress_db_string = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
                               self.user,
                               self.password,
                               self.host,
                               self.port,
                               self.name )
        print("Postgres",self.postgress_db_string)
        try:
            self.engine = create_engine(self.postgress_db_string)
            print("Connection to the {self.host} for user {self.user} created successfully.")
        except Exception as error:
            print("Error: Connection not established {}".format(error))

      #  self.Session = sessionmaker(bind=self.engine)
    def get(self):
        return self.engine


    #
    # def __enter__(self):
    #
    #     self.connection = create_engine(postgress_db_string)
    #     return self.connection
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if exc_type or exc_tb or exc_tb:
    #         self.connection.close()
    #     self.connection.commit()
    #     self.connection.close()

    def initialize_db(config: Dict):
        # note that this can be split into classes or separate methods
        # here you can do al preparations, make sure all libraries are imported
        # if you want to import some libs only if a given task type is used etc.
        pass

        # if config.get('source') == 'csv':
        #     if not os.path.isfile(config.get('task_params').get('path')):
        #         raise FileNotExists("File with given path does not exists!")

    def get_db(self):
        print("get DB", self.port)


class SqlLiteFactory(metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
    @staticmethod
    def initialize_db(config: Dict):
        pass

    @classmethod
    def get_db(self):
        print("get DB", self.kwargs)

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
        return factory(**config)

db_test = {'DB_TYPE': 'postgres', 'ENGINE': 'postgres', 'NAME': 'demo', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': 'postgres', 'PORT': 5432}
#
test = DBContext.get_db(db_test)
sss = test.get()

print(sss)
exit()
import pandas as pd
sql = '''
    SELECT * FROM actors;
'''
with sss.connect().execution_options() as conn:
    query = conn.execute(text(sql))
df = pd.DataFrame(query.fetchall())


#
# import pandas as pd
# with test as conn:
#      data =  pd.read_sql("select * from actor ", conn.connector)





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
