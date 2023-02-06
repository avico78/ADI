from .tasks import AddTask,load_csv
class LoadCsv:
    def __init__(self , setting , files, path, Thread=2 ) -> None:
        self.settings = setting
        self.files = files
        self.path = path
        self.load()
    def load(self):
        for file in self.files:
            a = load_csv().delay(files=file)
            print("Hi",a.get())
        # res = load_csv.delay(files)
        # print(res.get())



# if __name__ == "__main__":
#     settings = "{'config_file': PosixPath('app_config/config.yaml'), 'settings': {'PROJECT_NAME': 'ADI', 'application_conig': {'db_archive': '/db_archive', 'rules': {'folder': '/csv_files', 'files': ['source1.csv'], 'customers_list': [1, 2, 3, 4, 5, 6, 7]}}, 'databases': {'mongo': {'DB_TYPE': 'mongodb', 'ENGINE': 'mongodb', 'DRIVER': 'motor', 'NAME': 'webserver', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': 'mongo_db', 'PORT': 27017, 'DROP_COLLECTION_ON_START': ['sdad'], 'DB_PREPARATION': {'security': {'index': 'username email'}, 'customer': {'index': 'customer_no email'}}, 'WATCH': ['customer', 'test']}, 'postgres': {'DB_TYPE': 'postgres', 'ENGINE': 'postgres', 'NAME': 'dvdrental', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': '192.168.1.113', 'PORT': 5432}, 'redis': {'host': 'redis_db', 'port': 6379, 'db': 0}}, 'files': {'default': {'input_file_path': '/webserver/input/', 'output_file_path': '/webserver/output/'}}, 'security': {'trace_request': 'Y'}}}"
#     path = '/csv_files'
#     files = ['source1.csv']
#     LoadCsv(setting=settings,files=files ,path=path)