import pytest

from cron_parser.cron_fields import CronFieldAttribute, CronFieldName, CronFieldType
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.range_parser import RangeParser


class TestRangeParser:

    def test_parse_happy_path(self):
        parser_obj = RangeParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2-5",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == [2, 3, 4, 5]

    def test_parse_out_of_bounds(self):
        parser_obj = RangeParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2-31",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

    def test_parse_invalid_expression(self):
        parser_obj = RangeParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "2-31-1",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

    def test_parse_inverted_range(self):
        parser_obj = RangeParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "11-3",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

        assert f"Field value: 11-3 for field: {cron_field.field_name.value} " \
                      f"is not in allowed range: {cron_field.min} - {cron_field.max}" == str(exc.value)
