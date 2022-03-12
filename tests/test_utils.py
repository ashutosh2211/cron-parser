import pytest

from cron_parser.utils import create_range_inclusive, is_in_range_inclusive, convert_str_to_int, is_string_numeric, \
    flatten_lists


class Testutils:

    @pytest.mark.parametrize("lower_bound, upper_bound, expected",
                             [(3, 8, [3, 4, 5, 6, 7, 8]), (5, 3, [])])
    def test_create_range_inclusive(self, lower_bound, upper_bound, expected):
        res = create_range_inclusive(lower_bound, upper_bound)

        assert res == expected

    @pytest.mark.parametrize("value, lower_bound, upper_bound, expected",
                             [(5, 3, 8, True), (5, 1, 3, False)])
    def test_is_in_range_inclusive(self, value, lower_bound, upper_bound, expected):
        res = is_in_range_inclusive(value, lower_bound, upper_bound)
        assert res == expected

    @pytest.mark.parametrize("value, expected", [("22", 22), ("1", 1)])
    def test_convert_str_to_int(self, value, expected):
        res = convert_str_to_int(value)
        assert res == expected

    @pytest.mark.parametrize("value", ["5-3", "5-20/2", "*"])
    def test_convert_str_to_int_exception(self, value):
        with pytest.raises(ValueError) as exc:
            convert_str_to_int(value)

    @pytest.mark.parametrize("value, expected", [("22", True), ("5-3", False), ("5-20/2", False), ("*", False)])
    def test_is_string_numeric(self, value, expected):
        res = is_string_numeric(value)
        assert res == expected

    @pytest.mark.parametrize("value, expected", [([[1], [2, 3], [4]], [1, 2, 3, 4]), ([[1, 2, 3]], [1, 2, 3]), ([[]], [])])
    def test_flatten_lists(self, value, expected):
        res = flatten_lists(value)
        assert res == expected
