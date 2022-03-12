import logging
import re
from typing import List

from cron_parser.config import Config
from cron_parser.cron_field_factory import CronFieldFactory
from cron_parser.cron_fields import CronFieldName, CronFieldOutput, CronFieldAttribute
from cron_parser.exceptions import InvalidExpression
from cron_parser.field_parsers.cron_field_parser_factory import CronFieldParserFactory
from cron_parser.formatters.output_formatter import OutputFormatter

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class ExpressionParser:

    def __init__(self, config_obj: Config, output_formatter: OutputFormatter):
        self._config = config_obj
        self._output_formatter = output_formatter

    def _validate_expression(self, expression: str):
        expression_parts = []

        if not expression:
            return False, expression_parts

        replaced_expr = _RE_COMBINE_WHITESPACE.sub(" ", expression).strip()

        if not replaced_expr:
            return False, expression_parts

        expression_parts = replaced_expr.split(" ")

        if len(expression_parts) < 6:
            return False, expression_parts

        return True, expression_parts

    def parse_and_display(self, expression: str):
        is_valid, split_expression = self._validate_expression(expression)

        if not is_valid:
            raise InvalidExpression(expression)

        cron_expression = split_expression[:-1]
        cron_command = split_expression[-1]

        cron_field_names: List[CronFieldName] = [f for f in CronFieldName]

        cron_fields: List[CronFieldAttribute] = self._parse_cron_expression(cron_expression, cron_field_names)
        cron_field_output_list: List[CronFieldOutput] = self._parse_cron_fields(cron_fields)

        self._display_output(cron_field_output_list, cron_command)

    def _parse_cron_expression(self, cron_field_vals: List[str], cron_field_names: List[CronFieldName]):
        res = []
        cron_field_factory = CronFieldFactory(self._config)

        for val, cron_field in zip(cron_field_vals, cron_field_names):
            res.append(cron_field_factory.get_field(cron_field, val))

        return res

    def _parse_cron_fields(self, cron_fields: List[CronFieldAttribute]):
        res = []
        for cron_field in cron_fields:
            field_name = cron_field.field_name
            parser = CronFieldParserFactory.get_parser(cron_field.field_type)
            parsed_list = parser.parse(cron_field)
            res.append(CronFieldOutput(field_name, cron_field.field_val, parsed_list))

        return res

    def _display_output(self, cron_field_output_list: List[CronFieldOutput], cron_command: str):
        res_str = self._output_formatter.format(cron_field_output_list, cron_command)
        print(res_str)
