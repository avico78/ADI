from settings import Settings
from pathlib import Path
from sqlalchemy.sql import text
import sys
from pathlib import Path

import pandas as pd


from loader_config import LoadConfig
from db_config.config import DBContext


config_file = Path('app_config', 'config.yaml')
settings = Settings(config_file=config_file)



def clearn_target(setting=settings):
    
    sql =   '''SELECT tablename FROM pg_catalog.pg_tables 
            WHERE schemaname='public' ;'''

    target_db = settings.get('databases.target')
    engine = DBContext().get_db(target_db)
    engine_connected = engine.get_engine()
    temp_tables = pd.read_sql(sql, engine_connected)['tablename']
    print("Table to drop", temp_tables)
    with engine_connected as con:
        for table in temp_tables:
            sql = text(f"DROP table {table} CASCADE")
            con.execute(sql)
            print(f"Dropped table {table}.")

