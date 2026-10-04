import pytest

from src.toolkit.calculator import calc


@pytest.mark.parametrize("test_input,expected", [("126+3.1", 129.1), ("-12**2", 144)])
def test_calc(test_input, expected):
    assert calc(test_input, 5) == expected


