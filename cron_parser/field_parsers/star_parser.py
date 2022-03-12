from typing import List

from cron_parser.cron_fields import CronFieldAttribute
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.field_parser import FieldParser
from cron_parser.utils import create_range_inclusive


class StarParser(FieldParser):

    def parse(self, cron_field: CronFieldAttribute) -> List[int]:
        field_name = cron_field.field_name
        field_val = cron_field.field_val

        if field_val != "*":
            raise InvalidFieldValue(
                f"Field value: {field_val} for field: {field_name.value} does not follow the syntax for star"
            )

        if cron_field.min is None or cron_field.max is None:
            raise InvalidFieldValue(f"Field range is not present for field: {field_name}")

        return create_range_inclusive(cron_field.min, cron_field.max)
