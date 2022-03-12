import pytest

from cron_parser.cron_fields import CronFieldAttribute, CronFieldName, CronFieldType
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.star_parser import StarParser


class TestStarParser:

    def test_parse_happy_path(self):
        parser_obj = StarParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "*",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == list(range(0, 24))

    def test_parse_invalid_expression(self):
        parser_obj = StarParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "*/2",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

    def test_parse_invalid_bounds(self):
        parser_obj = StarParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "*/2",
            None,
            None
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)
