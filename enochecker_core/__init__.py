from dataclasses import dataclass
from enum import Enum
from typing import Optional, Callable, Any, Dict, List, Union, Type

class CheckerTaskResult(Enum):
    CHECKER_TASK_RESULT_OK = "OK"
    CHECKER_TASK_RESULT_MUMBLE = "MUMBLE"
    CHECKER_TASK_RESULT_DOWN = "OFFLINE"
    CHECKER_TASK_RESULT_INTERNAL_ERROR = "INTERNAL_ERROR"

    def __str__(self):
        return self.value

class CheckerTaskType(Enum):
    CHECKER_TASK_TYPE_PUTFLAG = "putflag"
    CHECKER_TASK_TYPE_GETFLAG = "getflag"
    CHECKER_TASK_TYPE_PUTNOISE = "putnoise"
    CHECKER_TASK_TYPE_GETNOISE = "getnoise"
    CHECKER_TASK_TYPE_HAVOC = "havoc"

    def __str__(self):
        return self.value

@dataclass
class CheckerInfoMessage:
    serviceName: str
    flagCount: int
    havocCount: int
    noiseCount: int

@dataclass
class CheckerResultMessage:
    result: str

@dataclass
class EnoLogMessage:
    tool: str
    type: str
    severity: str
    timestamp: str
    module: str
    function: str
    flag: Optional[str]
    flagIndex: Optional[int]
    runId: Optional[int]
    round: Optional[int]
    message: str
    teamId: Optional[str]
    teamName: Optional[str]
    serviceId: Optional[str]
    serviceName: str

@dataclass
class CheckerTaskMessage:
    runId: int
    method: str
    address: str
    serviceId: int
    serviceName: str
    teamId: int
    team: str
    relatedRoundId: int
    round: int
    flag: Optional[str]
    flagIndex: Optional[int]

class BrokenServiceException(Exception):
    pass

class OfflineException(Exception):
    pass
