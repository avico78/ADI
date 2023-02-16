import sys
import logging
import time
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from celery_app.utils.df_func import df_to_table
from celery_app.utils.load_operation import load_table



load_operators = {
    "load_table": load_table,

}

operators = {
    "df_to_table": df_to_table,

}


def init_config(*args, **kwargs):
    base_init = kwargs.get('base')
    db_to_init = kwargs.get('init_db')
    base_init.db[db_to_init]
    print("init customer completed")
    return

