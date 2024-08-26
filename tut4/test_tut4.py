import pytest
from sample4 import add


@pytest.mark.parametrize(
    "a,b,c", [(1, 2, 3), ("a", "b", "ab"), (10, 20, 30)], ids=["num", "str", "num"]
)
def test_add_4(a, b, c):
    assert add(a, b) == c
