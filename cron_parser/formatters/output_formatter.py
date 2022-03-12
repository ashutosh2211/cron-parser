from abc import ABC, abstractmethod
from typing import List

from cron_parser.cron_fields import CronFieldOutput


class OutputFormatter(ABC):

    @abstractmethod
    def format(self, cron_field_outputs: List[CronFieldOutput], cron_command: str):
        raise NotImplementedError("An implementation of this class is needed")
