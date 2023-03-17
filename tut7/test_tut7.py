from sample_tut7 import Student, get_topper
from datetime import datetime
import pytest


# here were are making a factory fixture, so this fixture can be used as a parameter for creating tests
@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "CSE", credits)

    return _make_dummy_student


# here students starts storing the fixture objects which can be later used for assertions
def test_get_topper_top(make_dummy_student):
    students = [
        make_dummy_student("ram", 21),
        make_dummy_student("bheem", 19),
        make_dummy_student("ravi", 22),
    ]

    topper = get_topper(students)
    assert topper == students[2]
    assert students[2].name == "ravi"


print("glpat-ag3xiGGyygw9o_eesm7z")
