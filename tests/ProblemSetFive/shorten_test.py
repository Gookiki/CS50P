from shorten import shorten
import pytest

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("AEIOU") == ""
    assert shorten("") == ""
