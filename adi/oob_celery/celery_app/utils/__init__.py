import sys
import logging
import time
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from celery_app.utils.df_func import *
from celery_app.utils.load_operation import *

from celery.utils.log import get_task_logger 
logger = get_task_logger(__name__)

load_operators = {
    "load_table": load_table,
    "load_table_from_db": load_table_from_db,
}

operators = {
    "df_to_table": df_to_table,

}


def init_config(*args, **kwargs):
    base_init = kwargs.get('base')
    db_to_init = kwargs.get('init_db')
    try:
        base_init.db[db_to_init]
        logger.info('InitDB Completed ')   
    except (RuntimeError, TypeError, NameError) as e:
        logger.error('InitDB Error ' , e)   
    finally:
        logger.info('All good , init Completed ')   
    return 

