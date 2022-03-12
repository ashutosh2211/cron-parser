import pytest

from cron_parser.expression_parser import ExpressionParser


@pytest.fixture
def expression_parser_fixture(valid_config_fixture, formatter_fixture):
    return ExpressionParser(valid_config_fixture, formatter_fixture)


class TestParser:

    def test_parser_valid_expression(self, expression_parser_fixture: ExpressionParser):
        expression_parser_fixture.parse_and_display("1 0 1 */2 * /usr")

    def test_parser_invalid_expression(self, expression_parser_fixture: ExpressionParser):
        expression_parser_fixture.parse_and_display("1 0 1 *,* * /usr")

    @pytest.mark.parametrize("expression, expected",
                             [("1 0 1 *,* * /usr", True), ("1 0 1 * /usr", False),
                              ("", False), ("1 0 1  2  * du", True)])
    def test_validate_expression(self, expression, expected, expression_parser_fixture: ExpressionParser):
        is_valid, _ = expression_parser_fixture._validate_expression(expression)

        assert is_valid == expected
