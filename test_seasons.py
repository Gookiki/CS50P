import pytest
from seasons import main

def tests():
    assert main("2001-01-01") == "13913280.0"

tests()
