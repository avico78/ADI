import os
from abc import ABC, abstractmethod
from typing import Dict

# from exceptions import FileNotExists
from task import Task


class TaskFactory(ABC):

    @staticmethod
    @abstractmethod
    def get_task(config: Dict):
        pass

    @staticmethod
    @abstractmethod
    def initialize_task(config: Dict):
        pass


class DataLoadFactory(TaskFactory):

    @staticmethod
    def initialize_task(config: Dict):
        # note that this can be split into classes or separate methods
        # here you can do al preparations, make sure all libraries are imported
        # if you want to import some libs only if a given task type is used etc.
        settings = config

        # if config.get('source') == 'csv':
        #     if not os.path.isfile(config.get('task_params').get('path')):
        #         raise FileNotExists("File with given path does not exists!")

    @staticmethod
    def get_task(config: Dict):
        # here you actually return the task
        DataLoadFactory.initialize_task(config)
        return Task(config=config)


class DataTransformationFactory(TaskFactory):

    @staticmethod
    def initialize_task(config: Dict):
        pass

    @staticmethod
    def get_task(config: Dict):
        return Task(config=config)