from cron_parser.cron_fields import CronFieldOutput, CronFieldName
from cron_parser.formatters.string_formatter import StringFormatter


class TestStringFormatter:

    def test_format_field(self):
        cron_field_output = CronFieldOutput(
            CronFieldName.MINUTE,
            "1, 5",
            [1, 5]
        )

        formatter = StringFormatter(spacing=25)
        res = formatter.format_field(cron_field_output)

        assert res == f"{cron_field_output.field_name.name.lower(): <{25}}1 5"

    def test_format_(self):
        cron_field_outputs = [
            CronFieldOutput(
                CronFieldName.MINUTE,
                "1, 5",
                [1, 5]
            ), CronFieldOutput(
                CronFieldName.HOUR,
                "9-12",
                [9, 10, 11, 12]
            )
        ]
        cron_command = '/usr/find'
        formatter = StringFormatter(spacing=25)
        res = formatter.format(cron_field_outputs, cron_command)

        assert (
            res ==
            """minute                   1 5\nhour                     9 10 11 12\ncommand                  /usr/find"""
        )
