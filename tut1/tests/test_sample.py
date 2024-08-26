import pytest
from tut1.sample import add


def test_add():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


class TestSample:
    def test_add_num(self):
        assert add(4, 5) == 9

    def test_add_str(self):
        assert add("x", "y") == "xy"
