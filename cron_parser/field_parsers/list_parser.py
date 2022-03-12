import logging
from typing import List

from cron_parser.cron_field_factory import CronFieldFactory
from cron_parser.cron_fields import CronFieldAttribute
from cron_parser.exceptions import InvalidFieldValue
import cron_parser.field_parsers.cron_field_parser_factory as parser_factory
from cron_parser.field_parsers.field_parser import FieldParser
from cron_parser.utils import is_in_range_inclusive, flatten_lists

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class ListParser(FieldParser):

    def parse(self, cron_field: CronFieldAttribute) -> List[int]:
        field_name = cron_field.field_name
        field_val = cron_field.field_val
        res = []

        values = field_val.split(",")

        for v in values:
            cron_field_type = CronFieldFactory.get_cron_field_type(v)
            parser: FieldParser = parser_factory.CronFieldParserFactory.get_parser(cron_field_type)

            res.append(parser.parse(
                CronFieldAttribute(field_name, cron_field_type, v, cron_field.min, cron_field.max)))

        res = flatten_lists(res)
        res = sorted(list(set(res)))

        if not res:
            err_msg = f"Empty value: {field_val} for field: {field_name.name}"
            logger.error(err_msg)
            raise InvalidFieldValue(err_msg)
        else:
            range_min = res[0]
            range_max = res[-1]

        if not is_in_range_inclusive(range_min, cron_field.min, cron_field.max) \
                or not is_in_range_inclusive(range_max, cron_field.min, cron_field.max):

            err_msg = f"Field value: {field_val} for field: {field_name.name} " \
                      f"is not in allowed range: {cron_field.min} - {cron_field.max}"
            logger.error(err_msg)
            raise InvalidFieldValue(err_msg)

        return res
