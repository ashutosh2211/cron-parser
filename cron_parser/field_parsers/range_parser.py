from typing import List

import cron_parser.field_parsers.cron_field_parser_factory as parser_factory
from cron_parser.cron_fields import CronFieldAttribute, CronFieldType
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.field_parser import FieldParser
from cron_parser.field_parsers.numeric_parser import NumericParser
from cron_parser.utils import is_in_range_inclusive, convert_str_to_int, create_range_inclusive


class RangeParser(FieldParser):

    def parse(self, cron_field: CronFieldAttribute) -> List[int]:
        field_name = cron_field.field_name
        field_val = cron_field.field_val

        values = field_val.split("-")

        if len(values) != 2:
            raise InvalidFieldValue(
                f"Field value: {field_val} for field: {field_name.value} does not follow the syntax for range")

        for val in values:
            cron_type = CronFieldType.NUMERIC
            parser: NumericParser = parser_factory.CronFieldParserFactory.get_parser(cron_type)
            parser.parse(CronFieldAttribute(field_name, cron_type, val, cron_field.min, cron_field.max))

        start, end = values

        range_min = convert_str_to_int(start)
        range_max = convert_str_to_int(end)

        if not is_in_range_inclusive(range_min, cron_field.min, cron_field.max) \
                or not is_in_range_inclusive(range_max, cron_field.min, cron_field.max):
            raise InvalidFieldValue(
                f"Field value for field: {field_name.value} is not in allowed range: {cron_field.min} - {cron_field.max}")

        return create_range_inclusive(range_min, range_max)
