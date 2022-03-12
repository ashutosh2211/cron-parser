from abc import ABC, abstractmethod
from typing import List

from cron_parser.cron_fields import CronFieldAttribute


class FieldParser(ABC):

    @abstractmethod
    def parse(self, cron_field: CronFieldAttribute) -> List[int]:
        """

        :param expressions:
        :type cron_field: object
        """
        raise NotImplementedError("An implementation of this class is needed")
