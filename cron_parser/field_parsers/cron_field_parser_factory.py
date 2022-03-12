from cron_parser.cron_fields import CronFieldType
import cron_parser.field_parsers.numeric_parser as numeric_parser
import cron_parser.field_parsers.range_parser as range_parser
import cron_parser.field_parsers.star_parser as star_parser
import cron_parser.field_parsers.step_parser as step_parser


class CronFieldParserFactory:

    @staticmethod
    def get_parser(cron_field_type):
        if cron_field_type == CronFieldType.STAR:
            return star_parser.StarParser()
        elif cron_field_type == CronFieldType.NUMERIC:
            return numeric_parser.NumericParser()
        elif cron_field_type == CronFieldType.RANGE:
            return range_parser.RangeParser()
        elif cron_field_type == CronFieldType.STEP:
            return step_parser.StepParser()
