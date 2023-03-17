from sample_tut8 import Student
from datetime import datetime
import pytest


@pytest.fixture
def dummy_student(request):
    return Student("Akash", datetime(2000, 1, 1), "CSE", request.param)


# here were are making a factory fixture, so this fixture can be used as a parameter for creating tests
@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "CSE", credits)

    return _make_dummy_student
