import pytest

from src.toolkit.calculator import calc, str_sep


# todo тесты ещё доделай пжпжпжпж
@pytest.mark.parametrize("test_input,expected", [("126+3.1", 129.1), ("126+3.3", 129.3)])
def test_calc(test_input, expected):
    assert calc(test_input)==expected

def test_tokeniser():
    assert str_sep("12+6")==([12.0, 6.0], ["+"])