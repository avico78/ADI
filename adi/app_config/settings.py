import yaml
from functools import reduce
import operator
from pathlib import Path

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs ):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Settings(metaclass=SingletonMeta):

    def __init__(self, *args, **kwargs):
        self.config_file = kwargs['config_file']


        with open(self.config_file, "r") as stream:
            try:
                self.settings = yaml.safe_load(stream)

            except yaml.YAMLError as exc:
                print(exc)
    def get(self, element):
        return reduce(operator.getitem, element.split('.'), self.settings)


## adding sys.path.append(str(Path(__file__).parent.parent)) - will include the parent dir so can work directly
# or from main

# s1 = Settings(config_file='config.yaml')
# print(s1.get('databases.mongo.ENGINE'))

# if __name__ == "__main__":
#     # The client code.
#     config_file = Path('.', 'config.yaml')
#     s1 = Settings(config_file=config_file)

    # print(s1.get('databases.mongo.ENGINE'))
#     if id(s1) == id(s2):
#         print("Singleton works, both variables contain the same instance.")
#     else:
#         print("Singleton failed, variables contain different instances.")