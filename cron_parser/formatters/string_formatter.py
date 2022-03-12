from typing import List

from cron_parser.cron_fields import CronFieldOutput
from cron_parser.formatters.output_formatter import OutputFormatter


class StringFormatter(OutputFormatter):

    def __init__(self, spacing=25):
        self._spacing = spacing

    def format(self, cron_field_outputs: List[CronFieldOutput], cron_command: str) -> str:
        res = "\n".join(list(map(self.format_field, cron_field_outputs)))
        res += f"\n{self._format_key_value('command', cron_command)}"

        return res

    def format_field(self, cron_field_parsed: CronFieldOutput) -> str:
        name = cron_field_parsed.field_name.name.replace("_", " ").lower()
        values = list(map(str, cron_field_parsed.values))
        val = " ".join(values)

        return self._format_key_value(name, val)

    def _format_key_value(self, key, value) -> str:
        return f"{key: <{self._spacing}}{value}"
