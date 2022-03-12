from typing import List

from cron_parser.cron_fields import CronFieldAttribute
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.field_parser import FieldParser
from cron_parser.utils import is_string_numeric, is_in_range_inclusive, convert_str_to_int


class NumericParser(FieldParser):

    def parse(self, cron_field: CronFieldAttribute) -> List[int]:
        field_name = cron_field.field_name
        field_val = cron_field.field_val

        if is_string_numeric(field_val):
            field_val_int = convert_str_to_int(field_val)

            if not is_in_range_inclusive(field_val_int, cron_field.min, cron_field.max):
                raise InvalidFieldValue(
                    f"Field value: {field_val} for field: {field_name.value} is not in allowed range: {cron_field.min} - {cron_field.max}")
            return [field_val_int]

        raise InvalidFieldValue(f"{field_val} is not a valid field value for field: {field_name.value}")
