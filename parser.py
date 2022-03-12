import argparse
import logging

from cron_parser.config import Config
from cron_parser.expression_parser import ExpressionParser
from cron_parser.formatters.string_formatter import StringFormatter

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


def main():
    config_data = Config("cron_parser/config.yml")
    expression_parser = ExpressionParser(config_data, StringFormatter())

    arg_parser = argparse.ArgumentParser(description='Parse a given cron expression')

    arg_parser.add_argument(
        'cron_expression',
        metavar='cron_expression',
        type=str,
        help='the cron expression to be parsed'
    )

    args = arg_parser.parse_args()

    expression = args.cron_expression
    expression_parser.parse_and_display(expression)


if __name__ == "__main__":
    main()
