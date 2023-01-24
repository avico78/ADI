import pandas as pd
from pathlib import Path
import os
from pathlib import Path




    # file exists
class TaskRule:
    def __init__(self , config_file):
        self.config_file = config_file
        os_ = os.path.dirname(os.path.abspath(__file__))
        p_ = os.path.abspath(os.getcwd())

    def load_rules(self):
        return pd.read_csv(self.config_file)

class Task(TaskRule):
    def __init__(self , config_file):
        TaskRule.__init__(self, config_file)

#
# t = Task('rules/source_1.csv')
# print(t.load_rules())