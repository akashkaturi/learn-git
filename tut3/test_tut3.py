import pytest
from sample import add
import sys


@pytest.mark.skip(reason="Wanted to skip this for this test")
def test_add():
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info > (3, 9), reason="use python 3.7 or less")
def test_add_str():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "darwin", reason="Dont run on macos")
def test_add_str2():
    assert add("e", 1) == "ex"
    raise Exception()


class TestSample:
    def test_add_num(self):
        assert add(4, 5) == 9

    def test_add_str(self):
        assert add("x", "y") == "xy"
