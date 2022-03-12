from typing import List


def create_range_inclusive(minimum: int, maximum: int) -> List[int]:
    """
    Creates a list of values between a given range including the lower and upper bound
    :param minimum: Lower bound for the range
    :param maximum: Upper bound for the range
    :return: List of values
    """
    return list(range(minimum, maximum + 1))


def is_in_range_inclusive(val: int, minimum: int, maximum: int) -> bool:
    """
    Checks if a given val is within a given range (including the lower and upper bounds)
    :param val: value to check
    :param minimum: lower bound
    :param maximum: upper bound
    :return: boolean result
    """
    return minimum <= val <= maximum


def convert_str_to_int(val: str) -> int:
    """
    Convert a given string value to int if it is parseable
    :param val: String value
    :return: Integer value (if parseable) else raises Exception
    """
    if is_string_numeric(val):
        return int(val)

    raise ValueError(f"Not able to cast expression :{val} to int")


def is_string_numeric(val: str) -> bool:
    """
    Checks if a given string value is parseable to an integer
    :param val: string value
    :return: boolean result
    """
    try:
        int(val)
    except ValueError as exc:
        return False

    return True


def flatten_lists(lists: List[List]) -> List:
    """
    Flattens a list of list to a single level
    :param lists: list of lists
    :return: flattened list
    """
    return [val for sublist in lists for val in sublist]
