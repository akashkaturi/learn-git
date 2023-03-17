from sample_tut8 import Student, is_eligible_for_degree
from datetime import datetime
import pytest


# writing test cases for the fixtures
def test_eligible_for_degree(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("Sam", 21)) == True


# parametrizing the fixture factory
@pytest.mark.parametrize(
    "credits,expected", [(19, False), (21, True)], ids=["Ineligible", "Eligible"]
)
def test_degree_eligibility(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student("sam", credits)) is expected


# This method doesnot require fixture factory to implement, we can use indirect and directly use the fixture for tests
@pytest.mark.parametrize(
    "dummy_student,expected",
    [(19, False), (21, True)],
    indirect=["dummy_student"],
    ids=["Ineligible", "Eligible"],
)
def test_dummy_fixture(dummy_student, expected):
    assert is_eligible_for_degree(dummy_student) is expected
