import pytest
@pytest.mark.smoke
def test_strings_match(setup):
    msg = "Hello Word"
    assert msg == "Hello World","Strings mismatch"
