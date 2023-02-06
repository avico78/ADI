
import csv
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))



from celery import group

from loadCsv.load_manager import LoadManager
from app_config.db_config import DBContext
from app_config.settings import Settings


rules = 'application_conig.rules.'

class LoadConfig:


    def __init__(self , config , files, path,customers_list, Thread=2 ) -> None:
        self.operation = None
        self.settings = config
        self.customers_list = customers_list
        self.files = files[0]
        self.path = path
        self.csv2dict = self._convertcsv2dict()
        self.db_connection = {}
        self.load_manager = None

    def run(self):
        print("Run")
        # return group([ avi.delay(customer) for customer in self.customers_list])
        #self.load_manager = LoadManager.delay
    def initialize_operation(self):

        for rule in self.csv2dict:
            if rule is not None:
                if rule['rules']['source_type'] == 'db':
                    # Updating all required db connection    
                    db_name = rule['rules']['source_name']
                    db_connection_name = rule['rules']['db_connection_name']
                    db_engine =  DBContext().get_db(settings.get('databases.postgres')) 
                  
                    self.db_connection[db_name] = { 'connection_name' :db_connection_name,'engine' : db_engine}

                    # print(rule['rules']['db_connection_name'])
                    # db_name =  self.db_connection[rule['rules']['source_name']]
                    # db_connection =  rule['rules']['db_connection_name']
                    # DBContext().get_db(settings.get('databases.' + db_name ))       
                    # self.db_connection[rule['rules']['source_name']] = "{ 'connection_name' = rule['rules']['db_connection_name'],'engine' = ''}"

    def _convertcsv2dict(self):
        import json
        from collections import OrderedDict
        from operator  import itemgetter
        content = []
        with open('loadCsv' + self.path + '/' + self.files) as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            for row in csv_reader:
                row_data = {key: value for key, value in zip(headers, row)}
                updated_row = {}
                updated_row.update({'key':'' , 'rules':row_data})
                content.append(updated_row)  
        sorted_mapping_rules = sorted(content, key=lambda d: d['rules']['order']) 
                           
        return sorted_mapping_rules

    def load(self):
         return group([ avi.delay(customer) for customer in self.customers_list])
    
        # res = load_csv.delay(files)
        # print(res.get())



if __name__ == "__main__":
    config_file = Path('app_config', 'config.yaml')
    settings = Settings(config_file=config_file)
    config = settings
    path = '/csv_files'
    files = ['source1.csv']
    x1 = LoadConfig(config=config,files=files ,path=path ,customers_list=[1,2,3])
    x1.initialize_operation()
    # x1.set_db_connection()
    print("here",x1.db_connection)