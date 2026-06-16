from fuel import checks


def test_checks_valid_values():
    assert checks("1/2") == "50%"
    assert checks("1/4") == "25%"
    assert checks("3/4") == "75%"
    assert checks("1/100") == "E"
    assert checks("99/100") == "F"


def test_checks_invalid_values():
    assert checks("2/1") is False
    assert checks("1/0") is False
    assert checks("abc") is False