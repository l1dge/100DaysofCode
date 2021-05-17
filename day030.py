import pytest


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    ans = len(text) - len(text.lstrip(" "))

    return ans


# Tests
@pytest.mark.parametrize(
    "input_string, count",
    [
        ("string  ", 0),
        ("  string", 2),
        ("    string", 4),
        ("            string", 12),
        ("\t\tstring", 0),
        ("  str  ing", 2),
        ("  str  ", 2),
    ],
)
def test_count_indents(input_string, count):
    assert count_indents(input_string) == count