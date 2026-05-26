from fuel import checks
import pytest

def test_checks():
    assert checks("1/2") == "50%"
    assert checks("1/4") == "25%"
    assert checks("3/4") == "75%"
    assert checks("1/100") == "E"
    assert checks("99/100") == "F"
    assert checks("2/1") == False
    assert checks("1/0") == False
    assert checks("abc") == False