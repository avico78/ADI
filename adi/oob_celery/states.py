from enum import Enum


class State(str, Enum):
    SCHEDULED = "Scheduled"
    RUNNING = "Running"
    FINISHED = "Finished"
    CANCELLED = "Cancelled"
    FAILED = "Failed"