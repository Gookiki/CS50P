from vanityplate import is_valid
import pytest
import re

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS50P2024") == False
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CS50P2") == False
    assert is_valid("CS50P02") == False
    assert is_valid("CS50P0") == False


def test_zero_placement():
    assert is_valid("CS50P0") == False
    assert is_valid("ABC012") == False
    assert is_valid("AB0") == False


def test_alphanumeric_characters():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
