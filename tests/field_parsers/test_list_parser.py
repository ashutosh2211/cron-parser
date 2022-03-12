import pytest

from cron_parser.cron_fields import CronFieldAttribute, CronFieldName, CronFieldType
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.list_parser import ListParser


class TestListParser:

    def test_parse_happy_path(self):
        parser_obj = ListParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2,5",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == [2, 5]

    def test_parse_with_multiple_values(self):
        parser_obj = ListParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2,5,7",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == [2, 5, 7]

    def test_parse_out_of_bounds(self):
        parser_obj = ListParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2,31",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

        assert f"Field value: 31 for field: {cron_field.field_name.value} " \
               f"is not in allowed range: {cron_field.min} - {cron_field.max}" == str(exc.value)

    def test_parse_invalid_expression(self):
        parser_obj = ListParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "1,2,",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

    def test_parse_composite_expression(self):
        parser_obj = ListParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "1-2,3-5/2",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == [1, 2, 3, 5]