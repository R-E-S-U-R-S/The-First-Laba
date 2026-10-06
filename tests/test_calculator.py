import pytest

from src.toolkit.calculator import calc
from src.toolkit.errors import CalcErrors

@pytest.mark.parametrize("test_input,expected", [("126+3.1", 129.1), ("-12**2", 144), ("10*-2", -20), ("-(6)", -6), ("-(141//3)", -47), ("(12+6)*       2", 36), ("123%6", 3)])
def test_calc_successful(test_input, expected):
    assert calc(test_input, 5) == expected

@pytest.mark.parametrize("test_input", ["126++3.1", "-12***2", "Text input", "12/0", "++++"])
def test_calc_failure(test_input):
    with pytest.raises(CalcErrors):
        calc(test_input, 5)