import logging
from typing import List

from cron_parser.cron_field_factory import CronFieldFactory
from cron_parser.cron_fields import CronFieldAttribute
from cron_parser.exceptions import InvalidFieldValue
import cron_parser.field_parsers.cron_field_parser_factory as parser_factory
from cron_parser.field_parsers.field_parser import FieldParser
from cron_parser.utils import is_in_range_inclusive, convert_str_to_int, create_range_inclusive

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class StepParser(FieldParser):

    def parse(self, cron_field: CronFieldAttribute) -> List[int]:
        field_name = cron_field.field_name
        field_val = cron_field.field_val

        values = field_val.split("/")

        if len(values) != 2:
            err_msg = f"Invalid field value: {field_val} for field: {field_name.name}"
            logger.error(err_msg)
            raise InvalidFieldValue(err_msg)

        range_elem, step = values

        cron_field_type = CronFieldFactory.get_cron_field_type(range_elem)
        parser: FieldParser = parser_factory.CronFieldParserFactory.get_parser(cron_field_type)

        value_range = parser.parse(
            CronFieldAttribute(field_name, cron_field_type, range_elem, cron_field.min, cron_field.max))

        if len(value_range) == 1:
            range_min = value_range[0]
            range_max = cron_field.max
        else:
            range_min = value_range[0]
            range_max = value_range[-1]

        step = convert_str_to_int(step)

        if not is_in_range_inclusive(range_min, cron_field.min, cron_field.max) \
                or not is_in_range_inclusive(range_max, cron_field.min, cron_field.max):
            err_msg = f"Invalid field value: {field_val} for field: {field_name.name}, " \
                      f"not in allowed range: {cron_field.min} - {cron_field.max}"
            logger.error(err_msg)
            raise InvalidFieldValue(err_msg)

        values = create_range_inclusive(range_min, range_max)

        return [values[i] for i in range(len(values)) if i % step == 0]
