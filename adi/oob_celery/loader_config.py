
import csv
import sys
import json



# from loadCsv.load_manager import LoadManager

rules = 'application_conig.rules.'

class LoadConfig:

    def __init__(self , settings) :
        
        self.settings = settings
        self.customers_list = self.settings.get(f'{rules}customers_list')
        self.files = self.settings.get(f'{rules}files')[0]
        self.files_path = self.settings.get(f'{rules}folder')  
        self.mapping_rule_file = self.files_path + '/' + self.files
        self.load_config:dict = {}
        self.operation = None

        self.csv2dict = {}
        self.db_connections = []
        self.load_manager = None


    def __repr__(self):       
        return json.dumps(self.load_config)

    def run(self):

        # print("Run",json.dumps((self.load_config)))
       
        # return group([ avi.delay(customer) for customer in self.customers_list])
        #LoadManager().delay(config=(self.load_config))
        return 


    def initialize_operation(self):
        self.csv2dict = self._convertcsv2dict(self.mapping_rule_file)
     
        self.load_config = { 'csvdict' :self.csv2dict,
                        'customers_list': self.customers_list }


        db_connection = {}
       
        for rule in self.csv2dict:
          
            if rule is not None:
                if rule['rules']['source_type'] == 'db':
                    # Updating all required db connection    
                    db_name = rule['rules']['source_name']
                    db_connection[db_name] =  { 'connection_details' : self.settings.get('databases.' + db_name),'engine' : ''}


        self.db_connections = db_connection
        
        self.load_config['db_connections'] = db_connection
       

    def prepare_celery_config(self):
        db_config = self.load_config['db_connections']
      
        for db_name , db_details in db_config.items():
            print(db_name ,db_details)


    def get_db_connections(self):
        return self.db_connections


    @staticmethod
    def _convertcsv2dict(file_path):
        """ Function will conevert the csv to dict format where each column in csv would be key in the dict
            In exampe table_name,connection would be { 'table_name': <param>, 'connection': <parama> }"""
            
        content = []
        rule_id = 1
        with open(file_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            for row in csv_reader:
                row_data = {key: value for key, value in zip(headers, row)}
                updated_row = {}
                updated_row.update({'rule_id': rule_id, 'rules':row_data})
                content.append(updated_row)  
                rule_id += 1
                
        sorted_mapping_rules = sorted(content, key=lambda d: d['rules']['order']) 
                   
        return sorted_mapping_rules

    def load(self):
        pass
         
         #return group([ avi.delay(customer) for customer in self.customers_list])
    
        # res = load_csv.delay(files)
        # print(res.get())


# load_config.initialize_operation()

# print(load_config.csv2dict)

# db_all = {}
# for db_name,db_details in load_config.db_connections.items():
#     print("Here --> \n", db_name ,db_details['connection_details'])
#     db_engine =  DBContext().get_db(db_details['connection_details'])    
#     db_all[db_name] = db_engine
#     # print("DB connections is",db_engine)
# # load_config.initialize_operation()


# if __name__ == "__main__":


#     settings = {'csvdict': [{'key': '', 'rules': {'source_type': 'db', 'source_name': 'postgres', 'db_connection_name': 'source_ps', 'sql': 'SELECT * FROM customer1 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '1'}}, {'key': '', 'rules': {'source_type': 'db', 'source_name': 'postgres', 'db_connection_name': 'source_ps', 'sql': 'SELECT * FROM rental1 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '1'}}, {'key': '', 'rules': {'source_type': 'db', 'source_name': 'postgres', 'db_connection_name': 'source_ps', 'sql': 'SELECT * FROM customer2 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '3'}}, {'key': '', 'rules': {'source_type': 'db', 'source_name': 'postgres', 'db_connection_name': 'source_ps', 'sql': 'SELECT * FROM rental2 where customer=&1 ', 'target_type': 'df ', 'db_connection_target': ' file ', 'order': '3'}}], 'customers_list': [1, 2, 3, 4, 5, 6, 7], 'db_connections': {'postgres': {'connection_name': 'source_ps', 'engine': <app_config.db_config.PostgresFactory object at 0x7f5fc2548460>}}}
#     # config = settings
#     # path = '/csv_files'
#     # files = ['source1.csv']
#     x1 = LoadConfig(settings=settings)
#     x1.initialize_operation()
#     # # x1.set_db_connection()
#     # print("here",x1.db_connection)