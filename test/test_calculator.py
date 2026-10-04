import pytest

from calculator import calc


# todo тесты ещё доделай пжпжпжпж
@pytest.mark.parametrize("test_input,expected", [("126+3.1", 129.1), ("-12**2", 16)])
def test_calc(test_input, expected):
    assert calc(test_input)==expected