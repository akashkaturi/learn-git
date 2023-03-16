from tut2.sample import validate_age
import pytest


def test_validate_age():
    validate_age(10)


def test_validate_age():
    # we use with when we expect an exception
    with pytest.raises(ValueError) as exec_info:
        validate_age(-1)
    assert str(exec_info.value) == "Age cannot be less than 0"

def test_validate_age_type_2():
    with pytest.raises(ValueError,match="Age cannot be less than 0"):
        validate_age(-10)