from typing import Dict
from task import Task


def load_task(config:Dict) -> Task:
    return Task(config=config)


