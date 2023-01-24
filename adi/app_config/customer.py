import pandas as pd
from typing import NewType

CustomerDF = NewType('CustomerDF', pd.DataFrame())


class Customer:

    def __init__(self):
        self.customer_id = None
        self.running : bool = None
        self.customer_df :CustomerDF = None

    def load_2df(self):
        pass

    def load_2db(self):
        pass



class CustomerDataCollector:

    def __init__(self):
        self.data_source = None
        self.db_connection = None
        self.customers_list : list = list(Customer)


