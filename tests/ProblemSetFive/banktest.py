from bank import value
import pytest
def test_value():
    assert value("Hello") == 100
    assert value("hello") == 100    
    assert value("Hi") == 20
    assert value("aojfwa") == 0