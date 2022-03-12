import pytest

from cron_parser.cron_fields import CronFieldAttribute, CronFieldName, CronFieldType
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.numeric_parser import NumericParser


class TestNumericParser:

    def test_parse_happy_path(self):
        parser_obj = NumericParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == [2]

    def test_parse_out_of_bounds(self):
        parser_obj = NumericParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "24",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

    def test_parse_invalid_expression(self):
        parser_obj = NumericParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2/2",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

    def test_parse_empty_expression(self):
        parser_obj = NumericParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)
