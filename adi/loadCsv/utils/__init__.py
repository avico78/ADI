import sys
import logging
import time
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from loadCsv.exceptions import UnknownOperator
from loadCsv.utils.df_func import df_to_table

operators = {
    "df_to_table": df_to_table,

}


def init_customer(*args, **kwargs):
    base_init = kwargs.get('base')

    base_init.all_customers
    base_init.all_rules
    print("init customer completed")
    return




def none_operator(*args, **kwargs):
    # this should probably be handled in tasks init to fail quick not at runtime
    raise UnknownOperator("Unknown operator passed!")