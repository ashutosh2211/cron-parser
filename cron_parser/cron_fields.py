import re
from dataclasses import dataclass, field
from enum import Enum
from typing import List


class CronFieldName(Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY_OF_MONTH = "day of month"
    MONTH = "month"
    DAY_OF_WEEK = "day of week"


class CronFieldType(Enum):
    STAR = re.compile(r"^\*$")
    NUMERIC = re.compile(r"^[0-9]+$", )
    RANGE = re.compile(r"^[0-9]+-[0-9]+$")
    STEP = re.compile(r"^([0-9]+-[0-9]+|\*|[0-9]+)/([0-9]+)$")
    LIST = re.compile(r"^[0-9\*\-\/]+,[0-9\*\-\/]+$")


@dataclass
class CronFieldAttribute:
    field_name: CronFieldName
    field_type: CronFieldType
    field_val: str
    min: int
    max: int


@dataclass
class CronFieldOutput:
    field_name: CronFieldName
    expr: str
    values: List[int] = field(default_factory=list)
