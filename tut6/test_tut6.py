from sample_tut6 import Student
from datetime import datetime
import pytest


@pytest.fixture(scope="function")
def dummy_student():
    return Student("Akash", datetime(2000, 1, 1), "CSE")


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 0
