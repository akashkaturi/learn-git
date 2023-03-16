from sample_tut7 import Student, get_topper
from datetime import datetime
import pytest


@pytest.fixture
def dummy_student():
    return Student("Akash", datetime(2000, 1, 1), "CSE", 20)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "CSE", credits)

    return _make_dummy_student


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20


def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("ram", 21),
        make_dummy_student("bheem", 19),
        make_dummy_student("ravi", 22),
    ]

    topper = get_topper(students)
    assert topper == students[2]
