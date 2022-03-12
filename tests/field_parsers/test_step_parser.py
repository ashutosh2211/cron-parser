import pytest

from cron_parser.cron_fields import CronFieldAttribute, CronFieldName, CronFieldType
from cron_parser.exceptions import InvalidFieldValue
from cron_parser.field_parsers.step_parser import StepParser


class TestRangeParser:

    def test_parse_happy_path(self):
        parser_obj = StepParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "3-10/2",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == [3, 5, 7, 9]

    def test_parse_out_of_bounds(self):
        parser_obj = StepParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "3-26/2",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

    def test_parse_non_range_step(self):
        parser_obj = StepParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "18/2",
            0,
            23
        )

        res = parser_obj.parse(cron_field)

        assert res == [18, 20, 22]

    def test_parse_invalid_step_value(self):
        parser_obj = StepParser()

        cron_field = CronFieldAttribute(
            CronFieldName.HOUR,
            CronFieldType.RANGE,
            "18",
            0,
            23
        )

        with pytest.raises(InvalidFieldValue) as exc:
            res = parser_obj.parse(cron_field)

        assert f"Invalid field value: 18 for field: {cron_field.field_name.name}" == str(exc.value)
