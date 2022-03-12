import logging
from typing import List

from cron_parser.cron_fields import CronFieldAttribute
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.field_parser import FieldParser
from cron_parser.utils import create_range_inclusive

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class StarParser(FieldParser):

    def parse(self, cron_field: CronFieldAttribute) -> List[int]:
        field_name = cron_field.field_name
        field_val = cron_field.field_val

        if field_val != "*":
            err_msg = f"Invalid field value: {field_val} for field: {field_name.name}, does not follow the syntax for star"
            logger.error(err_msg)
            raise InvalidFieldValue(err_msg)

        if cron_field.min is None or cron_field.max is None:
            err_msg = f"Field range is not present for field: {field_name.name}"
            logger.error(err_msg)
            raise InvalidFieldValue(err_msg)

        return create_range_inclusive(cron_field.min, cron_field.max)
