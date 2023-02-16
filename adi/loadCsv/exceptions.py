class WorkflowException(Exception):
    pass


class WrongDataSourceProvided(WorkflowException):
    pass


class FileNotExists(WrongDataSourceProvided):
    pass


class WorkflowConfigurationError(WorkflowException):
    pass


class UnknownOperator(WorkflowException):
    pass