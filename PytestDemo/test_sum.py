import pytest
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_numbers_parametrize(setup,a, b, expected):
    assert a+b == expected
